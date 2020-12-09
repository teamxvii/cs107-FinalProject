from FADiff import FADiff


class Scal:
    _tmp_der = None                     # For evaluating derivative

    def __init__(self, val, inputs=None, name=None, new_input=False):
        self._val = val
        if inputs is None:
            inputs = {}
        self._inputs = inputs           # Roots of an instance
        if new_input:
            self._inputs[self] = []
            FADiff._revscal_inputs.append(self)
        self._name = name

    # TODO: Check works correctly
    def __add__(self, other):
        try:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, 1]]
            for root in other._inputs.keys():
                if root in inputs:
                    inputs[root].append([other, 1])
                else:
                    inputs[root] = [[other, 1]]
            return Scal(self._val + other._val, inputs)
        except AttributeError:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, 1]]
            return Scal(self._val + other, inputs)

    def __radd__(self, other):
        return self.__add__(other)

    # TODO: Check works correctly
    def __mul__(self, other):
        try:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, other._val]]
            for root in other._inputs.keys():
                if root in inputs:
                    inputs[root].append([other, self._val])
                else:
                    inputs[root] = [[other, self._val]]
            return Scal(self._val * other._val, inputs)
        except AttributeError:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, other]]
            return Scal(self._val * other, inputs)

    def __rmul__(self, other):
        return self.__mul__(other)

    
    ## TODO: check coded by xiaoxuan
    def __truediv__(self, other):
        """
        Divides self by other (self / other)
        
        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: new Scal object
        """
        try:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, 1 / other._val]]
            for root in other._inputs.keys():
                if root in inputs:
                    inputs[root].append([other, -self._val / (other._val**2)])
                else:
                    inputs[root] = [[other, -self._val / (other._val**2)]]
            return Scal(self._val / other._val, inputs)

    def __rtruediv__(self, other):
        """
        Divides other by self (other / self)
        
        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: new Scal object
        """
        for root in self._inputs.keys():
            inputs[root].append([self, -other / (self._val**2)])
        return Scal(other / self._val, inputs)
    
    def __pow__(self,other):
        try:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, other._val*self._val**(other._val - 1)]]
            for root in other._inputs.keys():
                if root in inputs:
                    inputs[root].append([other, self._val**other._val*np.log(self._val)])
                else:
                    inputs[root] = [[other, self._val**other._val*np.log(self._val)]]
            return Scal(self._val**other._val, inputs)
        except AttributeError:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, other*self._val**(other-1)]]
            return Scal(self._val**other, inputs)
    
    def __rpow__(self,other):
        for root in self._inputs.keys():
            inputs[root] = [[self,other**self._val*np.log(other)]]
            
        return Scal(other**self._val, inputs)
    
    
    def __neg__(self,other):
        for root in self._inputs.keys():
            inputs[root] = [[self,-1]]
            
        return Scal(-self._val,inputs)
    
    ### Comparison Operators ### Same as fad

    def __eq__(self, other):
        """
        Checks if self equals other
        
        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: Boolean (True if self equals other, False otherwise)
        """
        try: # if other is a Scal
            return self._val == other._val
        except AttributeError: # if other is a scalar, but not an instance of Scal
            return self._val == other
        
    def __ne__(self, other):
        """
        Checks if self does not equal other
        
        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: Boolean (True if self does not equal other, False otherwise)
        """
        try: # if other is a Scal
            return self._val != other._val
        except AttributeError: # if other is a constant
            return self._val != other      
        
    def __lt__(self, other):
        """
        Checks if self is less than other
        
        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: Boolean (True if self is less than other, False otherwise)
        """
        try: # if other is a Scal
            return self._val < other._val
        except AttributeError: # if other is a constant
            return self._val < other 
        
    def __le__(self, other):
        """
        Checks if self is less than or equal to other
        
        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: Boolean (True if self is less than or equal to other, False otherwise)
        """
        try: # if other is a Scal
            return self._val <= other._val
        except AttributeError: # if other is a constant
            return self._val <= other   
        
    def __gt__(self, other):
        """
        Checks if self is greater than other
        
        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: Boolean (True if self is greater than other, False otherwise)
        """
        try: # if other is a Scal
            return self._val > other._val
        except AttributeError: # if other is a constant
            return self._val > other 
        
    def __ge__(self, other):
        """
        Checks if self is greater than or equal to other
        
        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: Boolean (True if self is greater than or equal to other, False otherwise)
        """
        try: # if other is a Scal
            return self._val >= other._val
        except AttributeError: # if other is a constant
            return self._val >= other 
    
    def __hash__(self):
        """
        Ensures that objects which are equal have the same hash value
        
        Inputs: self (Scal object)
        Returns: integer ID of self
        """
        return id(self)
    
    
    @property
    def val(self):
        return [self._val]

    # TODO: Check works correctly
    @property
    def der(self):
        parents = []
        for root in FADiff._revscal_inputs:  # Iterating w/this keeps var order
            if root in self._inputs.keys():
                Scal._tmp_der = 1
                self._back_trace(root)
                parents.append(Scal._tmp_der)
        return parents

    # TODO: Check works correctly
    def _back_trace(self, root):
        if self._inputs[root]:               # (Base case: list is empty @ root)
            for parent, part_der in self._inputs[root]:
                Scal._tmp_der = Scal._tmp_der * part_der
                parent._back_trace(root)
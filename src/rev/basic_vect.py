import numpy as np


class Vect:
    """
    Input: val jacobian dictionary of the list of derivtives
    """
    def __init__(self, val, ders=None):
        """
        input: val: value of the function, ders: list of derivative stored in a dictionary
        return a scalar object with value and derivative
        
        """
        self._val = val
        self._ders = ders
        
    def init_vect(self, inputs):
        """
        initialize a dictionary of lists of derivatives
        
        input: self, inputs: list of scalars
        return: dict of list of derivatives
        """
        self._ders = {}
        for i in inputs:
            self._ders[i] = int(id(self) == id(i))

        def __add__(self, other):
            try:
                ders_update = {}
                for i, j in self._ders.items():
                    ders_update[i] = [[j + other._ders[i]]]
                return Vect(self._val + other._val, ders_update)
            except AttributeError:
                return Vect(self._val + other, self._ders)

        def __radd__(self, other):
            return self.__add__(other)
        
        def __sub__(self, other):
            try:
                ders_update = {}
                for i,j in self._ders.items():
                    ders_update[i] = [[j - other._ders[i]]]
                return Vect(self._val - other._val, ders_update)
            except AttributeError:
                return Vect(self._val - other, self._ders)
            
        def __rsub__(self, other):
            return self.__sub__(other)
        
        def __mul__(self, other):
            try: 
                ders_update = {}
                for i,j in self._ders.items():
                    ders_update[i] = [self._val*other._ders[i] + j*other._val]
                return Vect(self._val*other._val, ders_update)
            except AttributeError:
                ders_update = {}
                for i,j in self._ders.items():
                    ders_update[i] = j*other
                return Vect(self._val*other, ders_update)
            
        def __rmul__(self, other):
            return self.__mul__(other)
        
        def __truediv__(self,other):
            ders_update = {}
            try:
                for i,j in self._ders.items():
                    ders_update[i] = [(j*other._val - other._ders[i]*self._val)/(other._val**2)]
                return Vect(self._val / other._val, ders_update)
            except AttributeError:
                for i,j in self._ders.items():
                    ders_update[i] = [j / other._val]
                return Vect(self._val / other, ders_update)
        def __rtruediv__(self,other):
            ders_update = {}
            for i,j in self._ders.items():
                ders_update[i] = [-other*j / (self._val**2)]
            return Vect(other / self._val, ders_update)
        
        def __pow__(self, other):
            ders_update = {}
            try:
                for i,j in self._ders.items():
                    ders_update[i] = [(self._val**other._val)*(np.log(self._val)*other._ders[i] + (other._val*j / self._val))]
                return Vect(self._val**other._val, ders_update)
            except AttributeError:
                for i,j in self._ders.items():
                    ders_update[i] = [other*(self._val)**(other - 1)*j]
                return Vect(self._val**other, ders_update)
            
        def __rpow__(self,other):
            ders_update = {}
            for i,j in self._ders.items():
                ders_update[i] = [(other**self._val)*np.log(other)*j]
            return Vect(other**self._val, ders_update)
            
        def __neg__(self,other):
            ders_update ={}
            for i,j in self._ders.items():
                ders_update[i] = -j
            return Vect(-self._val, ders_update)
        
        def __eq__(self, other):
            if (self._val == other._val) and (self._ders == other._ders):
                return True
            else:
                return False
            
        def __ne__(self, other):
            if (self._val == other._val) and (self._ders == other._ders):
                return False
            else:
                return True    
       
                
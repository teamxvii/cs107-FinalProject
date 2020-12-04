#!/usr/bin/env python3

from FADiff import FADiff


class Scal:
    """
    A class to...
    """
    def __init__(self, val, der=None, parents=[], name=None, new_input=False):
        """
        Constructs all the...

        Parameters
        ----------
            val : float
                value of the scalar variable
            der : float, dictionary
                derivative of the scalar variable
            parents : list of Scal objects
                the parent/grandparent vars of the variable
            name : str
                the name of the variable
            new_input : boolean
                if variable is an input variable
        """
        self._val = val
        if new_input:                       # Creating input var?
            self._der = {}                  # Add gradient dict for new var
            for var in FADiff.scal_inputs:    # Update gradient dicts for all vars
                self._der[var] = 0          # Partial der of others as 0 in self
                var._der[self] = 0          # Self's partial der as 0 in others
            self._der[self] = der           # Self's partial der in self
            FADiff.scal_inputs.append(self)   # Add self to global vars list
        else:
            self._der = der
        self.name = name  # TODO: Utilize if have time?
        self.parents = parents

    def __add__(self, other):
        """
        Adds...

        Parameters
        ----------
        other : Scal, constant
            the Scal object or constant being added to self

        Returns
        -------
        new Scal instance
        """
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der + other._der.get(var)
            parents = self.set_parents(self, other)
            return Scal(self._val + other._val, der, parents)
        except AttributeError:
            parents = self.set_parents(self)
            return Scal(self._val + other, self._der, parents)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = self._val * other._der.get(var) +\
                           part_der * other._val
            parents = self.set_parents(self, other)
            return Scal(self._val * other._val, der, parents)
        except AttributeError:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der * other
            parents = self.set_parents(self)
            return Scal(self._val * other, der, parents)

    def __rmul__(self, other):
        return self.__mul__(other)

    @property
    def val(self):
        return [self._val]

    @property
    def der(self):
        '''Returns partial derivatives wrt all root input vars used'''
        parents = []
        for var, part_der in self._der.items():
            if var in self.parents:
                parents.append(part_der)
        if parents:                           # For output vars
            return parents
        elif self in FADiff.scal_inputs:       # For input vars (no parents)
            return [self._der[self]]

    @staticmethod
    def set_parents(var1, var2=None):
        '''Sets parent/grandparent vars (including root input vars used)'''
        parents = []
        parents.append(var1)
        for parent in var1.parents:
            parents.append(parent)
        if var2:
            parents.append(var2)
            for parent in var2.parents:
                parents.append(parent)
        parents = list(set(parents))
        return parents

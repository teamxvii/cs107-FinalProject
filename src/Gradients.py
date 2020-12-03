#!/usr/bin/env python3

from FADiff import FADiff


class Scal_Func:
    def __init__(self, val, der=None, parents=[], name=None, new_input=False):
        self._val = val
        if new_input:  # Creating input var?
            self._der = {}
            for var in FADiff.vars_list:
                self._der[var] = 0         # Partial der of others' as 0 in self
                var._der[self] = 0         # Self's partial der as 0 in others
            self._der[self] = der          # Self's partial der as der in self
            FADiff.vars_list.append(self)  # Add self to global vars list
        else:
            self._der = der
        self.name = name  # TODO: Utilize somewhere?
        self.parents = parents

    def __add__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der + other.partial_der(var)
            parents = self.set_parents(self, other)
            return Scal_Func(self._val + other._val, der, parents)
        except AttributeError:
            parents = self.set_parents(self)
            return Scal_Func(self._val + other, self._der, parents)

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = self._val * other.partial_der(var) +\
                           part_der * other._val
            parents = self.set_parents(self, other)
            return Scal_Func(self._val * other._val, der, parents)
        except AttributeError:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der * other
            parents = self.set_parents(self)
            return Scal_Func(self._val * other, der, parents)

    def __rmul__(self, other):
        return self.__mul__(other)

    def partial_der(self, var):            # Returns partial deriv wrt var
        return self._der[var]

    @property
    def val(self):
        return [self._val]

    @property
    def der(self):                      # Returns partial derivs of calculation
        parents = []
        for key, value in self._der.items():
            if key in self.parents:
                parents.append(value)
        if parents:
            return parents
        elif self in FADiff.vars_list:       # For input vars (no parents)
            return [self._der[self]]

    @staticmethod
    def set_parents(var1, var2=None):   # Retrieves parent vars + grandparents
        parents = []
        parents.append(var1)
        for parent in var1.parents:
            parents.append(parent)
        if var2:
            parents.append(var2)
            for parent in var2.parents:
                parents.append(parent)
        parents = set(parents)
        parents = list(parents)
        return parents

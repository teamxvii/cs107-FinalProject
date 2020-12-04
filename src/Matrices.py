#!/usr/bin/env python3

import numpy as np
from FADiff import FADiff


class Vect:
    def __init__(self, vect, der=None, parents=[], name=None, new_input=False):
        self._val = np.array(vect)
        if new_input:
            self._der = {}
            for vec_var in FADiff.vects_list:
                self._der[vec_var] = 0
                vec_var._der[self] = 0
            self._der[self] = der * np.identity(len(vect))
            FADiff.vects_list.append(self)
        else:
            self._der = der
        self.name = name  # TODO: Utilize somewhere?
        self.parents = parents

    def __sub__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der - other._der.get(var)
            parents = self.set_parents(self, other)
            return Vect(self._val - other._val, der, parents)
        except AttributeError:
            parents = self.set_parents(self)
            return Vect(self._val - other, self._der, parents)

    def __rsub__(self, other):
        return self.__sub__(other)

    @property
    def val(self):
        return [self._val]

    @property
    def der(self):
        '''Returns partial derivatives wrt all root input vars used'''
        parents = []
        for key, value in self._der.items():
            if key in self.parents:
                parents.append(value)
        if parents:                      # For output vars
            return parents
        elif self in FADiff.vects_list:  # For input vars (no parents)
            return [self._der[self]]

    @staticmethod
    def set_parents(var1, var2=None):
        '''Sets parent/grandparent vars used (including root input vars)'''
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

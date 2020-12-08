#!/usr/bin/env python3

import numpy as np
from FADiff import FADiff


class Vect:
    def __init__(self, vect, der=None, parents=None, name=None, new_input=False):
        self._val = np.array(vect)
        if new_input:
            self._der = {}
            for vec_var in FADiff._fadvect_inputs:
                self._der[vec_var] = 0
                vec_var._der[self] = 0
            self._der[self] = der * np.identity(len(vect))
            FADiff._fadvect_inputs.append(self)
        else:
            self._der = der
        self._name = name  # TODO: Utilize if have time?
        if parents is None:
            parents = []
        self._parents = parents

    def __sub__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der - other._der.get(var)
            parents = self._set_parents(self, other)
            return Vect(self._val - other._val, der, parents)
        except AttributeError:
            parents = self._set_parents(self)
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
        for var, part_der in self._der.items():
            if var in self._parents:
                parents.append(part_der)
        if parents:                      # For output vars
            return parents
        elif self in FADiff._fadvect_inputs:  # For input vars (no parents)
            return [self._der[self]]

    @staticmethod
    def _set_parents(var1, var2=None):
        '''Sets parent/grandparent vars used (including root input vars)'''
        parents = []
        parents.append(var1)
        for parent in var1._parents:
            parents.append(parent)
        if var2:
            parents.append(var2)
            for parent in var2._parents:
                parents.append(parent)
        parents = list(set(parents))
        return parents

#!/usr/bin/env python3

from FADiff import FADiff


class Scal:
    _tmp_part_der = 0

    def __init__(self, val, der=None, parents=[],
                 roots=[], name=None, new_input=False):
        self._val = val
        self._grad = 0          # TODO: Not sure if need
        if new_input:
            self._der = {}
            for var in FADiff._revscal_inputs:
                self._der[var] = 0
                var._der[self] = 0
            self._der[self] = der
            FADiff._revscal_inputs.append(self)
        else:
            self._der = der
        self._name = name
        self._parents = parents
        self._root_inputs = roots

    def __add__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der + other._der.get(var)
            parents = [self, other]
            roots = self._set_roots(self, other)
            return Scal(self._val + other._val, der, parents, roots)
        except AttributeError:
            parents = [self]
            roots = self._set_roots(self)
            return Scal(self._val + other, self._der, parents, roots)

    def __radd__(self, other):
        return self.__add__(other)

    # TODO
    def __mul__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = self._val * other._der.get(var) +\
                           part_der * other._val
            parents = [self, other]
            roots = self._set_roots(self, other)
            return Scal(self._val * other._val, der, parents, roots)
        except AttributeError:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der * other
            parents = [self]
            roots = self._set_roots(self, other)
            return Scal(self._val * other, der, parents, roots)

    def __rmul__(self, other):
        return self.__mul__(other)

    @property
    def val(self):
        return [self._val]

    @property
    def der(self):
        parents = []
        for var in self._der.keys():
            if var in self._root_inputs:
                Scal._tmp_part_der = 1
                self._back_trace(var)
                parents.append(Scal._tmp_part_der)
        return parents

    def _back_trace(self, var):
        if not self._parents:             # Base case (at root var)
            return
        parent = None     # TODO: Raise exception if no parent found?
        for par in self._parents:         # Find parent with partial der wrt var
            if var == par or var in par._root_inputs:
                parent = par
                break
        Scal._tmp_part_der = Scal._tmp_part_der * self._der.get(var)
        parent._back_trace(var)

    @staticmethod
    def _set_roots(var1, var2=None):
        roots = []
        if not var1._parents and var1 in FADiff._revscal_inputs:  # Root parent
            roots.append(var1)
        else:
            for root in var1._root_inputs:
                roots.append(root)
        if var2:
            if not var2._parents and var2 in FADiff._revscal_inputs:  # Root parent
                roots.append(var2)
            else:
                for root in var2._root_inputs:
                    roots.append(root)
        return roots

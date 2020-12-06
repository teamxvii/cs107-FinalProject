#!/usr/bin/env python3

from FADiff import FADiff


class Scal:
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
        self._tmp_part_der = 0   # TODO: Should this be static (should work without)?

    def __add__(self, other):
        try:
            der = {}
            for var, part_der in self._der.items():
                der[var] = part_der + other._der.get(var)
            parents = [self, other]
            roots = self._set_roots(self, other)

            # TODO: Debugging
            new = Scal(self._val + other._val, der, parents, roots)
            print(f'{new} --> ')
            part_ders = []
            for var, part_der in new._der.items():
                part_ders.append(part_der)
            print(f'{part_ders}')
            return new

            # return Scal(self._val + other._val, der, parents, roots)
        except AttributeError:
            parents = [self]
            roots = self._set_roots(self)
            return Scal(self._val + other, self._der, parents, roots)

    def __radd__(self, other):
        return self.__add__(other)

    @property
    def val(self):
        return [self._val]

    @property
    def der(self):
        parents = []
        for var in self._der.keys():
            if var in self._root_inputs:
                self._tmp_part_der = 1
                self._back_trace(var)
                parents.append(self._tmp_part_der)
        return parents  # TODO: Should return correct thing

    def _back_trace(self, var):
        found = False
        parent = None
        for parent in self._parents:
            pass  # TODO
        # TODO: self._tmp_part_der = self._tmp_part_der * parent_part_der
        if not self._parents:                   # Base case
            return
        else:
            parent._back_trace(var)
        # TODO: Should return a column's partial deriv

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

#!/usr/bin/env python3

from FADiff import FADiff


class Scal:
    _tmp_part_der = 0  # TODO: Maybe can use?

    def __init__(self, val, inputs={}, parents=[],     # TODO: Need parents and roots or delete?
                 roots=[], name=None, new_input=False):
        self._val = val
        self._inputs = inputs           # Roots in the eval trace table
        if new_input:
            self._inputs[self] = []
            FADiff._revscal_inputs.append(self)
        self._der = 0  # TODO: Not sure if need
        self._name = name
        self._parents = parents         # Immediate parents of an instance
        self._root_inputs = roots       # TODO: Don't need (see below)? -- An instance's particular roots

    # TODO
    def __add__(self, other):
        inputs = {}
        for root in self._inputs.keys():
            inputs[root] = [[self, 1]]
        try:
            for root in other._inputs.keys():
                if inputs[root]:
                    inputs[root].append([other, 1])
                else:
                    inputs[root] = [[other, 1]]
            # parents = [self, other]
            # roots = self._set_roots(self, other)
            return Scal(self._val + other._val, inputs)#, parents, roots)
        except AttributeError:
            # parents = [self]
            # roots = self._set_roots(self)
            return Scal(self._val + other, inputs)#, parents, roots)

    def __radd__(self, other):
        return self.__add__(other)

    # TODO
    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        return self.__mul__(other)

    @property
    def val(self):
        return [self._val]

    # TODO
    @property
    def der(self):
        parents = []
        for root in FADiff._revscal_inputs:  # Iterating w/this keeps var order
            if root in self._root_inputs:  # TODO: Think can use self._inputs.keys() here instead
                self._tmp_part_der = 1  # TODO: Will this work instead of _der?
                self._back_trace(root)
                parents.append(self._tmp_part_der)
        return parents  # TODO: Should return correct thing

    # TODO
    def _back_trace(self, var):
        if self._inputs[var]:    # (Base case: list is empty @ root)
            pass

    # TODO: Don't think need this --
    # @staticmethod
    # def _set_roots(var1, var2=None):
    #     roots = []
    #     if not var1._parents and var1 in FADiff._revscal_inputs:  # Root parent
    #         roots.append(var1)
    #     else:
    #         for root in var1._root_inputs:
    #             roots.append(root)
    #     if var2:
    #         if not var2._parents and var2 in FADiff._revscal_inputs:  # Root parent
    #             roots.append(var2)
    #         else:
    #             for root in var2._root_inputs:
    #                 roots.append(root)
    #     return roots

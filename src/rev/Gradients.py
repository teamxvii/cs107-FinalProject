#!/usr/bin/env python3

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

    ### Comparison Operators ###

    def __eq__(self, other):
        if isinstance(other, Scal):
            return self.__key() == other.__key()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Scal):
            return self.__key() != other.__key()
        return NotImplemented

    def __key(self):
        return id(self)

    def __hash__(self):
        return hash(self.__key())

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

#!/usr/bin/env python3

from FADiff import FADiff
import numpy as np


class Scal:
    def __init__(self, val, inputs=None, name=None, new_input=False):
        self._val = val
        if inputs is None:
            inputs = {}
        self._inputs = inputs           # Roots of an instance
        if new_input:
            self._inputs[self] = []
            FADiff._revscal_inputs.append(self)
        self._name = name
        self._tmp_der = 0

    def __add__(self, other):
        try:
            inputs = {}
            for root in other._inputs.keys():
                inputs[root] = [[other, 1]]
            for root in self._inputs.keys():
                if root in inputs:
                    inputs[root].append([self, 1])
                else:
                    inputs[root] = [[self, 1]]
            return Scal(self._val + other._val, inputs)
        except AttributeError:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, 1]]
            return Scal(self._val + other, inputs)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        try:
            inputs = {}
            for root in other._inputs.keys():
                inputs[root] = [[other, -1]]
            for root in self._inputs.keys():
                if root in inputs:
                    inputs[root].append([self, 1])
                else:
                    inputs[root] = [[self, 1]]
            return Scal(self._val - other._val, inputs)
        except AttributeError:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, 1]]
            return Scal(self._val - other, inputs)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        try:
            inputs = {}
            for root in other._inputs.keys():
                inputs[root] = [[other, self._val]]
            for root in self._inputs.keys():
                if root in inputs:
                    inputs[root].append([self, other._val])
                else:
                    inputs[root] = [[self, other._val]]
            return Scal(self._val * other._val, inputs)
        except AttributeError:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, other]]
            return Scal(self._val * other, inputs)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Divides self by other (self / other)

        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: new Scal object
        """
        try:
            inputs = {}
            for root in other._inputs.keys():
                inputs[root] = [[other, -1 * self._val / (other._val ** 2)]]
            for root in self._inputs.keys():
                if root in inputs:
                    inputs[root].append([self, 1 / other._val])
                else:
                    inputs[root] = [[self, 1 / other._val]]
            return Scal(self._val / other._val, inputs)
        except AttributeError:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, 1 / other]]
            return Scal(self._val / other, inputs)

    def __rtruediv__(self, other):
        """
        Divides other by self (other / self)

        Inputs: self (Scal object), other (either Scal object or constant)
        Returns: new Scal object
        """
        inputs = {}
        for root in self._inputs.keys():
            inputs[root].append([self, -1 * other / (self._val ** 2)])
        return Scal(other / self._val, inputs)

    def __pow__(self, other):
        try:
            inputs = {}
            for root in other._inputs.keys():
                inputs[root] = [[other, np.log(self._val) * self._val ** other._val]]
            for root in self._inputs.keys():
                if root in inputs:
                    inputs[root].append([self, self._val ** (other._val - 1) * other._val])
                else:
                    inputs[root] = [[self, self._val ** (other._val - 1) * other._val]]
            return Scal(self._val ** other._val, inputs)
        except AttributeError:
            inputs = {}
            for root in self._inputs.keys():
                inputs[root] = [[self, self._val ** (other - 1) * other]]
            return Scal(self._val ** other, inputs)

    def __rpow__(self, other):
        inputs = {}
        for root in self._inputs.keys():
            inputs[root] = [[self, np.log(other) * other ** self._val]]
        return Scal(other ** self._val, inputs)

    def __neg__(self):
        inputs = {}
        for root in self._inputs.keys():
            inputs[root] = [[self, -1]]
        return Scal(-1 * self._val, inputs)

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
        return np.array(self._val)

    @property
    def der(self):
        part_ders = []
        for root in FADiff._revscal_inputs:  # Iterating w/this keeps var order
            if root in self._inputs.keys():
                self._tmp_der = 1
                self._back_trace(root)
                part_ders.append(root._tmp_der)
                self._tmp_der = 0
                self._undo_back_trace(root)
        return np.array(part_ders)

    def _back_trace(self, root):
        if self._inputs[root]:               # (Base case: list is empty @ root)
            for parent, part_der in self._inputs[root]:
                parent._tmp_der += self._tmp_der * part_der
                parent._back_trace(root)

    def _undo_back_trace(self, root):
        if self._inputs[root]:
            for parent, part_der in self._inputs[root]:
                parent._tmp_der = 0
                parent._undo_back_trace(root)

#!/usr/bin/env python3

import numpy as np
from FADiff import FADiff


class Vect:
    def __init__(self, val, inputs=None):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        return self.__sub__(other)

    def __eq__(self, other):
        if isinstance(other, Vect):
            return self.__key() == other.__key()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Vect):
            return self.__key() != other.__key()
        return NotImplemented

    def __key(self):
        return id(self)

    def __hash__(self):
        return hash(self.__key())

    @property
    def val(self):
        pass

    @property
    def der(self):
        pass

    @staticmethod
    def _set_parents(var1, var2=None):
        pass

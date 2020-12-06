#!/usr/bin/env python3

import numpy as np
from FADiff import FADiff


class Vect:
    def __init__(self):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        return self.__sub__(other)

    @property
    def val(self):
        pass

    @property
    def der(self):
        pass

    @staticmethod
    def _set_parents(var1, var2=None):
        pass

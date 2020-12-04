#!/usr/bin/env python3

import numpy as np
from FADiff import *


def sin(x):
    '''
    Returns the sum of two decimal numbers in binary digits.

        Parameters:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            binary_sum (str): Binary string of the sum of a and b
    '''
    try:
        der = {}
        for var in x._der.keys():
            der[var] = x._der.get(var) * np.cos(x._val)
        parents = x.set_parents(x)
        return Scal(np.sin(x._val), der, parents)
    except AttributeError:
        return np.sin(x)

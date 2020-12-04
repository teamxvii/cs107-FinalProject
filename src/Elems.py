#!/usr/bin/env python3

import numpy as np
from FADiff import *


def sin(x):
    '''
    Returns the sine of...

        Parameters:
            x: float, Scal, Vect

        Returns:
            new Scal instance or sine of x
    '''
    try:
        der = {}
        for var in x._der.keys():
            der[var] = x._der.get(var) * np.cos(x._val)
        parents = x.set_parents(x)
        return Scal(np.sin(x._val), der, parents)
    except AttributeError:
        return np.sin(x)

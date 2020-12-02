#!/usr/bin/env python3

import numpy as np
from FADiff import *


def sin(x):
    try:
        der = {}
        for var in x._der.keys():
            der[var] = x.partial_der(var) * np.cos(x._val)
        parents = x.set_parents(x)
        return Scalar(np.sin(x._val), der, parents)
    except AttributeError:
        return np.sin(x)

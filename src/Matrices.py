#!/usr/bin/env python3

import numpy as np
from Gradients import Scal_Func


class Vector:
    def __init__(self, vector, der=None):
        self._val = np.array(vector)
        self._der = der * np.identity(len(vector))

    def compute_jacobian(self):
        pass
    
#!/usr/bin/env python3

# NOTE: See bottom of this module for imported modules

class FADiff:
    vars_list = []        # Global vars list (Jacobian includes all)
    vectors_list = []

    # TODO: Should we also handle for list inputs?

    @staticmethod
    def new_scal(val, der=None, name=None):
        if not der:         # No der arg?
            der = 1         # Init der to 1
        return ScalFunc(val, der=der, name=name, new_input=True)

    @staticmethod
    def new_vec(vector, der=None, name=None):
        if not der:         # No der arg?
            der = 1         # Init der to 1
        return Vector(vector, der=der, name=name, new_input=True)

    # TODO: More API(?) stuff?
    #  - Jacobian?


# NOTE: Imports intentionally at bottom to prevent circular dependencies
from Gradients import ScalFunc
from Matrices import Vector

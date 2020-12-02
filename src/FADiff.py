#!/usr/bin/env python3

# NOTE: See bottom of this module for imported modules

class FADiff:
    vars_list = []        # Global vars list (Jacobian includes all)

    @staticmethod
    def new_var(val, der=None, name=None):
        # TODO: Should we also handle for list inputs?
        if not der:         # No der arg?
            der = 1         # Init der to 1
        return Scalar(val, der=der, name=name, new_input=True)

    @staticmethod
    def new_vector(vector, der=None, name=None):
    # TODO: Should we also handle for list inputs?
        if not der:         # No der arg?
            der = 1         # Init der to 1
        return Vector(val, der=der, name=name, new_input=True)

    # TODO: More API(?) stuff?
    #  - Jacobian


# NOTE: Imports intentionally at bottom to prevent circular dependencies
from Scalars import Scalar
from Matrices import Vector

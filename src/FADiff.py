#!/usr/bin/env python3

# NOTE: See bottom of this module for imported modules

class FADiff:
    scal_inputs = []        # Global input scalar vars list
    vect_inputs = []        # Global input vector vars list

    # TODO: If time, also handle for list inputs?

    @staticmethod
    def new_scal(val, der=None, name=None):
        if not der:         # No der arg?
            der = 1         # Init der to 1
        return Scal(val, der=der, name=name, new_input=True)

    @staticmethod
    def new_vect(vect, der=None, name=None):
        if not der:         # No der arg?
            der = 1         # Init der to identity matrix
        return Vect(vect, der=der, name=name, new_input=True)

    # TODO
    @staticmethod
    def new_funcvect():
        pass

    # TODO: Make sure to specify in doc how user can get Jacobians, etc.


# NOTE: Imports intentionally at bottom to prevent circular dependencies
from Gradients import Scal
from Matrices import Vect


# References:
# - https://www.programiz.com/python-programming/docstrings

#!/usr/bin/env python3

# NOTE: See bottom of this module for imported modules

class FADiff:
    scal_inputs = []        # Global input scalar vars list
    vect_inputs = []        # Global input vector vars list
    mode = 'forward'        # Default mode is forward mode

    @staticmethod
    def set_mode(mode):
        # TODO: Input validation necessary here?
        FADiff.mode = mode.lower()

    @staticmethod
    def new_scal(val, der=None, name=None):
        if not der:         # No der arg?
            der = 1         # Init der to 1
        if FADiff.mode == 'forward':
            return fadScal(val, der=der, name=name, new_input=True)

    @staticmethod
    def new_vect(vect, der=None, name=None):
        if not der:         # No der arg?
            der = 1         # Init der to identity matrix
        if FADiff.mode == 'forward':
            return fadVect(vect, der=der, name=name, new_input=True)

    @staticmethod
    def new_funcvect(func_list):
        if FADiff.mode == 'forward':
            return fadFuncVect(func_list)


# NOTE: Imports intentionally at bottom to prevent circular dependencies
from fad.Gradients import Scal as fadScal
from fad.Matrices import Vect as fadVect
from fad.FuncVect import FuncVect as fadFuncVect


# References:
# - https://www.programiz.com/python-programming/docstrings

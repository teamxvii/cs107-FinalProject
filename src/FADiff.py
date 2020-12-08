#!/usr/bin/env python3
import numpy as np
# NOTE: See bottom of this module for imported modules

class FADiff:
    _fadscal_inputs = []        # Global input scalar vars list
    _fadvect_inputs = []        # Global input vector vars list
    _revscal_inputs = []
    _mode = 'forward'           # Default mode is forward mode

    @staticmethod
    def set_mode(mode):
        # TODO: Input validation necessary here?
        FADiff._mode = mode.lower()

    @staticmethod
    def new_scal(val, der=None, name=None):
        if not der:  # No der arg?
            der = 1  # Init der to 1
        if FADiff._mode == 'forward':
            return _fadScal(val, der=der, name=name, new_input=True)
        elif FADiff._mode == 'reverse':
            return _revScal(val, der=der, name=name, new_input=True)

    @staticmethod
    def new_vect(vect, der=None, name=None):
        if FADiff._mode == 'forward':
            if not der:  # No der arg?
                der = np.ones(vect.shape)  # Init der to identity matrix
            return _fadVect(vect, der=der, name=name, new_input=True)
        elif FADiff._mode == 'reverse':
            return _revVect()

    @staticmethod
    def new_funcvect(func_list):
        return _funcVect(func_list)


# NOTE: Imports intentionally at bottom to prevent circular dependencies
from fad.Gradients import Scal as _fadScal
from fad.Matrices import Vect as _fadVect
from FuncVect import FuncVect as _funcVect
from rev.Gradients import Scal as _revScal
from rev.Matrices import Vect as _revVect


# References:
# - https://www.programiz.com/python-programming/docstrings

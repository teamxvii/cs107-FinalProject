#!/usr/bin/env python3
import numpy as np
# NOTE: See bottom of this module for imported modules


class FADiff:
    _fadscal_inputs = []        # Global input scalar vars list, forward mode
    _fadvect_inputs = []        # Global input vector vars list, forward mode
    _revscal_inputs = []        # Global input vector vars list, reverse mode
    _revvect_inputs = []        # Global input vector vars list, reverse mode
    _mode = 'forward'           # Default mode is forward mode

    @staticmethod
    def set_mode(mode):
        if mode.lower() == 'forward' or mode.lower() == 'reverse':
            FADiff._mode = mode.lower()

    @staticmethod
    def new_scal(val, der=None, name=None):
        if FADiff._mode == 'forward':
            if not der:  # No der arg?
                der = 1  # Init der to 1
            return _fadScal(val, der=der, name=name, new_input=True)
        elif FADiff._mode == 'reverse':
            return _revScal(val, name=name, new_input=True)

    @staticmethod
    def new_vect(vect, der=None, name=None):
        if FADiff._mode == 'forward':
            vect = np.array(vect)# TODO: Keep this?
            if not der:  # No der arg?
                der = np.ones(vect.shape)  # Init der to identity matrix
            return _fadVect(vect, der=der, name=name, new_input=True)
        elif FADiff._mode == 'reverse':
            if not der:  # No der arg?
                pass  # TODO: Need to change?
            return _revVect(vect, name=name, new_input=True)

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

#!/usr/bin/env python3

from FADiff import FADiff
from fad.Gradients import Scal as fadScal
from rev.Gradients import Scal as revScal


class FuncVect:
    def __init__(self, funcs):
        try:                                   # All fxns all Scal xor all Vect?
            func_type = type(funcs[0])         # Check the first element
            for func in funcs[1:]:
                if type(func) != func_type:    # Check for consistency
                    raise Exception('All functions must be of same type (Scalar '
                                    'or Vector).')
        except Exception:
            raise
        else:
            # Set inputs list based on type (Scal or Vect) of functions
            if func_type is fadScal:
                inputs = FADiff._fadscal_inputs
            else:
                inputs = FADiff._fadvect_inputs
            self._f_vect = funcs   # List of objects (Scal or Vect) used in fxns
            self._input_vars = []  # Get complete list of input vars of f_vect
            for func in funcs:
                if func._parents:
                    for var in func._der.keys():
                        if var in func._parents:
                            self._input_vars.append(var)
                elif func in inputs:   # TODO: Input var (identity fxn) is correct? Make sure to test
                    self._input_vars.append(func)
            self._input_vars = list(set(self._input_vars))

    @property
    def val(self):
        func_vals = []
        for func in self._f_vect:
            func_vals.append(func._val)
        return func_vals

    @property
    def der(self):
        funcs_parents = []
        for func in self._f_vect:
            parents = []
            for var, part_der in func._der.items():
                if var in self._input_vars:
                    parents.append(part_der)
            funcs_parents.append(parents)
        return funcs_parents  # TODO: Return correct?

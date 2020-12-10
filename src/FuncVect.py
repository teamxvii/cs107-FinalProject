#!/usr/bin/env python3

from FADiff import FADiff
from fad.Gradients import Scal as fadScal
from rev.Gradients import Scal as revScal
import numpy as np


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
                if func._parents:  # Has parents?
                    for var in func._der.keys():  # Loop through existing roots
                        if var in func._parents:  # If var is in parent/root list
                            self._input_vars.append(var)
                elif func in inputs:  # Otherwise input var, i.e., f(x) = x?
                    self._input_vars.append(func)
            self._input_vars = list(set(self._input_vars))

    @property
    def val(self):
        func_vals = []
        for func in self._f_vect:   # For each fxn, add its value to list
            func_vals.append(func._val)
        return np.array(func_vals)  # Return list

    @property
    def der(self):
        all_fxns_jacobs = []
        for func in self._f_vect:
            one_fxn_jacob = []
            for var, part_der in func._der.items():
                if var in self._input_vars:
                    one_fxn_jacob.append(part_der)
            all_fxns_jacobs.append(one_fxn_jacob)
        return np.array(all_fxns_jacobs)

#!/usr/bin/env python3

from FADiff import FADiff
from fad.Gradients import Scal as fadScal
from rev.Gradients import Scal as revScal


class FuncVect:
    def __init__(self, funcs):
        # check that all functions in vector are of same type (either all Scal or all Vect)
        try:
            func_type = type(funcs[0]) # check the first element
            for func in funcs[1:]:
                if type(func) != func_type:        # Check for consistency
                    raise Exception('All functions must be of same type (Scalar or Vector).')
        except Exception:
            raise
        
        # set inputs list based on type of functions
        if scalar:
            inputs = FADiff._fadscal_inputs
        else:
            inputs = FADiff._fadvect_inputs
        
        # create list of variables (either Scal or Vect objects) that are used in functions 
        self._f_vect = funcs
        self._input_vars = []     # Get complete list of input vars of f_vect
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

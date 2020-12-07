#!/usr/bin/env python3

from FADiff import FADiff
from fad.Gradients import Scal as fadScal
from rev.Gradients import Scal as revScal


class FuncVect:
    def __init__(self, funcs):
        try:
            for func in funcs:
                if type(func) != fadScal:        # Don't accept non-Scals
                    raise Exception('Invalid function type entered')
        except Exception:
            raise
        else:
            self._f_vect = funcs
            self._input_vars = []     # Get complete list of input vars of f_vect
            for func in funcs:
                if func._parents:
                    for var in func._der.keys():
                        if var in func._parents:
                            self._input_vars.append(var)
                elif func in FADiff._fadscal_inputs:   # TODO: Input var (identity fxn) is correct? Make sure to test
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

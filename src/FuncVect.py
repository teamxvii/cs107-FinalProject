#!/usr/bin/env python3

from FADiff import FADiff
from Gradients import Scal


class FuncVect:
    def __init__(self, funcs):
        try:
            for func in funcs:
                if type(func) != Scal:             # Don't accept non-Scals
                    raise Exception('Invalid function type entered')
                if func in FADiff.scal_inputs:     # No scal input variables
                    raise Exception('Invalid function type entered')
        except Exception:
            raise
        else:
            self.f_vect = funcs
            self.input_vars = []     # Get complete list of input vars of f_vect
            for func in funcs:
                for key in func._der.keys():
                    if key in func.parents:
                        self.input_vars.append(key)
            self.input_vars = list(set(self.input_vars))

    @property
    def val(self):
        func_vals = []
        for func in self.f_vect:
            func_vals.append(func._val)
        return func_vals

    @property
    def der(self):
        pass

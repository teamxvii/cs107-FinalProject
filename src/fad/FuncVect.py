#!/usr/bin/env python3

from FADiff import FADiff
from Gradients import Scal


class FuncVect:
    def __init__(self, funcs):
        try:
            for func in funcs:
                if type(func) != Scal:        # Don't accept non-Scals
                    raise Exception('Invalid function type entered')
        except Exception:
            raise
        else:
            self.f_vect = funcs
            self.input_vars = []     # Get complete list of input vars of f_vect
            for func in funcs:
                if func.parents:
                    for var in func._der.keys():
                        if var in func.parents:
                            self.input_vars.append(var)
                elif func in FADiff.scal_inputs:   # TODO: Input var (identity fxn) is correct? Make sure to test
                    self.input_vars.append(func)
            self.input_vars = list(set(self.input_vars))

    @property
    def val(self):
        func_vals = []
        for func in self.f_vect:
            func_vals.append(func._val)
        return func_vals

    @property
    def der(self):
        funcs_parents = []
        for func in self.f_vect:
            parents = []
            for var, part_der in func._der.items():
                if var in self.input_vars:
                    parents.append(part_der)
            funcs_parents.append(parents)
        return funcs_parents  # TODO: Return correct?

#!/usr/bin/env python3

from FADiff import FADiff
from Gradients import Scal


class FuncVect:
    def __init__(self, funcs):
        try:
            for func in funcs:
                # TODO: Correctly validating? --
                # Don't accept non-Scals
                if type(func) != Scal:
                    raise Exception('Invalid function type entered')
                # Don't accept Scals that are input variables
                if func in FADiff.scal_inputs:
                    raise Exception('Invalid function type entered')

        except Exception:
            raise
        else:
            self.f_vect = funcs

            # TODO: Keep track of what input variables each function uses (can use set())
            self.inputs = []

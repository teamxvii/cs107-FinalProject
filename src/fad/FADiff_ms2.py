#!/usr/bin/env python3
import numpy as np

class FADiff():
    def __init__(self, value, deriv):
        self.val = value
        self.der = deriv

    def __add__(self, other):
        try:
            return FADiff(self.val + other.val, self.der)
        except AttributeError:
            try:
                return FADiff(self.val + other, self.der)
            except:
                pass

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        try:
            return FADiff(self.val - other.val, self.der)
        except AttributeError:
            try:
                return FADiff(self.val - other, self.der)
            except:
                pass

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        try:
            return FADiff(self.val*other.val, self.val*other.der + self.der*other.val)
        except AttributeError:
            try:
                return FADiff(self.val*other, self.der*other)
            except:
                pass

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        try:
            return FADiff(self.val/other.val, (self.der*other.val - self.val*other.der)/self.other**2)
        except AttributeError:
            try:
                return FADiff(self.val/other, self.der/other)
            except:
                pass
        
    def __rdiv__(self, other):
        return self.__div__(other)    

    def __pow__(self, other):
        try:
            return FADiff(self.val**other.val, self.der*other.val*self.val**(other.val-1.))
        except AttributeError:
            try:
                return FADiff(self.val**other, self.der*other*self.val**(other-1.))
            except:
                pass

    def __rpow__(self, other):
        try:
            return FADiff(other.val**self.val, np.log(other.val)*self.der*other.val**self.val)
        except AttributeError:
            try:
                return FADiff(other**self.val, np.log(other)*self.der*other**self.val)
            except:
                pass

    def __neg__(self):
        return self.__mul__(-1.)

    def exp(self):
        return FADiff(np.exp(self.val), np.exp(self.val) * self.der)
    
    
    def sin(self):
        return FADiff(np.sin(self.val), np.cos(self.val) * self.der)

    def cos(self):
        return FADiff(np.cos(self.val), - np.sin(self.val) * self.der)

    def tan(self):
        return FADiff(np.tan(self.val), (1 / np.cos(self.val) ** 2) * self.der)
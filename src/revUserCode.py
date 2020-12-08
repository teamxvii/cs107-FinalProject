#!/usr/bin/env python3

from FADiff import FADiff as ad    # User needs to import
import Elems as ef                 # User needs to import
import numpy as np


# TODO: Debugging, etc. --
print(f'---- DEMOS / DEBUGGING / VERIFY CALCULATIONS ----\n')

ad.set_mode('reverse')         # Set the mode to reverse

# TODO:
#  - Test/demo der (no underscore)

print('Create input vars -->')
print(f'x = FADiff.new_scal(2)')
x = ad.new_scal(2, name='x')
print(f'y = FADiff.new_scal(5)')
y = ad.new_scal(5, name='y')
print(f'z = FADiff.new_scal(3)')
z = ad.new_scal(3, name='z')
print(x.val)
print(x.der)
print(y.val)
print(y.der)
print(z.val)
print(z.der)

# TODO: Debugging
q = ad.new_scal(6)

print()
print('f = x + y + z')
f = x + y + z
print('f.val -->')
print(f.val)
print('f.der -->')
print(f.der)
# print()
# print('f = x * y')
# f = x * y
# print('f.val -->')
# print(f.val)
# print('f.der -->')
# print(f.der)

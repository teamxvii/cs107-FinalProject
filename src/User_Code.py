#!/usr/bin/env python3

from FADiff import FADiff as fd
import Elems as ef


# TODO: Debugging, etc. --
print(f'---- DEMOS / DEBUGGING / VERIFY CALCULATIONS ----\n')

print('Create input vars -->')       # Create input vars
print(f'x = FADiff.new_scalar(2)')
x = fd.new_var(2, name='x')             # x = 2
print(f'y = FADiff.new_scalar(5)')
y = fd.new_var(5, name='y')             # y = 5
print(f'z = FADiff.new_scalar(3)')
z = fd.new_var(3, name='z')             # z = 3

print(f'x.val -->\n'                   
      f'{x.val}')              # Should be 2
print(f'x.der -->\n'           
      f'{x.der}')
print(f'y.val -->\n'                  
      f'{y.val}')              # Should be 5
print(f'y.der -->\n'
      f'{y.der}')
print(f'z.val -->\n'                  
      f'{z.val}')              # Should be 3
print(f'z.der -->\n'
      f'{z.der}')

print()

print(f'check = x * y + ef.sin(x)')
check = x * y + ef.sin(x)

print(f'check.val -->\n'
      f'{check.val}')                    # Should be 10.909...
print(f'check.der -->\n'
      f'{check.der}')                    # Should be [4.583, 2]
print(f'check.partial_der(x) -->\n'
      f'{check.partial_der(x)}')         # Should be 4.583...
print(f'check.partial_der(y) -->\n'  
      f'{check.partial_der(y)}')         # Should be 2

print(f'check = ef.sin(x + y)')
check = ef.sin(x + y)

print(f'check.val -->\n' 
      f'{check.val}')                    # Should be 0.656...
print(f'check.der -->\n'
      f'{check.der}')
print(f'check.partial_der(x) -->\n'
      f'{check.partial_der(x)}')         # Should be 0.753...
print(f'check.partial_der(y) -->\n'
      f'{check.partial_der(y)}')         # Should be 0.753...

print(f'check = ef.sin(x * y)')
check = ef.sin(x * y)

print(f'check.val -->\n'
      f'{check.val}')                    # Should be -0.544..
print(f'check.der -->\n'
      f'{check.der}')
print(f'check.partial_der(x) -->\n'
      f'{check.partial_der(x)}')         # Should be -4.195...
print(f'check.partial_der(y) -->\n'
      f'{check.partial_der(y)}')         # Should be -1.678...

print(f'check = 8 * x')
check = 8 * x

print(f'check.val -->\n'
      f'{check.val}')                    # Should be 16
print(f'check.der -->\n'
      f'{check.der}')
print(f'check.partial_der(x) -->\n'
      f'{check.partial_der(x)}')         # Should be 8

print(f'check = 8 * y')
check = 8 * y

print(f'check.val -->\n'
      f'{check.val}')                    # Should be 40
print(f'check.der -->\n'
      f'{check.der}')
print(f'check.partial_der(y) -->\n'
      f'{check.partial_der(y)}')         # Should be 8

print(f'check = 8 + x')
check = 8 + x

print(f'check.val -->\n'
      f'{check.val}')                    # Should be 10
print(f'check.der -->\n'
      f'{check.der}')
print(f'check.partial_der(x) -->\n'
      f'{check.partial_der(x)}')         # Should be 1

print(f'check = 8 + y')
check = 8 + y

print(f'check.val -->\n'
      f'{check.val}')                    # Should be 13
print(f'check.der -->\n'
      f'{check.der}')
print(f'check.partial_der(y) -->\n'
      f'{check.partial_der(y)}')         # Should be 1

print(f'check = x * y + ef.sin(x) + z')  # * Check using all three input vars *
check = x * y + ef.sin(x) + z

print(f'check.val -->\n'
      f'{check.val}')                    # Should be 13.909...
print(f'check.der -->\n'
      f'{check.der}')
print(f'check.partial_der(x) -->\n'
      f'{check.partial_der(x)}')         # Should be 4.583...
print(f'check.partial_der(y) -->\n'  
      f'{check.partial_der(y)}')         # Should be 2
print(f'check.partial_der(z) -->\n'  
      f'{check.partial_der(z)}')         # Should be 1

print(f'check = 7 * x + 6')
x1 = fd.new_var(2)
x2 = fd.new_var(3)
check = x1 * x2 + x1

print(f'check.val -->\n'
      f'{check.val}')
print(f'check.der -->\n'
      f'{check.der}')

# TODO: VECTOR DEBUGGING --

# i = x * y + ef.sin(x) + z
# j = x * y
#
# print('check = i + j')
# check = i + j
# print(f'check.val -->\n'
#       f'{check.val}')
# print(f'check.der -->\n'
#       f'{check.der}')
# print(f'check.partial_der(x) -->\n'
#       f'{check.partial_der(x)}')
# print(f'check.partial_der(y) -->\n'
#       f'{check.partial_der(y)}')
# print(f'check.partial_der(z) -->\n'
#       f'{check.partial_der(z)}')

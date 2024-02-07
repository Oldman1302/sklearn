# some basic ex of array creation
import numpy as np


print('1. Just creation')
arr1 = np.array([
    [1, 2],
    [3, 4]])
print(arr1, '\n')

print('2. Copies')
arr2 = arr1.copy()
print(arr2, '\n')
arr2[0][0] = 99
print(arr1, '\n')
# '-> so we can see that it is a deepcopy. For a not deepcopy you should write arr2 = arr1'

print('3. Zero array')
# 2nd parameter is the type of array's elements (for instance complex)
zeros = np.zeros((2, 3))
print(zeros, '\n')
# for array with only 1 use np.ones()

print('4. Zero array with some special size (like another array has)')
zeros2 = np.zeros_like(arr1)
print(zeros2, '\n')
# for array with only 1 use np.ones_like()

print('5. Unit array')
# A unit matrix is a square matrix in which all elements on the
# diagonal have a value of 1 and all others have a value of 0
uMatrix = np.eye(3)
print(uMatrix, '\n')

print('6. Building an array from one number to another with some step')
# Also if you have mistaken (for example incorrect order from 0 to -1 with step 0.1)
# it won't be shown the mistake but just empty array
# Additionally by default from = 0 and step = 1, so you can use only one or two parameters
array = np.arange(0, 1, 0.1)
print(array, '\n')

print('7. Redefine array')
# The extra 0's can be appeared because some numbers, such as
# 0.1, cannot be represented accurately in a computer in
# floating-point binary, resulting in small rounding errors in arithmetic operations.
str_array = array.astype('str')
print(str_array, '\n')

print('8. All available types')
for k, t in np.sctypes.items():
    print(f"{k}: {t}")
print()
# numpy.void is used to more versatile and flexible types,
# and refers to data types that do not necessarily fall into any of these predefined data types.
# Produce data in hex encoding

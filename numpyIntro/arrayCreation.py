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
zeros = np.zeros((2, 3))
print(zeros, '\n')
# for array with only 1 use np.ones()

print('4. Zero array with some splecial size (like another array has)')
zeros2 = np.zeros_like(arr1)
print(zeros2, '\n')
# for array with only 1 use np.ones_like()

print('5. Unit array')
# A unit matrix is a square matrix in which all elements on the
# diagonal have a value of 1 and all others have a value of 0
uMatrix = np.eye(3)
print(uMatrix)

import numpy as np

arr = np.arange(12).reshape(3, -1)
print('Array\n', arr)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''

# weird method which duplicates every element from array and redefine it to 1D array
# (from what we take elements, how many duplicates)
duplicates = np.repeat(arr, 2)
print('\n1. Using np.repeat\n', duplicates)  # [ 0  0  1  1  2  2  3  3  4  4  5  5  6  6  7  7  8  8  9  9 10 10 11 11]


s = np.stack((arr, arr))
# merges two arrays into one subarray
print('\n\n2. Using np.stack\n', s)
'''
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]]
'''
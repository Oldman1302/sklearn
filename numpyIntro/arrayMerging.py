import numpy as np

# Merged arrays has to have the same number of axis
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.arange(-10, 0).reshape(2, -1)

print('Array 1\n', arr1, '\n') # [[0 1 2 3 4] [5 6 7 8 9]]
print('Array 2\n', arr2, '\n') # [[-10  -9  -8  -7  -6] [ -5  -4  -3  -2  -1]]

print('1. Join arrays (make them sub-arrays of the new object and organize along the new axis)')
arr12 = np.stack((arr2, arr1))
print(arr12, '\n')
'''
[[ 1  2  3  4  5  6  7  8  9]
 [-9 -8 -7 -6 -5 -4 -3 -2 -1]]
'''
# In this case joined arrays must have the same size
print('2. Merge relatively to the existing axis')
concate_array = np.concatenate((arr1, arr2), 1)
print(concate_array, '\n')
'''
[[  0   1   2   3   4 -10  -9  -8  -7  -6]
 [  5   6   7   8   9  -5  -4  -3  -2  -1]]
'''

# vstack is concatenation along the first axis after 1-D arrays of shape (N,) have been reshaped to (1,N)

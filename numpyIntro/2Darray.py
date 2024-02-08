# here are some interesting 2D+ numpy arrays features
import numpy as np

arr2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print('Basement\n', arr2)
'''
out:
[[1 2 3 4]
[5 6 7 8]]
'''
# but if you want to output it on 1 line you need to use *
print('\nOutput it on 1 line', *arr2)
'''
out:
[1 2 3 4] [5 6 7 8]
'''

print('\nGet dimensionality(number of axis) of array')
print(arr2.ndim)

print('\nObtain the size of all elements in array')
print(arr2[0].size)
# also count all internal elements (if you write arr2.size output is 8)

print('\nObrain the define size relatively every axis of array')
print(arr2.shape)

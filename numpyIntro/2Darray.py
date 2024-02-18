# here are some interesting 2D+ numpy arrays features
import numpy as np

arr2 = np.array([[10, 2, 3, 4],
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
print(arr2.ndim)  # 2

print('\nObtain the size of all elements in array')
print(arr2[0].size)  # 4
# also count all internal elements (if you write arr2.size output is 8)

print('\nObtain the define size relatively every axis of array')
print(arr2.shape)  # (2, 4)

print('\nObtain the minimum number relatively to every row of array')
#            array    relatively to which axis (1 means it will find minimum in every subarray with index [: i]
print(np.min(arr2, 1))  # [2 5]

# !!! Find differences between average and mean
print('\nObtain the  number relatively to every column of array')
print(np.mean(arr2, 0))  # [7.5 4.  5.  6. ]

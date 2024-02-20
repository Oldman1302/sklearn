# here are some interesting 2D+ numpy arrays features
import numpy as np

arr2 = np.array([[10, 2, 3, 4],
                 [5, 6, 7, 8]])
print('Basement\n', arr2)
'''
out:
[[10 2 3 4]
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
# if you want to get index of minimum number you can use arr2.argmin but this method
# uses 1D array if you don't change parameter axis

# small example with 3D array to show aggregators functionality
arr3 = np.arange(8).reshape(2, 2, -1)
print('3D Array\n', arr3)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
print('Obtain the sum of numbers relatively some axis (more than 1)')
print(np.sum(arr3, (0, 2)))  # [10 18]

print('\nMake a mask on our array')
mask_array = np.ma.masked_greater(arr2, 5)
print(mask_array)

print('\nObtain the  average result relatively to every column of array')
print(np.mean(arr2, 0))  # [7.5 4.  5.  6. ]
# On a first view, it seems np.mean and np. average are identical
# But there are some critical differences
# 1. If you make a mask numpy.average doesn't figure out it and count all elements anyway
# 2. np.average has such parameter as weights for all elements:
print('\nObtain the  average result relatively to every column of array and weights')
print(np.average(arr2, 0, weights=np.array([0.1, 0.9])))  # [5.5 5.6 6.6 7.6]
# np.mean doesn't have this kind of parameter

print('\nAlso you can use arr.aggregator instead of np.aggregator(arr)')
print('arr2.min\n', arr2.min())

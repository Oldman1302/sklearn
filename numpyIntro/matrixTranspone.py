import numpy as np
# transposition - row and column interchange
arr = np.arange(24).reshape(4, 3, -1)

print(f'Array\n{arr}\n\n')

print('1. Create one-dimensional array')
arr_1d = arr.ravel()
print(arr_1d, '\n')  # [0 1 2 3 4 5 ... 23]

print('2. Array transposition through .T (row and column interchange)')
t_arr = arr.T
print(t_arr, '\n')
'''
[[[ 0  6 12 18]
  [ 2  8 14 20]
  [ 4 10 16 22]]

 [[ 1  7 13 19]
  [ 3  9 15 21]
  [ 5 11 17 23]]] 
'''

# arr.T has another more profitable functional
# you can define different orders of transposition
print('3. Array transposition through .transpose (row and column interchange)')
transposition_arr = np.transpose(arr, (0, 2, 1))
print(transposition_arr, '\n')  # [1 4] [2 5] [3 6]
'''
[[[ 0  2  4]
  [ 1  3  5]]

 [[ 6  8 10]
  [ 7  9 11]]

 [[12 14 16]
  [13 15 17]]

 [[18 20 22]
  [19 21 23]]]
'''

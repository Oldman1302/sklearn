import numpy as np

# the creation of basic array
sample = np.arange(24)
print('Basement\n', sample, '\n')

print('1. Reshape the array to 2D array')
array_2d = sample.reshape(3, 8)
print(array_2d, '\n')
# Also you can reshape to more spaces (e.g. sample.reshape(2, 6, 2))
# * it isn't deepcopy => if you change sample/array_2d you modify another array as well

# you can reshape array to put -1 instead of 1 parameter, and it will be calculated automatically
print('2. Special feature for reshape')
array_2d = sample.reshape(4, -1)
print(array_2d, '\n')

print('3. Create one-dimensional array')
array_1d = array_2d.ravel()
print(array_1d, '\n')
# or use just reshape(-1)

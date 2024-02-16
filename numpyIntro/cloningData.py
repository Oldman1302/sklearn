import numpy as np

arr = np.arange(12).reshape(3, -1)

# silly method which duplicates every element from array and redefine it to 1D array
# (from what we take elements, how many duplicates)
duplicates = np.repeat(arr, 2)

print(duplicates)


s = np.stack((arr, arr))
t_s = np.transpose(s, (1, 0, 2))
print(s, '\n\n\n', (t_s))


# here are some interesting 2D+ numpy arrays features
import numpy as np


arr2 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print(arr2)
'''
out:
[[1 2 3 4]
[5 6 7 8]]
'''
# but if you want to output it on 1 line you need to use *
print('\n', *arr2)
'''
out:
[1 2 3 4] [5 6 7 8]
'''

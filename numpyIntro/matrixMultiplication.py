import numpy as np

A = np.array([[1., 3., 2.], [3, 6, 3]])
B = np.array([0., -2., -3.])

print('Array A\n', A)
print('\nArray B\n', B)

print('\n1. A * B\n', np.dot(A, B))  # [-12. -21.]

A = np.arange(6).reshape(2, 3)
B = np.arange(12, 0, -1).reshape(3, 4)
print('\n\n2. Matrix Multiplication\nArray A\n', A, '\nArray B\n', B)
res = np.dot(A, B)
print('\nResult\n', res, '\n\n')  # res[i, j] = Sum(sumA[i, :] * B[:, j])
'''
[[16 13 10  7]
 [88 76 64 52]]
'''
# if you have multidimensional array ,and you want to make multiplication according not standard axis
# use np.tensordot(A, B, [2, 1])
# * the dimensions of these axes must be identical

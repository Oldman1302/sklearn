import numpy as np

A = np.array([[1, 2, 10], [3, 11, 4]])
B = np.array([[-1, -2, 3], [-4, 111, 5]])

total = A + B
print("\n1. Sum of 2 arrays\n", total)  # by analogy such operations as - * / // % ** (but it works only with float64)
# if you want to round results you can use # np.round
'''
[[  0   0  13]
 [ -1 122   9]]
'''

C = np.array([-1, -2, -10])
print("\n2. Sum of 2 different sized arrays\n", A + C)
# by analogy such operations as - * / // % ** (but it works only with float64)
'''
[[ 0  0  0]
 [ 2  9 -6]]
'''

total_plus1 = total + 1
print("\n3. Sum of array and number\n", total_plus1)  # you can use as many operators as you want
'''
[[  1   1  14]
 [  0 123  10]]
'''

exp_array = np.exp(A)
print("\n4. e^A[i]\n", exp_array)
'''
[[3.0000e+00 7.0000e+00 2.2026e+04]
 [2.0000e+01 5.9874e+04 5.5000e+01]]
'''

log_array = np.log(A)
print("\n5. lnA\n", log_array)
'''
[[0.         0.69314718 2.30258509]
 [1.09861229 2.39789527 1.38629436]]
'''

cos_array = np.cos(A)  # if you want to use degrees instead of radians just use np.degrees
# the same way with other trigonometric functions
print("\n6. cosA\n", cos_array)
'''
[[ 0.54030231 -0.41614684 -0.83907153]
 [-0.9899925   0.0044257  -0.65364362]]
'''

# documentations with all math operations: https://numpy.org/doc/stable/reference/routines.math.html

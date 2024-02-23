# this code creates 3 sigmoids with different alpha
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(alpha) -> np.array:
    return 1 / (1 + np.exp(- alpha * x))


# it creates an array with 100 nums from -5 to 5 evenly distributed
x = np.linspace(-5, 5, 100)

plt.title('y = 1/(1 + e^(- alpha * x))')
plt.xlabel('x')
plt.ylabel('y')  # axis
plt.grid(True)

for i in range(3):
    A = float(input(f'{i + 1}. Input alpha: '))
    graph = plt.plot(x, sigmoid(A), label=f'1/(1 + e^(- {A} * x))')

plt.legend()

plt.show()

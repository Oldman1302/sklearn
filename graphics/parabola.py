import matplotlib.pyplot as plt
import numpy as np

print('y = ax^2 + bx c')

a = float(input(f'Input a: '))
b = float(input(f'Input b: '))
c = float(input(f'Input c: '))

# it creates an array with 100 nums from -5 to 5 evenly distributed
x = np.linspace(-b / (2 * a) - 10, -b / (2 * a) + 10, 100)

plt.title(f'y = {a}x^2 + {b}x + {c}')
plt.xlabel('x')
plt.ylabel('y')  # axis
plt.grid(True)

y = plt.plot(x, x**2 * a + b * x + c)

plt.show()

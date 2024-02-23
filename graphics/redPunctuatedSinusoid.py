import matplotlib.pyplot as plt
import numpy as np

print('y = asin(bx) + c')

a = float(input(f'Input a: '))
b = float(input(f'Input b: '))
c = float(input(f'Input c: '))

# it creates an array with 100 nums from -5 to 5 evenly distributed
x = np.linspace(-8, 8, 100)

plt.title(f'y = {a}sin({b}x + {c}')
plt.xlabel('x')
plt.ylabel('y')  # axis
plt.grid(True)

y = plt.plot(x, a * np.sin(b * x) + c, 'r--')  # 'r-' - means red color, '-' means dashed lines

plt.show()

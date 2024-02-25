import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 400)

plt.plot(x, (4 - x**2)**0.5 + (x**2)**0.33, color='red')
plt.plot(x, -(4 - x**2)**0.5 + (x**2)**0.33, color='red')
plt.title('I love you!', fontsize=16)

plt.show()

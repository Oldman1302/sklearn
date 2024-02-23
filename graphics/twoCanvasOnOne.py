import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-10, 10, 100)
y1 = np.abs(x1)

x2 = np.linspace(-10, 10, 100)
y2 = x2

# 1
#      num of rows, columns, index
plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.axvline(0, color='black', linewidth=1)  # to create axis y through 0
plt.title('y = |x|')

# 2
plt.subplot(2, 1, 2)
plt.plot(x2, y2)
plt.title('y = x')

# automatically adjust the position of elements so that they do not overlap each other
plt.tight_layout()

plt.show()

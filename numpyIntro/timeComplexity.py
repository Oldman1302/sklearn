# here I just wanna create an array and do smth with it (for instance check the time complexity)
import numpy as np
import time
import random

# let's create np array of 100000 int numbers (1 <= num[i] <= 100) and record the time of creation
start = time.time()
numpy_arr = np.random.randint(1, 101, 100000)
end = time.time()
print('numpy time complexity:', end - start)

# and no we're creating list of 10000 int numbers (1 <= num[i] <= 100) and record the time of creation
start = time.time()
arr = [random.randint(1, 100) for x in range(10000)]
end = time.time()
print('basic list time complexity:', end - start)

# so we can see that even 100000 elements with numpy methods were created faster than 10k elements with basic methods

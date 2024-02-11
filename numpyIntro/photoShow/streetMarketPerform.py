import numpy as np
from matplotlib import pyplot as plt
import cv2

img = cv2.imread('streetmarket.jpeg')[:, :, ::-1]
# OpenCV is working with images in format BGR
print(img)
plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.imshow(img)
plt.show()

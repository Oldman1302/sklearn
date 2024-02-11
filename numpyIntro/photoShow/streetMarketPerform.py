import numpy as np
from matplotlib import pyplot as plt
import cv2

# OpenCV is working with images in format BGR => why I've reversed 3rd array in cv2.imread
img = cv2.imread('streetmarket.jpeg')[:, :, ::-1]

# figsize - windows size
# dpi - the resolution of the figure in dots-per-inch
# facecolor - background
# edgecolor - the border color.
plt.figure(figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.title('good quality')
plt.imshow(img)

# then I'm going to decrease the resolution of picture
# ! Поменяв форму массива, мы получили 2 новые оси, по 2 значения в каждой, им
# соответствуют кадры, составленные из нечетных и четных строк и столбцов исходного изображения
worse_img = img.reshape(img.shape[0] // 2, 2, img.shape[1] // 2, 2, -1)
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.title('bad quality')
plt.imshow(worse_img[:, 0, :, 0])
plt.show()

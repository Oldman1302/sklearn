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
worse_img = img.reshape(img.shape[0] // 2, 2, img.shape[1] // 2, 2, -1)[:, 0, :, 0]
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.title('bad quality')
plt.imshow(worse_img)

# now let's rotate the array by transpose
# could be done by np.swapaxes which swap two axes we added in parameters
t_img = np.transpose(img, (1, 0, 2))
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.title('transposition')
plt.imshow(t_img)

# then create duplicate of our picture with using np.vstack (vertically)
# vstack is concatenation along the first axis after 1-D arrays of shape (N,) have been reshaped to (1,N)
canvas = np.vstack((img, img))
plt.figure(num=None, figsize=(15, 15), dpi=80, facecolor='w', edgecolor='k')
plt.title('vertical merge')
plt.imshow(canvas)
# for merging pictures horizontally is used np.hstack (horizontally)
# * has to mentioned when you merge it's made like deepcopy
# -> you won't change arrays through other arrays (in parameters)

# instantly 1D array
# now it has only one axis -> has to be divided by axis
# it's stretch the picture on some axis
# ,or we could use np.stack + np.transpose
stretch_photo = np.repeat(worse_img, 2)
stretch_photo = stretch_photo.reshape(worse_img.shape[0], worse_img.shape[1], worse_img.shape[2], -1)
print(worse_img.shape)
print(stretch_photo.shape)
stretch_photo = np.transpose(stretch_photo, (0, 3, 1, 2))
print("\n!!!\n", stretch_photo.shape)
stretch_photo = stretch_photo.reshape(-1, worse_img.shape[1], worse_img.shape[2])
plt.figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.title('stretch')
plt.imshow(stretch_photo)

plt.show()

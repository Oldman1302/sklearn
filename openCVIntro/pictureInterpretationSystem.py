import cv2

# so img[i j], i - row, j - column. And this img[i j] is array with 3 elements (RGB interpretation)
# *if you don't put any new params
# But if you want to make your picture black and white just use param 0 (or cv2.IMREAD_GRAYSCALE)
img = cv2.imread('pxl.png', 0)
'''
first row of our picture
[[  0   0   0]
  [  0   0   0]
  [  0   0   0]
  [  0   0   0]
  [255 255 255]
  [255 255 255]
  [255 255 255]
  [255 255 255]
  [255 255 255]
  [255 255 255]
  [  0   0   0]
  [  0   0   0]
  [  0   0   0]
  [  0   0   0]
  [  0   0   0]
  [  0   0   0]]
  ...
'''
print(img)

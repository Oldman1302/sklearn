import cv2

img = cv2.imread('pxl.png')

cv2.namedWindow('Zoomed Image', cv2.WINDOW_NORMAL)
cv2.imshow('Zoomed Image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

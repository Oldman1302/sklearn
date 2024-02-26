import cv2
import numpy as np


def view_image(image):
    cv2.namedWindow('Display')
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# this code divides all code into 17 different levels
def grayscale_17_levels():
    high = 255
    while high >= 0:
        low = high - 15
        lower = np.array([low])
        higher = np.array([high])
        # cv2. inRange() finds from gray pixels which are brighter than lower and grayer than higher
        curr_mask = cv2.inRange(gray, lower, higher)
        gray[curr_mask > 0] = high
        high -= 15


img = cv2.imread('ombre.jpg')

view_image(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayscale_17_levels()
view_image(gray)

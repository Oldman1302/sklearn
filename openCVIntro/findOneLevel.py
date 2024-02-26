import cv2
import numpy as np


def view_image(image):
    cv2.namedWindow('Display')
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# this code divides all code into 17 different levels
def grayscale_17_levels():
    mask = cv2.inRange(gray, np.array([150]), np.array([165]))
    gray[mask > 0] = 255
    gray[mask == 0] = 0


img = cv2.imread('ombre.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayscale_17_levels()
view_image(gray)

# STOP HERE
import cv2
import numpy as np


def view_image(img):
    cv2.namedWindow('Display')
    cv2.imshow('Display', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def grayscale_17_levels(img):
    # important to do before ocunturization
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output = []
    high = 255
    low = high
    first = True

    while low > 0:
        low = high - 15
        if not first:
            lower = np.array([high])
            higher = np.array([255])
            # cv2. inRange() finds from gray pixels which are brighter than lower and grayer than higher
            curr_mask = cv2.inRange(image, lower, higher)
            image[curr_mask > 0] = 0
            print(img)
        # ret - minimum which was used for binarization (initially 240)
        ret, threshold = cv2.threshold(image, low, 255, 0)
        # list of contours and their hierarchy
        contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:
            output.append([cv2.contourArea(contours[0])])
            cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
            high -= 15
            first = False

    print(output)
    return img


image = cv2.imread('ombre.jpg')
image = grayscale_17_levels(image)
view_image(image)

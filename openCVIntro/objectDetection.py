import cv2
import numpy as np


def view_image(img):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def greatest_contour(ctrs: list) -> list:
    max_square = 0
    index = -1

    for i, ctr in enumerate(ctrs):
        # cv2.contourArea count the square of figure with this contour
        if cv2.contourArea(ctr) > max_square:
            max_square = cv2.contourArea(ctr)
            index = i

    return ctrs[index]


image = cv2.imread('leaf.jpeg')
# hsv - color model which is described on Hue (оттенка), Saturation (насыщенности) и Value (яркости)
# HSV representation is  important because it's easier to get full range of one color with it
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# all green is in range from [45, 100, 50] to [75, 255, 255]
# here we get full range of green color
green_low = np.array([45, 100, 50])
green_high = np.array([75, 255, 255])
curr_mask = cv2.inRange(hsv_image, green_low, green_high)
hsv_image[curr_mask > 0] = ([75, 255, 200])

# transform our result to black and white representation to make then the delineation (оконтурирование)
rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

# then we need to make from it black and white picture and get contours on a broad between these colors
ret, threshold = cv2.threshold(gray_image, 90, 255, 0)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# param № 3: indexes of all contours which we will use for our image (-1 means we use all contours)
# param № 4: contour color
# param № 5: contours width
# view_image(image)

# but now we have some inaccuracies in our delineation, so we have to find only the biggest contour and use it only
largest_contour = greatest_contour(contours)
cv2.drawContours(image, largest_contour, -1, (0, 0, 255), 4)
view_image(image)

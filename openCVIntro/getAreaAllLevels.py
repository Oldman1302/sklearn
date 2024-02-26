# STOP HERE
import cv2
import numpy as np


def view_image(image):
    cv2.namedWindow('Display')
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_area_of_each_gray_level(im):
    ## преобразование изображения к оттенкам серого (обязательно делается до оконтуривания)
    image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    output = []
    high = 255
    first = True
    while (1):
        low = high - 15
        if first == False:
            break
        # Делаем значения выше уровня серого чёрными. Так они не будут обнаруживаться
        to_be_black_again_low = np.array([high])
        to_be_black_again_high = np.array([255])
        curr_mask = cv2.inRange(image, to_be_black_again_low,
                                to_be_black_again_high)
        image[curr_mask > 0] = (0)

        # Делаем значения этого уровня белыми. Так мы рассчитаем их площадь
        ret, threshold = cv2.threshold(image, low, 255, 0)
        contours, hirerchy = cv2.findContours(threshold,
                                              cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        if (len(contours) > 0):
            output.append([cv2.contourArea(contours[0])])
            cv2.drawContours(im, contours, -1, (0, 0, 255), 3)
            high -= 15
            first = False
        if (low == 0):
            break
    return output


image = cv2.imread('ombre.jpg')
print(get_area_of_each_gray_level(image))
view_image(image)

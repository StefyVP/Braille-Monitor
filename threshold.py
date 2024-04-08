import cv2
import numpy
import string
import os
from PIL import Image
from find_images import braille_alphabet

i = 0

for char in string.ascii_lowercase:
    input_path = braille_alphabet[i]
    input_image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    output_path = braille_alphabet[i]

    height = input_image.shape[0]
    width = input_image.shape[1]

    if len(input_image.shape) == 2:
        gray_input_image = input_image.copy()
    else:
        gray_input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    upper_threshold, thresh_input_image = cv2.threshold(
        gray_input_image, thresh=0, maxval=255, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    lower_threshold = 0.5 * upper_threshold

    canny = cv2.Canny(input_image, lower_threshold, upper_threshold)
    pts = numpy.argwhere(canny > 0)

    y1, x1 = pts.min(axis=0)
    y2, x2 = pts.max(axis=0)

    output_image = input_image[y1:y2, x1:x2]

    cv2.imwrite(output_path, output_image)

    i = i + 1

    if os.path.exists(input_path):
        # os.remove(input_path)
        print("The file does exist")
    else:
        print("The file does not exist")

import cv2
import numpy as num
from PIL import Image
import os.path

img = cv2.imread('braille a_rembg.png')
cv2.imshow('Image', img)

image = Image.open('braille a_rembg.png')
width, height = image.size
total_pixels = width*height
print("width: ", width)
print("height: ", height)

count_white_pixels = num.sum(img != 0)
count_black_pixels = num.sum(img == 0)

print("Number of non black pixels: ", count_white_pixels) #3
print("Number of black pixels: ", count_black_pixels) #2760
print("Total pixels: ", total_pixels)


'''
img = cv2.imread('braille b_rembg.png')
cv2.imshow('Image', img)


count_nonblack_pixels = num.sum(img != 0)
count_black_pixels = num.sum(img == 0)

print("Number of white pixels: ", count_nonblack_pixels) #40936
print("Number of black pixels: ", count_black_pixels) #4425
'''
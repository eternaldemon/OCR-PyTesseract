# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 02:33:44 2020

@author: eternal_demon
"""

import cv2
import pytesseract


img = cv2.imread('test1.png', cv2.IMREAD_GRAYSCALE)

# configurations for PSM

# OSD -  Orientation and Script Detection.
# 0 = Orientation and script detection (OSD) only.
# 1 = Automatic page segmentation with OSD.
# 2 = Automatic page segmentation, but no OSD, or OCR
# 3 = Fully automatic page segmentation, but no OSD. (Default)
# 4 = Assume a single column of text of variable sizes.
# 5 = Assume a single uniform block of vertically aligned text.
# 6 = Assume a single uniform block of text.
# 7 = Treat the image as a single text line.
# 8 = Treat the image as a single word.
# 9 = Treat the image as a single word in a circle.
# 10 = Treat the image as a single character.


config = ('-l eng --oem 1 --psm 3')
# use img or thresh as input on the basis of what you want to use.
text = pytesseract.image_to_string(img, config=config) 
# print text
text = text.split('\n')
print(text)
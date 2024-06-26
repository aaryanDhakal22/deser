import cv2
from time import sleep
import pyautogui
from pyautogui import click
from CORDS import *

sleep(5)

# Login
click(CORD_PASSKEY)
sleep(0.5)
click(CORD_PASSKEY)
sleep(0.5)
click(CORD_ENTER)
sleep(0.5)
click(CORD_DISPATCH)
sleep(1)
# Take a screenshot of all of the deliveries : One picture mode
pyautogui.screenshot("all_delivs.jpg")
# Step 1: Read the image
image = cv2.imread("all_delivs.jpg")

# Step 2: Define the coordinates of the ROI
# (top-left x, top-left y, width, height)
# Step 3: Crop the ROI from the image
addr_cords = []
for i in range(5):
    x = 710
    y = 425
    l = 125
    b = 15
    addr_cords.append([y, y + l, x, x + b])

roi = image[425:440, 710:837]

# Step 4: Save or display the cropped image

cv2.imwrite("original.jpg", roi)  # Display the cropped image

# slice the picture between the cords
# take all the names
# Stringify them and save to list

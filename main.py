import cv2
from time import sleep
import pyautogui
from pyautogui import click
from CORDS import *
import numpy as np
import keyboard
import playsound

while True:
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

    pyautogui.moveTo(1282, 394)
    pyautogui.dragTo(1282, 890, 1, button="left")
    sleep(2)
    # for i in range(4):
    #     pyautogui.press("pagedown")
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

    roi = image[400:900, 605:628]

    # Step 4: Save or display the cropped image

    cv2.imwrite("original.jpg", roi)  # Display the cropped image

    # slice the picture between the cords
    # take all the names
    # Stringify them and save to list

    # Load the main image and template image
    template = cv2.imread("template_image.jpg")
    main_image = cv2.imread("original.jpg")
    # Convert both images to grayscale
    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Get the width and height of the template image
    w, h = template_gray.shape[::-1]

    # Perform template matching
    result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # Set a threshold to determine if a match is found
    threshold = 0.8
    locations = np.where(result >= threshold)

    # Print "found" if a match is found
    click(CORD_KEY)
    if len(locations[0]) > 0:
        print("Found")
        for i in range(3):
            playsound.playsound("bell.wav")
    sleep(120)

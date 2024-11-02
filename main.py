import cv2
from time import sleep
import pyautogui
from pyautogui import click
from CORDS import *
import numpy as np
import playsound
import pytesseract


def is_being_used():
    pyautogui.screenshot("check.jpg")
    check_img = cv2.imread("check.jpg")
    aoi = check_img[294:305, 548:595]
    gray = cv2.cvtColor(aoi, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    print(text)
    if text.strip():
        return True
    else:
        return False


while True:
    sleep(10)
    if is_being_used():
        print("Computer is being used")
        continue
    else:
        pass
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
    pyautogui.screenshot("all_delivs.jpg")
    image = cv2.imread("all_delivs.jpg")

    roi = image[400:900, 605:628]

    cv2.imwrite("original.jpg", roi)
    template = cv2.imread("template_image.jpg")
    main_image = cv2.imread("original.jpg")
    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    locations = np.where(result >= threshold)
    click(CORD_KEY)
    if len(locations[0]) > 0:
        print("Found")
        for i in range(3):
            playsound.playsound("bell.wav")

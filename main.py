import cv2
from time import sleep
import pyautogui
from pyautogui import click
from CORDS import *
import numpy as np
import playsound
import pytesseract
from notifier import *


def is_being_used():

    pyautogui.screenshot("images/check.jpg")
    check_img = cv2.imread("images/check.jpg")
    aoi = check_img[294:305, 548:595]
    gray = cv2.cvtColor(aoi, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    print(text)
    if text.strip():
        return True
    else:
        return False


def is_empty(image_path, threshold=240, tolerance=0.95):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is None
    if image is None:
        return False

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the proportion of pixels above the threshold
    white_pixel_ratio = np.mean(gray_image >= threshold)

    # Check if the proportion is greater than the tolerance
    return white_pixel_ratio >= tolerance


while True:
    sleep(4)
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

    pyautogui.screenshot("images/scrollbar.jpg", region=(1273, 364, 20, 20))
    if is_empty("images/scrollbar.jpg"):
        print("Deliveries less than 11")
    else:
        pyautogui.moveTo(1282, 394)
        pyautogui.dragTo(1282, 890, 1, button="left")
    sleep(2)
    pyautogui.screenshot("images/all_delivs.jpg")
    image = cv2.imread("images/all_delivs.jpg")

    roi = image[400:900, 605:628]

    cv2.imwrite("images/original.jpg", roi)
    template = cv2.imread("images/template_image.jpg")
    main_image = cv2.imread("images/original.jpg")
    main_gray = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    w, h = template_gray.shape[::-1]
    result = cv2.matchTemplate(main_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8
    locations = np.where(result >= threshold)

    if len(locations[0]) > 0:
        click([605, 400 + max_loc[1]])
        sleep(1)
        click(CORD_EDIT)
        sleep(2)
        click(CORD_EDIT_CUST)
        sleep(1)
        click(CORD_CONF_EDIT)
        sleep(1)
        pyautogui.screenshot("images/card.jpg", region=(514, 600, 311, 306))
        sleep(1)
        click(CORD_TEXT_AREA)
        sleep(0.5)
        click(CORD_CLEAR)
        send_notification("Card Found", "images/card.jpg")
        sleep(0.5)
        for i in range(6):
            click(CORD_PAY_SEQ[i])
            sleep(1)
        for i in range(3):
            playsound.playsound("bell.wav")
        sleep(10)
    click(CORD_KEY)

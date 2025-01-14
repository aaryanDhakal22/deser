import cv2
from time import sleep
import pyautogui
from pyautogui import click
from CORDS import *
import numpy as np
import playsound
from notifier import *
import pytesseract as pyt
from user import User

def is_empty(image_path, threshold=240, tolerance=0.95):
    image = cv2.imread(image_path)
    if image is None:
        print("Image not found")
        return False
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    white_pixel_ratio = np.mean(gray_image >= threshold)
    print(white_pixel_ratio, tolerance)
    return white_pixel_ratio >= tolerance

user1 = User()


while True:
    sleep(10)
    user1.take_screenshot()
    key_color = user1.key_color()
    user_name = user1.user_name()
    print(f"The key color is {key_color} and the user_name is {user_name}")
    if key_color == "yellow" or len(user_name) > 1:
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

    pyautogui.screenshot("assets/images/dynamic/scrollbar.jpg", region=(1273, 364, 20, 20))
    if is_empty("assets/images/dynamic/scrollbar.jpg"):
        print("Deliveries less than 11")
    else:
        pyautogui.moveTo(1282, 394)
        pyautogui.dragTo(1282, 890, 1, button="left")
    sleep(2)
    pyautogui.screenshot("assets/images/dynamic/all_delivs.jpg")
    image = cv2.imread("assets/images/dynamic/all_delivs.jpg")

    roi = image[400:900, 605:628]

    cv2.imwrite("assets/images/dynamic/original.jpg", roi)
    template = cv2.imread("assets/images/static/template_image.jpg")
    main_image = cv2.imread("assets/images/dynamic/original.jpg")
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
        pyautogui.screenshot("assets/images/dynamic/card.jpg", region=(514, 600, 311, 306))
        sleep(1)
        click(CORD_TEXT_AREA)
        sleep(0.5)
        click(CORD_CLEAR)
        send_notification("Card Found", "assets/images/dynamic/card.jpg")
        sleep(0.5)
        for i in range(6):
            click(CORD_PAY_SEQ[i])
            sleep(1)
        for i in range(3):
            playsound.playsound("assets/audio/bell.wav")
        sleep(60)
    click(CORD_KEY)

import cv2
from time import sleep
import pyautogui
from pyautogui import click
from CORDS import *
import pytesseract
from utils import location_prov


def startup():
    sleep(5)
    click(CORD_PASSKEY)
    sleep(0.5)
    click(CORD_PASSKEY)
    sleep(0.5)
    click(CORD_ENTER)
    sleep(0.5)
    click(CORD_DISPATCH)
    sleep(1)


image = cv2.imread("./original.png")

raw_address = []

for idx, i in enumerate(addr_cords):
    # roi = image[425:440, 710:837]
    roi = image[i[0] : i[1], i[2] : i[3]]
    cv2.imwrite(f"./images/new__{idx+1}.jpg", roi)
    text = pytesseract.image_to_string(roi)
    raw_address.append(text)


location_prov(raw_address)

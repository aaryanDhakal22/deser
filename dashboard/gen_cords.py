import cv2
from time import sleep
import pyautogui
from pyautogui import click
import pytesseract
from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim(user_agent="Delivery Helper")

CORD_PASSKEY = [840, 644]
CORD_ENTER = [928, 756]
CORD_DISPATCH = [979, 291]

addr_cords = []

x = 710
y = 425
l = 125
b = 15
for i in range(5):
    addr_cords.append([y, y + b, x, x + l])
    y += 45


def location_prov(raw_addresses):
    result = []
    for address in raw_addresses:
        end = address.find(",")
        if end != -1:
            address: str = address[:end]

        sleep(1)
        new_address = address.strip() + ", Baltimore, MD"
        location = geolocator.geocode(new_address, timeout=30)
        if location == None:
            address = " ".join(address.split()[:-1])
            new_address = address.strip() + ", Baltimore, MD"
            sleep(1)
            location = geolocator.geocode(new_address)
        result.append((location.latitude, location.longitude))
    return result


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


def gen_main():
    image = cv2.imread("D:/projects/deserDJ/dashboard/original.png")

    raw_address = []

    for idx, i in enumerate(addr_cords):
        # roi = image[425:440, 710:837]
        roi = image[i[0] : i[1], i[2] : i[3]]
        # cv2.imwrite(f"./images/new__{idx+1}.jpg", roi)
        text = pytesseract.image_to_string(roi)
        raw_address.append(text)

    locations = location_prov(raw_address)
    print("The locations are", locations)
    return locations

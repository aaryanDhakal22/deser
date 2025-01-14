import pyautogui
import cv2
import pytesseract as pyt
import numpy as np

class User:
    def __init__(self):
        self._screenshot = 0
        self._user_name = ""
        self._is_using = False
    
    def take_screenshot(self):
        pyautogui.screenshot("assets/images/dynamic/login_page.jpg")
        self._screenshot = cv2.imread("assets/images/dynamic/login_page.jpg")

    def user_name(self):
        aoi = self._screenshot[290:310,530:603]
        user_logged_in = pyt.image_to_string(aoi)
        print("\n",user_logged_in.strip()+" is logged in.","\n")
        return user_logged_in
    

    def key_color(self):
        square = self._screenshot[500:525, 962:985]
        average_color = np.mean(square, axis=(0, 1))
        color_list = list(average_color)
        if color_list[0] > 200 and color_list[1] > 200 and color_list[2] > 200:
            return "yellow"
        else:
            return "gray"
import pyautogui
import cv2
from time import sleep

sleep(2)
pyautogui.screenshot("check.jpg")
check_img = cv2.imread("check.jpg")
aoi = check_img[294:305, 548:595]
# ref_img = cv2.imread("aoi.jpg")
gray = cv2.cvtColor(aoi, cv2.COLOR_BGR2GRAY)
cv2.imwrite("aoi.jpg", gray)

import pyautogui
import time
import playsound
import keyboard


def beep():
    playsound.playsound("bell.wav")  # 1000 Hz frequency, 200 ms duration


print("Press SPACE to stop beeping...")

for i in range(3):
    beep()

import pyautogui
import time

import winsound
def beep():
    winsound.Beep(1000, 200)  # 1000 Hz frequency, 200 ms duration

print("Press SPACE to stop beeping...")

while True:
    beep()
    time.sleep(0.5)  # Beep interval
    if ' ' in pyautogui.keyDown('space'):
        print("Spacebar pressed, stopping beeps.")
        break

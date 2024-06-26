import winsound
from datetime import datetime
import pyautogui
from time import sleep

new_file = open(f"./cords/{datetime.now().strftime('%H_%M_%S')}.txt", "w")
sleep(4)
for i in range(4):

    winsound.Beep(500, 1000)
    winsound.Beep(600, 1000)
    winsound.Beep(700, 1000)
    new_file.write(str(pyautogui.position()))
    new_file.write("\n")

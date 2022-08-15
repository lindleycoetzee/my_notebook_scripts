import pyautogui
import time

x = 2
while x > 1:
    pyautogui.moveTo(240, 600, duration=0.5)
    pyautogui.moveTo(740, 70, duration=0.5)
    time.sleep(10)
    x += 1

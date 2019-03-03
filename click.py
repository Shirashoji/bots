import pyautogui as ag
import time


clicktimes = int(input('何回繰り返しますか: '))

time.sleep(5)

for i in range(clicktimes):
    ag.click()

import pyautogui as ag
import time
#coordinate 座標
clicktimes = int(input('何回繰り返しますか: '))
#clicktimes = 100
time.sleep(5)

for i in range(clicktimes):
    ag.click()
    #ag.typewrite('Hello world!\n')  # intervalは文字間の入力待機時間です．

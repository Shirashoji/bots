#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui, time
import pyperclip

text = input("何を送りますか?: ")
pyperclip.copy(text)


clicktimes = int(input('何回繰り返しますか: '))

time.sleep(5)


for i in range(clicktimes):
    pyautogui.hotkey('command','v') #Mac
#    pyautogui.hotkey('ctrl','v') #Win
    pyautogui.hotkey('command','\n')


pyautogui.typewrite('Written by Python Program.')
pyautogui.hotkey('command','\n') #Mac
#pyautogui.hotkey('ctrl','v') #Win

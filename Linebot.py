#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui, time
#coordinate 座標
times = 20

time.sleep(2)

for i in range(times):
    pyautogui.typewrite('Hello, World!!')
    pyautogui.hotkey('command','\n')

pyautogui.typewrite('Written by Python Program.')
pyautogui.hotkey('command','\n')

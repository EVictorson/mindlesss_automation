#!/usr/bin/env python

# quick python script to automate the stupid screen clicks required for training modules

import pyautogui as pag
import sys

# spam a left click at current mouse location with sleep of <interval> seconds

def init(interval):
    pag.PAUSE = interval
    pag.FAILSAFE = True

def spam_clicks():
    try:
        while(True):
            pag.click()
    except KeyboardInterrupt:
        print('\n')

def run():
    print('Position mouse over location you would like to spam.')
    print('Moving the mouse to the upper-left will raise an exception to exit the program.')
    spam_clicks(5)


if __name__ == '__main__':
    init(5)
    run()

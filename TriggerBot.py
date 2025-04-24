"""
Module: TriggerBot.py
Author: Felix Nguyen
Date: 2025-04-24
Description: when cursor comes in contact with chosen color it will click it instantly
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tutorial used https://www.youtube.com/watch?v=YRAIUA-Oc1Y&ab_channel=KianBrose
#modified


#color yellow on overwatch (enemy outline): (255,255,0)
#middle of screen: X: 960 and Y: 540
screen_x = 960
screen_y = 540
target_color = (255, 255, 0) 
click_delay = 0.01 #10 ms delay between clicking down/up

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(click_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('f') == False:

    print("TriggerBot Activated:\n")
    print("Press F To Stop")

    current_pixel = pyautogui.pixel(screen_x,screen_y)

    #abs = absolute value number
    #example (245, 250, 5) is in range because each rgb value is withn 100 (can modify to make it more range)

    red_match = abs(current_pixel[0] - target_color[0]) < 100   
    green_match = abs(current_pixel[1] - target_color[1]) < 100 
    blue_match = abs(current_pixel[2] - target_color[2]) < 100 
    # if all the colors match then click 
    if red_match and green_match and blue_match:
        click(screen_x, screen_y)
        time.sleep(0.05) 

    time.sleep(click_delay)
    
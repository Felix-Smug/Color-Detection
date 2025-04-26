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
import math

#tutorial used https://www.youtube.com/watch?v=YRAIUA-Oc1Y&ab_channel=KianBrose
#modified


#color yellow on overwatch (enemy outline): (255,255,0) or use (219, 219, 10) for yellow
#middle of screen: X: 960 and Y: 540
screen_x = 960
screen_y = 540
target_color = (219, 219, 10)  #can change colors 
click_delay = 0.01 #10 ms delay between clicking down/up
radius = 10

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(click_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('f') == False:
    print("TriggerBot Activated:\n")
    print("Hold F To Stop")
    
    found_target = False
    
    # CIRCLE AROUND THE CROSSHAIR
    for x in range(screen_x - radius, screen_x + radius + 1):
        
        for y in range(screen_y - radius, screen_y + radius + 1):

            # only check pixels within the radius
            if math.sqrt((x - screen_x)**2 + (y - screen_y)**2) <= radius:
                try:
                    current_pixel = pyautogui.pixel(x, y)
                    red_match = abs(current_pixel[0] - target_color[0]) < 65  
                    green_match = abs(current_pixel[1] - target_color[1]) < 65
                    blue_match = abs(current_pixel[2] - target_color[2]) < 65
                    
                    if red_match and green_match and blue_match:
                        click(screen_x, screen_y)
                        found_target = True
                        break
                except:
                    pass
        
        if found_target:
            break
    
    time.sleep(click_delay)
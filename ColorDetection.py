"""
Module: ColorDetection.py
Author: Felix Nguyen
Date: 2025-04-21
Description: Select color and cursor will click the middle of your screen (Triggerbot)
"""

import pyautogui
import json
import time
import os
import re
import win32api, win32con
import math
import keyboard
import random
import threading

# using tutorial https://www.youtube.com/watch?v=lyoyTlltFVU&ab_channel=BroCode
from tkinter import *
from tkinter import simpledialog 
from tkinter import messagebox
from tkinter import colorchooser

# aim color will be used as a global variable
aim_color = None

window = Tk()
window.geometry("400x400")
window.title("Color Detection GUI")

# photo image catsss
icon = PhotoImage(file='cat.png')
window.iconphoto(True,icon)
window.config(background="grey")


# Main menu Title
title = Label(window, text="Color Detection", font=("Roboto", 24, "bold"), bg="grey", fg="white")
title.pack(pady=24) #reposition title 


#1st Button Function
def enterRGBValue():
    
    global aim_color 

    #get user input for valid rgb value or cancel
    idValue = simpledialog.askstring("Enter RGB", "Enter RGB Value (ex. (255,255,10)):")

    try:
        idValue = idValue.strip('() ')
        r, g, b = map(int, idValue.split(','))

        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            
            aim_color = (r, g, b)
            print(f"Valid RGB Color: {aim_color}")
            return

        else:
            messagebox.showerror("Invalid", "RGB values must in between 0-255")

    except:
        messagebox.showerror("Invalid", "Please use example provide to Type Valid (R,G,B)")

    

#2nd Button Function : https://www.youtube.com/watch?v=NDCirUTTrhg&ab_channel=Codemy.com

def color():

    global aim_color 

    chooseColor = colorchooser.askcolor()

    if chooseColor[0] == None:
        print("No Chosen Color")
        return
    
    print(f"Color Chosen: {chooseColor}")
    aim_color = chooseColor[0]


#3rd button function

def click(x,y):
    click_delay = 0.01
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(click_delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def triggerbot():
    
    if aim_color is None:
        messagebox.showerror("Warning", "No Color Was Selected")
        return
    
    button3.config(text="Running... Hold F to stop", state=DISABLED)
    window.update()

    #get user size of screen
    screen_x, screen_y = pyautogui.size() 
    screen_x, screen_y = screen_x // 2, screen_y // 2 
    target_color = aim_color
    click_delay = 0.01 #10 ms delay between clicking down/up
    
    #prompt user to enter radius
    radius = simpledialog.askstring("Enter Radius", "Enter Radius Value (ex. 10 or 15):")
    
    if not radius:
        button3.config(text="3. Run Color TriggerBot", state=NORMAL)
        return
    
    try:
        radius = int(radius)
    except ValueError:
        messagebox.showerror("Error", "Invalid radius value")
        button3.config(text="3. Run Color TriggerBot", state=NORMAL)
        return

    status_label = Label(window, text="TriggerBot Active: Hold F to stop", font=("Roboto", 12), bg="grey", fg="white")
    status_label.pack(pady=10)
    window.update()

    def run_trigger():
        while not keyboard.is_pressed('f'):
            found_target = False
            try:

                # check a smaller region on your screen
                screenshot = pyautogui.screenshot(region=(screen_x - radius, screen_y - radius, radius*2, radius*2))
                
                for x in range(0, radius*2):

                    for y in range(0, radius*2):

                        # only check pixels within the radius
                        if math.sqrt((x - radius)**2 + (y - radius)**2) <= radius:
                            current_pixel = screenshot.getpixel((x, y))
                            red_match = abs(current_pixel[0] - target_color[0]) < 65  
                            green_match = abs(current_pixel[1] - target_color[1]) < 65
                            blue_match = abs(current_pixel[2] - target_color[2]) < 65
                            
                            if red_match and green_match and blue_match:
                                click(screen_x, screen_y)
                                found_target = True
                                break

                    if found_target:
                        break
            except:
                print("Error")
            
            time.sleep(0.01)  
        
        status_label.destroy()
        button3.config(text="3. Run Color TriggerBot", state=NORMAL)
        window.update()

    threading.Thread(target=run_trigger, daemon=True).start()

#4th Button Exit Function
def endProgram():
    window.quit()



#Buttons (1-4)
button1 = Button(text="1. Enter Color (RGB Value)", font=("Roboto", 14), width=30, command=enterRGBValue)
button1.pack(pady=10)

button2 = Button(text="2. Pick a color", font=("Roboto", 14), width=30, command=color)
button2.pack(pady=10)

button3 = Button(text="3. Run Color TriggerBot", font=("Roboto", 14), width=30, command=triggerbot)
button3.pack(pady=10)

button4= Button(text="4. Exit", font=("Roboto", 14), width=30, command=endProgram)
button4.pack(pady=10)





window.mainloop()





#original idea having the user input but I wanted a more interative experience
'''
def main():
    
    # Menu GUI 

    while True:
        print("\n")
        print("1. Enter Color ID (HEX)")
        print("2. Click a color on your screen")
        print("3. Exit")

        option = input("Option: ")
        int(option)

        if option == 1:
            
        elif option == 2:

        elif option == 3:
            break
        else: 
            print("Invalid Option (1-3)")


main()

'''
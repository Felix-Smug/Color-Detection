"""
Module: ColorDetection.py
Author: Felix Nguyen
Date: 2025-04-21
Description: Choose a color through hex or click on it in your screen which will then prompt your cursor to click on the item
"""

import pyautogui
import json
import time
import os
import re

# using tutorial https://www.youtube.com/watch?v=lyoyTlltFVU&ab_channel=BroCode
from tkinter import *
from tkinter import simpledialog 
from tkinter import messagebox

window = Tk()
window.geometry("400x400")
window.title("Color Detection GUI")

# photo image catsss
icon = PhotoImage(file='cat.png')
window.iconphoto(True,icon)
window.config(background="grey")


# Main menu Title
title = Label(window, text="Color Detection", font=("Roboto", 24, "bold"), bg="grey", fg="white")
title.pack(pady=24) #reposition title in the middle


#1st Button Function
def enterHexID():
    
    #get user input and keep asking until user enter valid hex or cancel
    while True: 

        idValue = simpledialog.askstring("Enter HEX", "Enter HEX ID (ex. #FF0000):")

        validHex = re.fullmatch(r'#?[0-9A-Fa-f]{6}', idValue)

        if validHex:

            if not idValue.startswith("#"):
                idValue = "#" + idValue
            

            print(f"Valid Hex: {idValue}")
            break

        else:
            messagebox.showerror("Invalid", "Enter Valid Hex Value")


#2nd Button Function

#3rd Button Exit Function
def endProgram():
    window.quit()



#Buttons (1-4)
button1 = Button(text="1. Enter Color ID (HEX)", font=("Roboto", 14), width=30, command=enterHexID)
button1.pack(pady=10)

button2 = Button(text="2. Click a color on your screen", font=("Roboto", 14), width=30)
button2.pack(pady=10)

button3 = Button(text="3. Run Suspiciously Good Aim", font=("Roboto", 14), width=30)
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
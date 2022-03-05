# Original code credit goes to https://www.youtube.com/watch?v=YRAIUA-Oc1Y. I have used this code to practice.
#game URL: https://gameforge.com/en-US/littlegames/magic-piano-tiles/#

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con



first_tile = 0
second_tile = 0
third_tile = 0
fourth_tile = 0

"""
Calls the pyautogui.position() function after you press the described key and stores the x and y
coordinates in the coresponding variable.

This variable is then used in the click() function.
"""

print("Move your coursor to the first tile and press the d key.")
while keyboard.is_pressed('d') == False:
    first_tile = pyautogui.position()

print("Move your coursor to the first tile and press the e key.")
while keyboard.is_pressed('e') == False:
    second_tile = pyautogui.position()
    
print("Move your coursor to the first tile and press the r key.")
while keyboard.is_pressed('r') == False:
    third_tile = pyautogui.position()
    
print("Move your coursor to the first tile and press the t key.")
while keyboard.is_pressed('t') == False:
    fourth_tile = pyautogui.position()

print("To kill the programm press the 'q' key.")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(first_tile[0], first_tile[1])[0] == 0:
        click(first_tile[0], first_tile[1])

    if pyautogui.pixel(second_tile[0], second_tile[1])[0] == 0:
        click(second_tile[0], second_tile[1])
        
    if pyautogui.pixel(third_tile[0], third_tile[1])[0] == 0:
        click(third_tile[0], third_tile[1])
        
    if pyautogui.pixel(fourth_tile[0], fourth_tile[1])[0] == 0:
        click(fourth_tile[0], fourth_tile[1])

from subprocess import Popen
import pyautogui
import time
import pandas as pd

print("Grading started")
pyautogui.hotkey('alt', 'tab') # Move to browser after initialize

mark_always = pyautogui.locateCenterOnScreen('repair.PNG') 
pyautogui.click(mark_always.x-35, mark_always.y)
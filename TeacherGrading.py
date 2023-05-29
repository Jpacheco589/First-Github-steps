from subprocess import Popen
import pyautogui
import time
import pandas as pd

# Code to make the teachers grading holding in an
# automatic way. This code must not be shared and 
# has been made only with educational purposes. 

times = 10 # Replace with the number of teachers. 
end_or_progress = 3 # Change to 3 to execute normally, change to 4 to test

print("Grading started")
pyautogui.hotkey('alt', 'tab') # Move to browser after initialize

for i in range(times):
    # Insert code here
    time.sleep(1)
    scroll_set = pyautogui.locateCenterOnScreen('set.PNG')
    pyautogui.moveTo(scroll_set)
    pyautogui.click()
    pyautogui.press('down', presses=4) # Show all of the teachers on screen
    time.sleep(1)
    init_dot = pyautogui.locateCenterOnScreen('pendiente.PNG') 
    if init_dot is not None:
        print("Pendiente encontrada")
        pyautogui.click(init_dot.x-350, init_dot.y) # Move and click mouse to ungraded teacher
        time.sleep(6) # Wait till screen changes
        pyautogui.press('tab', presses=8) # Move to the first selecting dot
        pyautogui.press('down', presses=4) # Move to the 'Good' statement
        
        for z in range(12):
            pyautogui.press('tab')
            pyautogui.press('down', presses=4)
            time.sleep(0.1)
        pyautogui.press('tab', presses=end_or_progress) # End teacher grading
        time.sleep(1)
        pyautogui.press('enter')
    else:
        print("No hay pendientes, asignando 'en progreso'")
        progress_form = pyautogui.locateCenterOnScreen('inprogress.PNG') 
        print("En progreso encontrada")
        pyautogui.click(progress_form.x-350, progress_form.y) # Move and click mouse to ungraded teacher
        time.sleep(6) # Wait till screen changes
        pyautogui.press('tab', presses=8) # Move to the first selecting dot

        # Make sure everything is all right
        check_state = pyautogui.locateCenterOnScreen('cheking.PNG') 
        if check_state is not None:
            print("Sin problemas de calificación encontrados")
            for z in range(12):
                pyautogui.press('tab') # select and move to end
                time.sleep(0.1)
            pyautogui.press('tab', presses=end_or_progress) # End teacher grading
            time.sleep(1)
            pyautogui.press('enter')
        else: 
            print("Profesor calificado con mala calificación")
            # Move to good grade
            mark_always = pyautogui.locateCenterOnScreen('repair.PNG') 
            pyautogui.click(mark_always.x-35, mark_always.y)
            # chekmark repaired!
            for z in range(12):
                pyautogui.press('tab')
                pyautogui.press('down', presses=4)
                time.sleep(0.1)
            pyautogui.press('tab', presses=end_or_progress) # End teacher grading
            time.sleep(1)
            pyautogui.press('enter')
        
    

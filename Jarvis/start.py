import os
import keyboard
import time

while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('o'):
        os.startfile("C:/Users/1/Desktop/Progs/Py/Jarvis.py")
        time.sleep(1)
        try:
            os.close("C:/Users/1/Desktop/Progs/Py/cv_keyboard.py") 
        except Exception:
            print("Другие файлы не активны")
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('p'):
        os.startfile("C:/Users/1/Desktop/Progs/Py/cv_keyboard.py")
        time.sleep(1)
        try:
            os.close("C:/Users/1/Desktop/Progs/Py/Jarvis.py")
        except Exception:
            print("Другие файлы не активны")
            
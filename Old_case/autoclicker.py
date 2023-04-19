import pyautogui as pa
import keyboard
import time

def main():
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('d'):
            text=pa.prompt(text='Please enter text or code of emoji', title='Input Data', default='').split()
            print(text)
            if len(text)!=0:
                time.sleep(5)
                while True:
                    pa.write(text)
                    pa.press('enter')
                    if keyboard.is_pressed('esc'):
                        break
                    #pa.click()
if __name__=="__main__":
    main()
            


                



            
        


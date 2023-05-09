import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import cvzone
import pyautogui

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 
                        20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 5, y + 60), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        cv2.rectangle(img, (190, 0), (192, 720), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (430, 0), (432, 720), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (0, 160), (720, 162), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (0, 340), (720, 342), (0, 255, 0), cv2.FILLED)
        
    return img

class Button():
    def __init__(self, pos, text, size):
        self.pos = pos
        self.size = size
        self.text = text

def main():
    cap = cv2.VideoCapture(0)

    cap.set(3, 720)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=1)

    buttonList = []
    buttonList.append(Button([210, 215], 'SP', [100, 70]))
    buttonList.append(Button([320, 215], 'BS', [100, 70]))
    buttonList.append(Button([600, 0], 'EX', [100, 60]))

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList, bboxInfo = detector.findPosition(img)
        img = drawAll(img, buttonList)

        if lmList:
            fingers=[]
            for i in 8, 12, 16, 20:
                if lmList[i][1]>lmList[i-3][1]:
                    fingers.append(0)
                if lmList[i][1]<lmList[i-3][1]:
                    fingers.append(1)
            totalFingers = fingers.count(1)
            if totalFingers==3:
                if lmList[8][0]>432:
                    pyautogui.press('Right') 
                    sleep(0.15)
                if lmList[8][0]<190:
                    pyautogui.press('Left')
                    sleep(0.15)
                if lmList[8][1]>340:
                    pyautogui.press('Down') 
                    sleep(0.15)
                if lmList[8][1]<160:
                    pyautogui.press('Up') 
                    sleep(0.15)      

            if totalFingers==0:
                pyautogui.press('Space')
                sleep(0.15)

            if totalFingers==2:
                for button in buttonList:
                    x, y = button.pos
                    w, h = button.size
                    if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                        cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 5, y + 60), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        l, _, _ = detector.findDistance(8, 12, img)
                        if l < 35 :
                            if button.text=='SP':
                                pyautogui.press('Space')
                            elif button.text=='BS':
                                pyautogui.press('backspace')
                            elif button.text=='EX':
                                pass
                            sleep(0.15)
        key = cv2.waitKey(1)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        if key == ord('q'):
            cv2.destroyAllWindows()
            break
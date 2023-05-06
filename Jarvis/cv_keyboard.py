import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import cvzone
import pyautogui
import os

cap = cv2.VideoCapture(0)

cap.set(3, 1920)
cap.set(4, 1200)

detector = HandDetector(detectionCon=1)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]


def drawAll(img, buttonList):
    
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]), 
                        20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        cv2.rectangle(img, (450, 0), (452, 720), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (798, 0), (800, 720), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (0, 498), (1280, 500), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (0, 260), (1280, 262), (0, 255, 0), cv2.FILLED)
    return img


class Button():
    def __init__(self, pos, text, size=[80, 80]):
        self.pos = pos
        self.size = size
        self.text = text
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 150, 100 * i + 100], key))
buttonList.append(Button([300, 400], 'Space', [500, 80]))
buttonList.append(Button([810, 400], 'BS', [95, 85]))
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
            if lmList[8][0]>800:
                pyautogui.press('Right') 
                sleep(0.15)
            if lmList[8][0]<450:
                pyautogui.press('Left')
                sleep(0.15)
            if lmList[8][1]>500:
                pyautogui.press('Down') 
                sleep(0.15)
            if lmList[8][1]<260:
                pyautogui.press('Up') 
                sleep(0.15)      

        if totalFingers==0:
            pyautogui.press('Enter')
            sleep(0.15)

        if totalFingers==2:
            for button in buttonList:
                x, y = button.pos
                w, h = button.size
                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    l, _, _ = detector.findDistance(8, 12, img)
                    if l < 35 :
                        if button.text=='Space':
                            pyautogui.press('Space')
                        elif button.text=='BS':
                            pyautogui.press('backspace')
                        else:
                            pyautogui.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65),
                                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        sleep(0.15)

    key = cv2.waitKey(1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break


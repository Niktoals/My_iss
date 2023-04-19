import cv2
from cvzone.HandTrackingModule import HandDetector
import time

class Button:
    def __init__(self, pos, width, height, value):
        
        self.pos=pos
        self.width=width
        self.height=height
        self.value=value

    def draw(self, img, ):
        cv2.rectangle(img, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height),
                    (225, 225, 255), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height),
                    (50, 50, 50), 3)
        cv2.putText(img, self.value, (self.pos[0]+40, self.pos[1]+60), cv2.FONT_HERSHEY_PLAIN,
                    2, (50,50,50), 2)

    def Check_click(self, x, y):
        if self.pos[0]<x<self.pos[0]+self.width and \
            self.pos[1]<y<self.pos[1]+self.height:
            cv2.rectangle(img, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height),
                    (225, 225, 255), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height),
                    (50, 50, 50), 3)
            cv2.putText(img, self.value, (self.pos[0]+25, self.pos[1]+80), cv2.FONT_HERSHEY_PLAIN,
                    5, (0,0,0), 5)
            return True
        else:
            return False


# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector= HandDetector(detectionCon=0.8, maxHands=1)

#creating buttons
buttonlistvalues=[['7', '8', '9', '*'],
                ['4', '5', '6', '-'],
                ['1', '2', '3', '+'],
                ['0', '/', '.', '=']]

buttoncoords_x=[]
buttoncoords_y=[]
buttonlist=[]
for x in range(4):
    for y in range(4):
        xpos= x*100 + 800
        ypos= y*100+150
        buttonlist.append(Button((xpos, ypos), 100, 100, buttonlistvalues[y][x]))
        buttoncoords_x.append(xpos)
        buttoncoords_y.append(ypos)



#variables
myEquation= ''
delayCounter=0

while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)

    #Detection of hand
    hands, img = detector.findHands(img, flipType=False)

    #draw our buttons
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 100),
                (225, 225, 255), cv2.FILLED)
    cv2.rectangle(img, (800, 50), (800 + 400, 70 + 100),
                (50, 50, 50), 3)
    for button in buttonlist:
        button.draw(img)

    #check for Hand
    if hands:
        lmList = hands[0]['lmList']
        fingers=[]
        x1=lmList[8][0]
        x2=lmList[12][0]
        y1=lmList[8][1]
        y2=lmList[12][1]
        lenght= (((x2-x1)**2) +((y2-y1)**2))**(0.5)

        for i in 8, 12, 16, 20:
            if lmList[i][1]>lmList[i-3][1]:
                fingers.append(0)
            if lmList[i][1]<lmList[i-3][1]:
                fingers.append(1)
        totalFingers = fingers.count(1)
        x, y, _=lmList[8]
        if totalFingers==0:
            myEquation=''

        if totalFingers==2:
            if lenght<35:
                for i, button in enumerate(buttonlist):
                    if button.Check_click(x, y) and delayCounter == 0:
                        myValue=buttonlistvalues[int(i%4)][int(i/4)]
                        if myValue == '=':
                            myEquation = str(eval(myEquation))
                        else:
                            myEquation+=myValue
                        delayCounter = 1

    #avoid dubles
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter> 10:
            delayCounter = 0

    #proccessing 
    cv2.putText(img, myEquation, (810, 120), cv2.FONT_HERSHEY_PLAIN,
                3, (50,50,50), 3)
    #display the result


    # Display imageс
    key = cv2.waitKey(1)
    cv2.imshow("Image", img)
    if key == ord('c'):
        myEquation=''
    if key == ord("q"):
        cv2.destroyAllWindows()
        break


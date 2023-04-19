from tkinter import *
import datetime
time=datetime.datetime.today().strftime("%H%M")
day=datetime.datetime.today().strftime("%w")
time=int(time)
day=int(day)
P_b_a113=[542,617,652,728,754,827,900,931,1002,1047,1131,1215,1300,1345,1431,1515,1558,1644,1713,1742,1810,1839,1907,1933,1959,2054,2142,2237,2332]
P_v_a113=[547,640,736,832,913,953,1033,1113,1153,1233,1303,1333,1403,1432,1502,1532,1612,1651,1731,1811,1851,1930,2009,2048,2122,2156,2244,2332]
N_b_a113=[557,630,704,730,803,834,904,935,1019,1104,1148,1233,1318,1404,1449,1532,1618,1647,1716,1745,1814,1842,1909,1934,2030,2122,2215,2312,2,53]
N_v_a113=[621,716,811,851,931,1010,1049,1129,1209,1239,1309,1339,1409,1439,1509,1549,1629,1709,1749,1829,1908,1947,2026,2104,2137,2226,2315,4,53]

ma=[]
list_st=['P_b_a113', 'P_v_a113', 'N_b_a113', 'N_v_a113']


def des():
    hi.destroy()
def pere():
    global list_st
    for i in list_st:
        if i =='P_b_a113':
            list_st=P_b_a113
        if i =='P_v_a113':
            list_st=P_v_a113
        if i =='N_b_a113':
            list_st=N_b_a113
        if i =='N_v_a113':
            list_st=N_v_a113
def station(n, l):
    global list_st
    count=0
    for i in list_st:
        if i[n]!=l:
            count+=1
    for i in range(count):
        for i in list_st:
            index = list_st.index(i)
            if i[n]!=l:
                list_st.pop(index)
        
def days():
    global day
    if day==0 or day>5:
        station(2, 'v')
    elif day<=5:
        station(2, 'b')

def times():
    global ma
    global list_st
    global time
    for i in list_st:
        if i>time:
            ma.append(i)
            print(ma)

def ans():
    global time
    global a
    global b
    answer=str(ma[0])
    t=str(time)
    if len(str(time))<4:
        time='0'*(4-int(len(str(time))))+str(time)
    if len(str(answer))<4:
        answer='0'*(4-int(len(str(answer))))+str(answer)
    c=answer[: 2]
    if int(t[2:4])<60 and int(c)>int(t[0:2]):
        ti=60-int(t[2:4])
        tim=c+'00'
        e=(int(answer)-int(tim))+ti
    else:
        e=int(answer)-int(time)
    f=answer[:2]
    c=answer[2: 4]
    a='Ближайший авобус 113 в '+ str(f)+':'+str(c)
    b='До автобуса '+ str(e)+ ' минут'
def clear():
    global name_entry
    name_entry.delete(0, END)
def getTextInput():
    global result
    result=name.get()
    if len(result)>0:
        if result=='Профсоюзная':
            station(0, 'P')
        if result=='Черемушки':
            station(0, 'N')
        print(list_st)
        days()
        pere()
        times()
        ans()
        window.geometry("350x150")
        text = Label(text=a)
        text1 = Label(text=b)
        text.grid(row=1, column=0, sticky="w" )
        text1.grid(row=2, column=0, sticky="w" )
def start():
    des()
    global name
    global name_entry
    window.geometry("300x150")
    name=StringVar()
    window.title("Ближайший аувтобус!")
    name_label = Label(text="Введите станцию:")
    name_label.grid(row=0, column=0, sticky="w")
    name_entry = Entry(textvariable=name)
    name_entry.grid(row=0,column=2, padx=5, pady=5)
    group_name_button = Button(text="Ввод", command=getTextInput)
    clear_button = Button(text="Отчистить", command=clear)
    again=Button(text="Опять", command=ag)
    bye=Button(text='Пока', command=byebye)
    bye.place(x=130, y=60)
    again.place(x=200, y=60)
    group_name_button.grid(row=1,column=2, padx=5, pady=5, sticky="w")
    clear_button.grid(row=1, column=2, padx=5, pady=5, sticky="e")
def byebye():
    window.destroy()
def ag():
    byebye()
    ok()
def ok():
    global text
    global hi
    global window
    window = Tk()
    text = Text()
    window.attributes("-topmost",True)
    window.geometry("300x150")
    hi=Button(text="Начать", command=start)
    hi.place(x=130, y=60)
    window.mainloop()
result=''    
b=''
a=''
print(day)
ok()
# Надо добавить ночье время с первым рейсом и извинением

#Разобрать с временем после 00:00
#Синхронизация остаточного времени в ночьное врем




import time
import random
from tkinter import *
import datetime
 
def des():
    hi.destroy()
def pere():
    global list_st
    for i in list_st:
        if i =='P_b_a113':
            list_st=P_b_a113
        if i =='P_v_a113':
            list_st=P_v_a113
        if i =='N_b_a113':
            list_st=N_b_a113
        if i =='N_v_a113':
            list_st=N_v_a113
def station(n, l):
    global list_st
    count=0
    for i in list_st:
        if i[n]!=l:
            count+=1
    for i in range(count):
        for i in list_st:
            index = list_st.index(i)
            if i[n]!=l:
                list_st.pop(index)
                
def days():
    global day
    if day==0 or day>5:
        station(2, 'v')
    elif day<=5:
        station(2, 'b')

def times():
    global ma
    global list_st
    global time
    for i in list_st:
        if i>time:
            ma.append(i)

def ans():
    global time
    global a
    global b
    answer=str(ma[0])
    t=str(time)
    if len(str(time))<4:
        time='0'*(4-int(len(str(time))))+str(time)
    if len(str(answer))<4:
        answer='0'*(4-int(len(str(answer))))+str(answer)
    c=answer[: 2]
    if int(t[2:4])<60 and int(c)>int(t[0:2]):
        ti=60-int(t[2:4])
        tim=c+'00'
        e=(int(answer)-int(tim))+ti
    else:
        e=int(answer)-int(time)
    f=answer[:2]
    c=answer[2: 4]
    a='Ближайший авобус 113 в '+ str(f)+':'+str(c)
    b='До автобуса '+ str(e)+ ' минут'
def clear():
    global name_entry
    name_entry.delete(0, END)
def getTextInput():
    global result
    result=name.get()
    if len(result)>0:
        if result=='Профсоюзная':
            station(0, 'P')
        if result=='Черемушки':
            station(0, 'N')
        days()
        pere()
        times()
        ans()
        window.geometry("350x150")
        text = Label(text=a)
        text1 = Label(text=b)
        text.grid(row=1, column=0, sticky="w" )
        text1.grid(row=2, column=0, sticky="w" )
def start():
    des()
    global name
    global name_entry
    window.geometry("300x150")
    name=StringVar()
    window.title("Ближайший аувтобус!")
    name_label = Label(text="Введите станцию:")
    name_label.grid(row=0, column=0, sticky="w")
    name_entry = Entry(textvariable=name)
    name_entry.grid(row=0,column=2, padx=5, pady=5)
    group_name_button = Button(text="Ввод", command=getTextInput)
    clear_button = Button(text="Отчистить", command=clear)
    again=Button(text="Опять", command=ag)
    bye=Button(text='Пока', command=byebye)
    bye.place(x=130, y=60)
    again.place(x=200, y=60)
    group_name_button.grid(row=1,column=2, padx=5, pady=5, sticky="w")
    clear_button.grid(row=1, column=2, padx=5, pady=5, sticky="e")
def byebye():
    window.destroy()
def ag():
    byebye()
    ok()
def ok():
    global text
    global hi
    global window
    global wind
    wind.destroy()
    window = Tk()
    text = Text()
    window.attributes("-topmost",True)
    window.geometry("300x150")
    hi=Button(text="Начать", command=start)
    hi.place(x=130, y=60)
    window.mainloop()


def chek():
    global otvet
    otvet=var.get()
    if otvet==password:
        ok()

def change():
    global symbls
    global password
    random.shuffle(symbls)
    for i in symbls:
        password+=i
    print(password)
def passw():
    global y
    global symbls
    global password

    change()
time=datetime.datetime.today().strftime("%H%M")
day=datetime.datetime.today().strftime("%w")
time=int(time)
day=int(day)
P_b_a113=[542,617,652,728,754,827,900,931,1002,1047,1131,1215,1300,1345,1431,1515,1558,1644,1713,1742,1810,1839,1907,1933,1959,2054,2142,2237,2332]
P_v_a113=[547,640,736,832,913,953,1033,1113,1153,1233,1303,1333,1403,1432,1502,1532,1612,1651,1731,1811,1851,1930,2009,2048,2122,2156,2244,2332]
N_b_a113=[557,630,704,730,803,834,904,935,1019,1104,1148,1233,1318,1404,1449,1532,1618,1647,1716,1745,1814,1842,1909,1934,2030,2122,2215,2312,2,53]
N_v_a113=[621,716,811,851,931,1010,1049,1129,1209,1239,1309,1339,1409,1439,1509,1549,1629,1709,1749,1829,1908,1947,2026,2104,2137,2226,2315,4,53]
ma=[]
list_st=['P_b_a113', 'P_v_a113', 'N_b_a113', 'N_v_a113']
result=''    
b=''
a=''

otvet=''
symbls=['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
password=''
y=True
passw()
wind = Tk()
wind.title("************************")
wind.geometry('400x300')
wind.attributes("-topmost",True)
text=Label(wind, text='Ввдите пароль')
text.place(x=150, y=80)
btn = Button(wind, text="Ok", command=chek)
btn.place(x=150, y=120)
var = StringVar()
check = Entry(textvariable=var)
check.place(x=150, y=100)
wind.mainloop()

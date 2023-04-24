from vosk import Model, KaldiRecognizer
import pyaudio
import os
import json
import pyautogui as pg
import keyboard
import time
from fuzzywuzzy import fuzz
import random
from pydub import AudioSegment
from pydub.playback import play
import psutil
import webbrowser 
import pvporcupine
import struct

def mon_bet():
    battery = psutil.sensors_battery()
    plug=battery.power_plugged
    if battery.percent==2 and plug==False:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/2 %.wav'))
    elif battery.percent==7 and plug==False:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/7 %.wav'))
    elif battery.percent==11 and plug==False:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/11 %.wav'))
    elif battery.percent==13 and plug==False:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/Энергия 13%.wav'))
    elif battery.percent==15 and plug==False:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/Энергия 15 %.wav'))
    elif battery.percent==19 and plug==False:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/Сэр, энергия 19 %.wav'))
    elif battery.percent==48 and plug==False:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/Энергия 48% и падает сэр.wav'))
        
def analis_of_digits(res):
    if fuzz.partial_ratio("один", res["text"])>=90:
        return 100
    if fuzz.partial_ratio("два", res["text"])>=90:
        return 200
    if fuzz.partial_ratio("три", res["text"])>=90:
        return 300
    if fuzz.partial_ratio("четыре", res["text"])>=90:
        return 400
    if fuzz.partial_ratio("пять", res["text"])>=90:
        return 500    

def user_set_do(settings_do, res, count_scr):


    if fuzz.partial_ratio("пауза", res["text"][6::])>=90:
        pg.press('space')
        

    for key in settings_do.keys():
        id_key=res["text"].find(key[1::])
        
        if fuzz.partial_ratio(key[1::], res["text"])>=80 and settings_do[key]=='0':
            play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Да сэр", "Загружаю сэр", "Есть", "Как пожелаете ", "К вашим услугам сэр", "Запрос выполнен сэр", "Образ создан"])}.wav'))
            screen=pg.screenshot()
            if not os.path.exists("photos"):
                os.mkdir("photos")
            screen.save(f"photos/screen{count_scr}.png")
            count_scr+=1

        if fuzz.partial_ratio(key[1::], res["text"])>=90 and settings_do[key]=='0':
            play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Да сэр", "Загружаю сэр", "Есть", "Как пожелаете ", "К вашим услугам сэр", "Запрос выполнен сэр", "Образ создан"])}.wav'))
            fPath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(fPath).open("https://www.google.com/search?q=" + res["text"][id_key+6::])

        if fuzz.partial_ratio(key[1::], res["text"])>=90 and settings_do[key]!='0':
            play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Да сэр", "Загружаю сэр", "Есть", "Как пожелаете ", "К вашим услугам сэр", "Запрос выполнен сэр", "Образ создан"])}.wav'))
            os.startfile(settings_do[key])

def reading_settings():
    if not os.path.exists("settings.txt"):
        f = open('settings.txt', "w", encoding='utf-8', errors='replace')
        f.write(" играть,snake_001.py, браузер,C:/Program Files/Google/Chrome/Application/chrome.exe")
        f.close()
        
    f = open('settings.txt', encoding='utf-8', errors='replace')
    d=[n for n in f.read().split(",")]
    settings_do={}
    for i in range(1, len(d), 2):
        settings_do[d[i-1]]=d[i]
    f.close()
    return settings_do

def reading_model():
    if not os.path.exists("model.txt"):
        f = open('model.txt', "w", encoding='utf-8', errors='replace')
        text=pg.prompt(text='plese choose your model', title='Input Data', default="model small/big model")
        if fuzz.partial_ratio(text, "big")>=100 and text!="model small/big model":
            f.write("vosk-model-ru-0.42")
        if fuzz.partial_ratio(text, "small")>=100 and text!="model small/big model":
            f.write("model_small")
        f.close()
    f = open('model.txt', "r", encoding='utf-8', errors='replace')
    model=f.read()
    f.close()
    return model

def adding():
    global settings_do
    text=pg.prompt(text='"*"keyword,operation(if not 0)\n (*) 1 if screenshot; 2 if open website; else nothing', title='Input Data', default="your's input")
    f = open('settings.txt', "a", encoding='utf-8', errors='replace')
    if type(text)==str:
        if len(text)!=0 and text[0] in '123456789' and text!="your's input":
            f.write(','+text)
        elif len(text)!=0 and text[0] not in '123456789' and text!="your's input":
            f.write(', '+text)
        f.close()
        settings_do=reading_settings()


porcupine=None
pas_stream=None
p=None

count_scr=1
settings_do=reading_settings()
model = Model(reading_model())
rec = KaldiRecognizer(model, 16000)

play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Доброе утро", "Джарвис - приветствие"])}.wav'))

try:
    porcupine=pvporcupine.create(keywords=['jarvis', 'computer'])
    p = pyaudio.PyAudio()
    pas_stream = p.open(format=pyaudio.paInt16, channels=1, rate=porcupine.sample_rate, input=True, input_device_index=0, frames_per_buffer=porcupine.frame_length)
    while True:
        mon_bet()

        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('d'):
            adding(settings_do)

        pcm = pas_stream.read(porcupine.frame_length)
        pcm= struct.unpack_from("h"*porcupine.frame_length, pcm)

        keyword_index=porcupine.process(pcm)
        
        if keyword_index>=0:
            play(AudioSegment.from_wav("C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Да сэр.wav"))
            print("Ключевое слово распознанно, Джарвис активирован")
            stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, input_device_index=0, frames_per_buffer=8000)
            stream.start_stream()
            start=time.time()
            while True:
                data = stream.read(8000)
                if rec.AcceptWaveform(data):
                    res=json.loads(rec.FinalResult())
                    if fuzz.partial_ratio("конец", res["text"])>=70:
                        play(AudioSegment.from_wav("C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Отключаю питание.wav"))
                        stream.close()
                        print("Вы остановили Джарвиса, жду ключевое слово")
                        break
                    if len(res["text"])!=0:
                        user_set_do(settings_do, res, count_scr)
                if time.time()-start>30:
                    print("Джарвис уснул, дабы его разбудить, назовите его имя")
                    break
finally:
    if porcupine is not None:
        porcupine.delete()
    if pas_stream is not None:
        pas_stream.close()
    if p is not None:
        p.terminate()

    
''' if fuzz.partial_ratio("вверх", res["text"])>=90:
        dig = analis_of_digits(res)
        pg.scroll(dig)
    if fuzz.partial_ratio("вниз", res["text"])>=90:
        dig = analis_of_digits(res)
        pg.scroll(int(dig)*-1)'''

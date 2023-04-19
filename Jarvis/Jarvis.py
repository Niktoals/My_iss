from vosk import Model, KaldiRecognizer
import pyaudio
import os
import json
import pyautogui
import keyboard
from time import sleep
from fuzzywuzzy import fuzz
import random
from pydub import AudioSegment
from pydub.playback import play
import psutil
import webbrowser 


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

model = Model("C:/Users/1/Desktop/Progs/Py/model_small")
rec = KaldiRecognizer(model, 16000)

if not os.path.exists("photos"):
    os.mkdir("photos")

def mon_bet():
    battery = psutil.sensors_battery()
    plug=battery.power_plugged
    if battery.percent==2 and plug==False:
        play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/2 %.wav'))
    elif battery.percent==7 and plug==False:
        play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/7 %.wav'))
    elif battery.percent==11 and plug==False:
        play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/11 %.wav'))
    elif battery.percent==13 and plug==False:
        play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/Энергия 13%.wav'))
    elif battery.percent==15 and plug==False:
        play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/Энергия 15 %.wav'))
    elif battery.percent==19 and plug==False:
        play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/Сэр, энергия 19 %.wav'))
    elif battery.percent==48 and plug==False:
        play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/Заряд батареи, %/Энергия 48% и падает сэр.wav'))
        
def user_set_do(settings_do, res, count_scr):
    for key in settings_do.keys():
        if fuzz.partial_ratio(key[1::], res["text"])>=90 and key[0] in "123456789":
            play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Да сэр", "Загружаю сэр", "Есть", "Как пожелаете ", "К вашим услугам сэр", "Запрос выполнен сэр", "Образ создан"])}.wav'))
            if key[0]=='1':
                screen=pyautogui.screenshot()
                screen.save(f"photos/screen{count_scr}.png")
                count_scr+=1
            if key[0]=='2':
                fPath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
                id_key=res["text"].find(key[1::])
                print(res["text"][id_key+6::])
                webbrowser.get(fPath).open("https://www.google.com/search?q=" + res["text"][id_key+6::])

        if fuzz.partial_ratio(key[1::], res["text"])>=90 and key[0]==' ':
            play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Да сэр", "Загружаю сэр", "Есть", "Как пожелаете ", "К вашим услугам сэр", "Запрос выполнен сэр", "Образ создан"])}.wav'))
            os.startfile(settings_do[key])

def reading():
    f = open('Py/settings.txt', encoding='utf-8', errors='replace')
    d=[n for n in f.read().split(",")]
    settings_do={}
    for i in range(1, len(d), 2):
        settings_do[d[i-1]]=d[i]
    f.close()
    return settings_do

count_scr=1
settings_do=reading()

play(AudioSegment.from_wav(f'Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Доброе утро", "Джарвис - приветствие"])}.wav'))
while True:
    mon_bet()
    data = stream.read(8000)
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('d'):
        text=pyautogui.prompt(text='"*"keyword,operation(if not 0)\n (*) 1 if screenshot; 2 if open website; else nothing', title='Input Data', default='')
        f = open('Py/settings.txt', "a", encoding='utf-8', errors='replace')
        if len(text)!=0 and text[0] in '123456789':
            f.write(','+text)
        elif len(text)!=0 and text[0] not in '123456789':
            f.write(', '+text)
        f.close()
        settings_do=reading()
    if rec.AcceptWaveform(data):
        res=json.loads(rec.FinalResult())
        if fuzz.partial_ratio("конец", res["text"])>=70:
            play(AudioSegment.from_wav("Jarvis Sound Pack от Jarvis Desktop/Отключаю питание.wav"))
            break
        if len(res["text"])!=0:
            user_set_do(settings_do, res, count_scr)
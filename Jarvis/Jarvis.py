from vosk import Model, KaldiRecognizer
import pyaudio
import os
import json
import pyautogui as pg
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
        
def activating(res):
    if not os.path.exists('settings'):
        os.mkdir('settings')
    else:
        if len(os.listdir('settings'))!=0:
            for filename in os.listdir('settings'):
                if fuzz.partial_ratio(res, filename[:filename.rfind('.'):])>=70:
                    return filename
        else:
            print('Добавте ссылки на приложения в папку, пока что папка пуста...')

def user_set_do(res, count_scr):
    if fuzz.partial_ratio("пауза", res["text"][6::])>=90:
        pg.press('space')
        
    if fuzz.partial_ratio('скрин', res["text"])>=80:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Да сэр", "Загружаю сэр", "Есть", "Как пожелаете ", "К вашим услугам сэр", "Запрос выполнен сэр", "Образ создан"])}.wav'))
        screen=pg.screenshot()
        if not os.path.exists("photos"):
            os.mkdir("photos")
        screen.save(f"photos/screen{count_scr}.png")
        count_scr+=1

    if fuzz.partial_ratio('найди', res["text"])>=90:
        play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Да сэр", "Загружаю сэр", "Есть", "Как пожелаете ", "К вашим услугам сэр", "Запрос выполнен сэр", "Образ создан"])}.wav'))
        fPath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(fPath).open("https://www.google.com/search?q=" + res["text"][res['text'].find('найди')+6::])

    if fuzz.partial_ratio('запусти', res["text"])>=90:
        filename=activating(res["text"][res['text'].find('запусти')+8::])
        print(filename)
        try:
            os.startfile(f'C:/Users/1/Desktop/Progs/settings/{filename}')
        except Exception:
            print('Не найдено приложения в папке')


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

porcupine=None
pas_stream=None
p=None

count_scr=1
model = Model(reading_model())
rec = KaldiRecognizer(model, 16000)

play(AudioSegment.from_wav(f'C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/{random.choice(["Доброе утро", "Джарвис - приветствие"])}.wav'))

try:
    porcupine=pvporcupine.create(keywords=['jarvis', 'computer'])
    p = pyaudio.PyAudio()
    pas_stream = p.open(format=pyaudio.paInt16, channels=1, rate=porcupine.sample_rate, input=True, input_device_index=0, frames_per_buffer=porcupine.frame_length)
    while True:
        mon_bet()

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
                    print(res)
                    if fuzz.partial_ratio("конец", res["text"])>=70:
                        play(AudioSegment.from_wav("C:/Users/1/Desktop/Progs/Jarvis Sound Pack от Jarvis Desktop/Отключаю питание.wav"))
                        stream.close()
                        print("Вы остановили Джарвиса, жду ключевое слово")
                        break
                    if len(res["text"])!=0:
                        user_set_do(res, count_scr)
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

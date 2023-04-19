'''from gtts import gTTS
import os

text = input()
speech = gTTS(text=text, lang='ru', slow=False)
text="_".join(text.split(' '))
url=text+".mp3"
if not os.path.exists(url):
    speech.save(url)
os.system(url)'''


#output
import torch
import sounddevice as sd
import time
import Rec

language = 'ru'
model_id='ru_v3'
device = torch.device('cpu') # cpu or gpu

model, _= torch.hub.load(repo_or_dir='snakers4/silero-models',
                         model='silero_tts',
                         language=language,
                         speaker=model_id)

model.to(device)

while True:
    sample_rate=8000
    audio=model.apply_tts(text=Rec.record(),
                    speaker='baya', # aidar, baya. kseniya, xenia, random
                    sample_rate=sample_rate)
    sd.play(audio, sample_rate)
    time.sleep(len(audio)/sample_rate)
    sd.stop()


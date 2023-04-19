from vosk import Model, KaldiRecognizer
import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

model = Model("Py\model_small")
rec = KaldiRecognizer(model, 16000)

while True:
    data = stream.read(8000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())

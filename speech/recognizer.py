#test microphone
#vosk


#
"""

!!!!!!!!!!!!!!!!!!!!!!!
THIS IS DUPLICATE UNUSED CODE!!!!


"""



"""
import sys
import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer


from core.utils import recognition_enabled

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# Load model folder you unzipped
model = Model("vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)  # 16k sample rate

with sd.RawInputStream(samplerate=16000, blocksize=8000,
                       dtype='int16', channels=1, callback=callback):

    while True:
        data = q.get()
        if not recognition_enabled:
            print('lalala im not listening...')
            continue
        if recognizer.AcceptWaveform(data):
            print('im an idiot')
            print('full: ',json.loads(recognizer.Result())["text"])
        else:
            print(json.loads(recognizer.PartialResult())["partial"])


"""
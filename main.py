import tinytuya
import time
import random
import pyaudio
import numpy as np


d = tinytuya.BulbDevice('bfe52bc5274f152226spas', '192.168.0.87', 'ac4fc9f0967e454d', 'device22')
d.set_dpsUsed({"1": None})
d.set_version(3.3) 
d.set_socketPersistent(True)
d.set_socketNODELAY(False)


CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

for i in range(int(10*44100/1024)):
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    size = int(50*peak/2**16)
    bars="#"*size
    if size > 100:
        size = 100
    d.set_brightness_percentage(size)
    print(bars)

stream.stop_stream()
stream.close()
p.terminate()
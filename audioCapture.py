import pyaudio
import numpy as np
import math
import time
def get_noise_level():
    CHUNK=1024
    FORMAT=pyaudio.paInt16
    CHANNELS=1
    RATE=44100
    audio= pyaudio.PyAudio()
    stream=audio.open(rate=RATE,channels=CHANNELS,format=FORMAT,input=True,frames_per_buffer=CHUNK)
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    rms = np.sqrt(np.mean(data**2))
    db = 20 * np.log10(rms) if rms > 0 else -np.inf
    return db
import pyaudio
import wave
from datetime import datetime
import numpy as np  

path="C:\\Users\\ZN\\Desktop\\Wava test\\ReadFile"
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 10#聲音紀錄的最小長度
LEVEL = 1500#聲音保存的閥值
COUNT_NUM = 20#NUM_SAMPLES個取樣之内出现COUNT_NUMLEVEL的取樣則紀錄聲音
WAVE_OUTPUT_FILENAME = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+ ".wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

print("* recording")
save_count = 0 
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    audio_data = np.frombuffer(data, dtype=np.short)
    large_sample_count = np.sum( audio_data > LEVEL ) 
    print(np.max(audio_data))
    if large_sample_count > COUNT_NUM: 
        save_count = RECORD_SECONDS
    else: 
        save_count -= 1 

    if save_count < 0: 
        save_count = 0 

    if save_count > 0:
        frames.append(data)

print("Recode a piece of  voice successfully!")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(path+"\\"+WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
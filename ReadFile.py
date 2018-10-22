import wave as we
import numpy as np
import matplotlib.pyplot as plt

#打開檔案
wavefile=we.open("output.wav","r")

params=wavefile.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(params)

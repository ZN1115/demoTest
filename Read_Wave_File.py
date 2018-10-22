import wave as we
import numpy as np
import matplotlib.pyplot as plt

#打開檔案
wavefile=we.open("2018-10-22_10_30_37.wav","rb")


#讀取這首wave的資訊
#內容有這些(nchannels, sampwidth, framerate, nframes, comptype, compname)
#分別為聲道數，量化位數(byte)，採樣頻率，採樣點數，壓縮類型，壓縮類型描述
params=wavefile.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(params)


#轉成二進位 readframes
datawav=wavefile.readframes(nframes)
wavefile.close()


#將字串轉換成陣列
datause=np.frombuffer(datawav,dtype=np.short)

#LRLRLRLR
datause.shape=-1,2
datause=datause.T
time=np.arange(0,nframes)*(1.0/framerate)#採樣時間

##畫圖
plt.title("wave frames")
plt.subplot(211)
plt.plot(time,datause[0],color = 'green')
plt.subplot(212)
plt.plot(time, datause[1])
plt.show()


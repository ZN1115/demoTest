import wave as we
import numpy as np
import matplotlib.pyplot as plt
import os

filepath = "./ReadFile/" #存放音檔的路徑
filename= os.listdir(filepath) #資料夾下的所有檔案 
num=0
for file in range(len(filename)):
    print(num+1, end=" ")
    num+=1
    print(filename[file])
name = input('請輸入檔名：')
print('---------聲音資訊------------')

#打開檔案
wavefile=we.open(filepath+filename[int(name)-1],"rb")
wavefile2=we.open("./ReadFile/2018-11-12_10_35_00.wav","rb")


#讀取這首wave的資訊
#內容有這些(nchannels, sampwidth, framerate, nframes, comptype, compname)
#分別為聲道數，量化位數(byte)，採樣頻率，採樣點數，壓縮類型，壓縮類型描述
params=wavefile.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
params2=wavefile2.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
print(params)



#轉成二進位 readframes
datawav=wavefile.readframes(nframes)
wavefile.close()
datawav2=wavefile2.readframes(nframes)
wavefile2.close()


#將字串轉換成陣列
datause=np.frombuffer(datawav,dtype=np.short)
datause2=np.frombuffer(datawav2,dtype=np.short)

print("datause長度",end="")
print(len(datause))
print(datause)
# =============================================================================
# for i in range(len(datause)):
#     avg+=datause[i]
#     print('avg: ',avg)
# =============================================================================

#LRLRLRLR
datause.shape=-1,2
datause=datause.T
time=np.arange(0,nframes)*(1/framerate)#採樣時間
datause2.shape=-1,2
datause2=datause2.T
time2=np.arange(0,nframes)*(1/framerate)#採樣時間

##畫圖
plt.title(filename[int(name)-1])
#plt.subplot(211)
plt.plot(time,datause[0],'r--')
# =============================================================================
# plt.subplot(212)
# plt.plot(time, datause[1])
# plt.show()
# =============================================================================

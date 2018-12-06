import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.fftpack import dct
from scipy.io import wavfile # get the api
import numpy as np
from scipy import signal
import math
import pyaudio
import wave
import time
import os
import wave as we
#buf=[]
def readfile():
    filepath = "./ReadFile/" #存放音檔的路徑
    filename= os.listdir(filepath) #資料夾下的所有檔案 
    num=0
    for file in range(len(filename)):
        print(num+1, end=" ")
        num+=1
        print(filename[file])
    name = input('請輸入檔名：')
    return filepath+filename[int(name)-1]
    
    print('---------聲音資訊------------') 
#讀入單一檔案測試
def init():
    filename=readfile()
    fs, data = wavfile.read(filename) # load the data
    b=[(ele/2**16.) for ele in data]# this is 16-bit track, b is now normalized on [-1,1)
    c = fft(b) # calculate fourier transform (complex numbers list)
    d = len(c)//2  # you only need half of the fft list (real signal symmetry)
    
    wavefile=we.open(filename,"rb")
    params=wavefile.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    
    time=np.arange(0,nframes)*(1/framerate)#採樣時間
    plt.subplot(2,2,1)
    plt.plot(time,b,'b')
    plt.title('Original wave')
    
    
    xf=np.arange(len(c))
    xf2 = xf[range(int(len(time-1)/2))]
    
    plt.subplot(2,2,3)
    plt.plot(xf2,abs(c[:(d)]),'b')
    plt.title('fft') 
    
    plt.subplot(2,2,2)
    plt.plot(xf,c,'b')
    plt.title('fft') 
    
    e=dct(b)
    plt.subplot(2,2,4)
    plt.plot(e,'b')
    plt.title('fft') 
    
    
    
    
    
    plt.show()
    return fs, b    #取樣率 data



#轉成頻域
def fft_domyself(b, fs, plotshow=None):
    global ftmap
    #set value
    one_second_block_num = 21*2                   #one second 擷取次數
    second = len(b)/44100
    second_len = int(one_second_block_num*second)
    fft_num = int(fs/one_second_block_num)        #one second 間格點數 #2100
    ftmap = np.zeros((int(fft_num/2),second_len)) #建立fft陣列的圖片大小  
    startime = 0#362000
 
    #轉成fft 並儲存在fft陣列
    for i in range(0,second_len):
        endtime = startime + fft_num
        ffttemp = abs(fft(b[startime:endtime]))
        ftmap[0:fft_num,i] = ffttemp[0:int(len(ffttemp)/2)]
        startime = endtime
 
    #做20log()
    for i in range(0, len(ftmap[:,1])):
        for j in range(0, len(ftmap[1,:])):
            try:
                #ftmap[i,j] = 20*math.log10(ftmap[i,j])
                ftmap[i,j] = 20*math.log(ftmap[i,j], 10)
            except:
                #由於 log(0) 輸入0會error
                print('log error with ftmap: ', ftmap[i,j])
        
    ftmap = ftmap + abs(np.min(ftmap))  
    lineft = np.median(ftmap, axis=1)   #用二維的方式，查看頻域的整體資料情況
    
    if plotshow:
        if plotshow == 'linefft':
            plt.plot(lineft, 'b')
            plt.show()
        else:
            
            plt.plot(lineft,'g') 
            plt.show()
            plt.imshow(ftmap)
            plt.xlabel('Frequency [Hz]')
            plt.ylabel('Time [sec]')
            plt.colorbar()
            plt.show()
     
    return ftmap, lineft
 
#使用內建的function將聲音轉成頻域
def spectrogram_(b, fs, plotshow=None):
    #x1 = np.array(b, dtype = float)
    f, t, Sxx = signal.spectrogram(b, fs)    #output 時頻譜
    
    for i in range(0, len(Sxx[:,1])):
        for j in range(0, len(Sxx[1,:])):
            Sxx[i,j] = 20*math.log10(Sxx[i,j])
            #print('do')
    Sxx = Sxx + abs(np.min(Sxx))
    
    if plotshow: 
        plt.pcolormesh(t, f, Sxx)             #draw 時頻譜
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.colorbar()
        plt.show()
    return Sxx
if __name__ == '__main__':
    
    fs, b = init()
    #fftmap = fft_domyself(b, fs, plotshow = True)   #自己做的
    #sx = spectrogram_(b, fs, plotshow = True)       #內建function
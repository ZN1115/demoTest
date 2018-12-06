import os
import numpy as np

filepath = "./ReadFile/" #存放音檔的路徑
filename= os.listdir(filepath) #資料夾下的所有檔案 
num=0
for file in range(len(filename)):
    print(num+1, end=" ")
    num+=1
    print(filename[file])
name = input('請輸入檔名：')


f = open(filepath+filename[int(name)-1],"rb")
f.seek(0)
f.read(44)
data = np.fromfile(f, dtype=np.int16)
# =============================================================================
# data.tofile("test.pcm")
# =============================================================================

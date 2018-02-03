from function.CompressioneFrammenti import comprimi_frammenti
from function.EstrazioneFrammenti import *
from function.EstrazioneMaschere import estrazione_maschere
from function.UnioneFrammenti import merge
from function.jpeg import jpeg_comrpess
from function.statistic import statistic

felzenszwalb=1
slic=0;


filenameIntoImgInput='delta.bmp'
arr=[15,16,17,18,19,20,21,22,23,25,26,27]
frammentiImpo="frammento"+str(arr[0])+".bmp";
arr.pop(0);

for i in arr:
    frammentiImpo=frammentiImpo+",frammento"+str(i)+".bmp"



forground = 100
background = 89
qulityJpegDicect=78
algoritmoSegmentation=felzenszwalb


#uguale compression data 100 88 76 quasi uguale psnr
'''
print("estrazione maschere in corso...................")

estrazione_maschere(filenameIntoImgInput,algoritmoSegmentation,n_segments=120);
print("end")
print("ottengo frammenti a colori...................")
estrazioneframmentiAcolori(filenameIntoImgInput)
print("end")
print("comprimo...................")


#mergewithoutCompression(filenameIntoImgInput)

'''
comprimi_frammenti(frammentiImpo,forground,background);

merge();


jpeg_comrpess("ImgInput\\"+filenameIntoImgInput,"RESULT\\jpegDirect\\result.jpeg ",qulityJpegDicect);


statistic(filenameIntoImgInput)

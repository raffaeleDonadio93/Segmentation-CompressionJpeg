from function.CompressioneFrammenti import comprimi_frammenti
from function.EstrazioneFrammenti import *
from function.EstrazioneMaschere import estrazione_maschere
from function.UnioneFrammenti import merge
from function.jpegNostro import jpeg_compress
from function.statistic import statistic

dirs=['Frammenti','Compressi',"Maschere","test3Divide","RESULT","RESULT\\jpegDirect"]

for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)

felzenszwalb=1
slic=0;

filenameIntoImgInput='AstronautaB&W.bmp'
arr=[1]
frammentiImpo="frammento"+str(arr[0])+".bmp";
arr.pop(0);

for i in arr:
    frammentiImpo=frammentiImpo+",frammento"+str(i)+".bmp"

forground = 100
background = 89
qulityJpegDicect=78
algoritmoSegmentation=felzenszwalb


#uguale compression data 100 88 76 quasi uguale psnr

print("estrazione maschere in corso...................")

estrazione_maschere(filenameIntoImgInput,algoritmoSegmentation,n_segments=120);
print("end")
print("ottengo frammenti a colori...................")
estrazioneframmentiAcolori(filenameIntoImgInput)
print("end")
print("comprimo...................")

comprimi_frammenti(frammentiImpo,forground,background);

merge();

jpeg_compress("ImgInput\\" + filenameIntoImgInput, "RESULT\\jpegDirect\\result.jpeg ", qulityJpegDicect);

statistic(filenameIntoImgInput)

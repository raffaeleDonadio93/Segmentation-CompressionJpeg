import numpy as np
import matplotlib.image as mpimg
import scipy.misc
import os

def setcolor(img, mask,longPath):
    maskAmplified = np.zeros(img.shape, dtype=img.dtype)
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if(mask[i][j]==255):
                maskAmplified[i][j]=img[i][j]
    scipy.misc.toimage(maskAmplified).save(longPath)

def estrazioneframmentiAcolori(fileNameImgOriginale):
    lista = []
    for file in os.listdir("Maschere"):
        lista.append(file)
    img = mpimg.imread('ImgInput/'+fileNameImgOriginale)
    i=0
    for s in lista:
        mask = mpimg.imread('Maschere/' + s);
        setcolor(img, mask, 'Frammenti/' + s)
        print("estrazione a colore frammento:"+str(i))
        i+=1



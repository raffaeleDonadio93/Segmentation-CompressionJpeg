from __future__ import print_function

import numpy as np
import os
import scipy.misc
from function.jpegNostro import jpeg_compress
import skimage.measure as sky
from skimage.segmentation import felzenszwalb, slic, mark_boundaries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def compare(path1,path2,original):

    noriginale=os.path.getsize(original);
    npath1 = os.path.getsize(path1);
    npath2 = os.path.getsize(path2)

    Ioriginal= mpimg.imread(original)
    Ipath1=mpimg.imread(path1)
    Ipath2=mpimg.imread(path2)

    psnr1= sky.compare_psnr(Ioriginal, Ipath1)
    print("PATH1 c.r:"+str(noriginale/npath1)+":1    psnr:"+str(psnr1));
    psnr2= sky.compare_psnr(Ioriginal,Ipath2)
    print("PATH2 c.r :"+str(noriginale/npath2)+":1     psnr:"+str(psnr2));
#nome del file nella cartella ImgInput
def dividi3(fileName):
    img = mpimg.imread(fileName)
    pezzo1=np.zeros([int(img.shape[0]/3),img.shape[1],img.shape[2]], dtype=img.dtype)
    pezzo2=np.zeros([int(img.shape[0]/3),img.shape[1],img.shape[2]], dtype=img.dtype)
    pezzo3=np.zeros([int(img.shape[0]/3),img.shape[1],img.shape[2]], dtype=img.dtype)

    for i in range(img.shape[0]):
        for j in range((img.shape[1])):
            if i<img.shape[0]/3:
                pezzo1[i][j]=img[i][j]
            else :
                if i< img.shape[0]/3*2:
                    pezzo2[i-int(img.shape[0]/3)][j] = img[i][j]
                else:
                    pezzo3[i-(int(img.shape[0]/3)*2)][j] = img[i][j]
    return [pezzo1,pezzo2,pezzo3]
def dividiAndSave(fileName):
    appoggio=dividi3('ImgInput/'+fileName)
    scipy.misc.toimage(appoggio[0]).save(pathinitial+'1.bmp')
    scipy.misc.toimage(appoggio[1]).save(pathinitial+'2.bmp')
    scipy.misc.toimage(appoggio[2]).save(pathinitial+'3.bmp')

pathinitial='test3Divide\\Pezzo'
quality=50
dividiAndSave("honda3.bmp")
img = mpimg.imread(pathinitial+'1.bmp')
print(img.shape[:2])
jpeg_compress(pathinitial + '1.bmp', pathinitial + '1.jpg', quality)
jpeg_compress('ImgInput\\honda3.bmp', 'test3Divide\\honda3Direct.jpg', quality)
pezzoJpeg=dividi3("test3Divide\\honda3Direct.jpg")[0]
print(pezzoJpeg.shape[:2]);
scipy.misc.toimage(pezzoJpeg).save("test3Divide\\pezzojpeg.jpg")
#pezzoInfra=dividi3("test3Divide\\honda3INFRA.jpg")[0]
#scipy.misc.toimage(pezzoInfra).save("test3Divide\\pezzoinfra.jpg")

compare('test3Divide\\Pezzo1.jpg',"test3Divide\\pezzojpeg.jpg","test3Divide\\Pezzo1.bmp")

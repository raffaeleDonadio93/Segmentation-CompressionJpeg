import os
import scipy.misc
from function.UnioneFrammenti import *
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
def merge(pathResult='RESULT/result.jpeg',dirMerge="Compressi",firstFragmentName='frammento0.bmp'):

    lista = []

    for file in os.listdir(dirMerge):
        lista.append(file)
        #print(file);

    print("-----------------------------------------")

    fr0 = mpimg.imread(dirMerge+'/'+firstFragmentName);
    unione = np.zeros(fr0.shape, dtype=fr0.dtype)

    lista=[]
    for file in os.listdir(dirMerge):
        lista.append(file)


    for f in lista:
        frtemp = mpimg.imread(dirMerge+'/' + f)

        for i in range(frtemp.shape[0]):
            unione[i]=unione[i]+frtemp[i];
    scipy.misc.toimage(unione).save(pathResult)
    plt.imshow(unione)
    plt.show()




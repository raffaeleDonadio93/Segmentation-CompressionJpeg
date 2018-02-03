import os
import scipy.misc
from function.UnioneFrammenti import *
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
def merge(pathResult='RESULT/result.jpeg',dirMerge="Compressi"):

    lista = []
    for file in os.listdir(dirMerge):
        lista.append(file)

    fr0 = mpimg.imread(dirMerge+'/'+lista.pop())
    unione = np.zeros(fr0.shape, dtype=fr0.dtype)

    for f in lista:
        frtemp = mpimg.imread(dirMerge+'/' + f)

        for i in range(frtemp.shape[0]):
            unione[i]=unione[i]+frtemp[i]

    scipy.misc.toimage(unione).save(pathResult)
    plt.imshow(unione)
    plt.show()




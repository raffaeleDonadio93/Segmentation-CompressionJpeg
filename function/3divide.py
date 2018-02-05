from __future__ import print_function

import numpy as np
import os
import scipy.misc
from skimage.segmentation import felzenszwalb, slic, mark_boundaries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#nome del file nella cartella ImgInput
def dividi3(fileName):
    img = mpimg.imread('../ImgInput/'+fileName)
    r1= os.path.getsize('../ImgInput/' + fileName);
    pezzo1=np.zeros(img.shape, dtype=img.dtype)
    pezzo2=np.zeros(img.shape, dtype=img.dtype)
    pezzo3=np.zeros(img.shape, dtype=img.dtype)
    for i in range(img.shape[0]):
        for j in range((img.shape[1])):
            if i<=img.shape[0]/3:
                pezzo1[i][j]=img[i][j]
            else :
                if i<= img.shape[0]/3*2:
                    pezzo2[i][j] = img[i][j]
                else:
                    pezzo3[i][j] = img[i][j]
    #scipy.misc.toimage(p).save('Maschere\\frammento' + str(k) + '.bmp')
    plt.imshow(pezzo1)
    plt.show()
    plt.imshow(pezzo2)
    plt.show()
    plt.imshow(pezzo3)
    plt.show()

dividi3("delta.bmp")
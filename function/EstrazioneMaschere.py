from __future__ import print_function

import numpy as np
import scipy.misc
from skimage.segmentation import felzenszwalb, slic, mark_boundaries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#nome del file nella cartella ImgInput
def estrazione_maschere(fileName,value,n_segments=40,scale=2000):
    img = mpimg.imread('ImgInput/'+fileName)
    if(value==1):
        segments_fz = felzenszwalb(img,scale , sigma=0.5, min_size=50)
        print("Felzenszwalb number of segments: {}".format(len(np.unique(segments_fz))))
        scipy.misc.toimage(mark_boundaries(img, segments_fz)).save('RESULT/segmentation.bmp')
    else:
        segments_fz= slic(img,n_segments , compactness=10, sigma=1)
        scipy.misc.toimage(mark_boundaries(img, segments_fz)).save('RESULT/segmentation.bmp')

        print("Slic number of segments: {}".format(len(np.unique(segments_fz))))

    k = 0
    # loop over the unique segment values
    for (i, segVal) in enumerate(np.unique(segments_fz)):
        # construct a mask for the segment
        # Return a new array of given shape and type, filled with zeros.
        # img.shape ritorna le dimensioni della matrice, usando :2 ritorna le due prime dimensionsi
        mask = np.zeros(img.shape[:2], dtype="uint8")
        mask[segments_fz == segVal] = 255
        scipy.misc.toimage(mask).save('Maschere/frammento' + str(k) + '.bmp')
        k = k + 1

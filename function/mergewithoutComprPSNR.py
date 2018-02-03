import os
import skimage.measure as sky
import matplotlib.image as mpimg

from function.UnioneFrammenti import merge


def mergewithoutCompression(filenameIntoImgInput,pathResult='RESULT/merge/withoutCompression/result.bmp'):
    merge(pathResult,dirMerge="Frammenti",firstFragmentName='frammento0.bmp')
    input = mpimg.imread('ImgInput\\' + filenameIntoImgInput)
    merged = mpimg.imread(pathResult)
    psnr1 = sky.compare_psnr(input, merged)
    print("max PSNR"  + str(psnr1));


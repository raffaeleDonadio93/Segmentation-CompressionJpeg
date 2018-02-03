import os
import skimage.measure as sky
import matplotlib.image as mpimg


def statistic(inputFilenameImg):
    imgINPUT=os.path.getsize("ImgInput/"+inputFilenameImg);

    r1=os.path.getsize("RESULT/result.jpeg");
    r2=os.path.getsize("RESULT/jpegDirect/result.jpeg")




    input= mpimg.imread('ImgInput\\'+inputFilenameImg)
    custom=mpimg.imread('RESULT/result.jpeg')
    direct=mpimg.imread('RESULT/jpegDirect/result.jpeg')

    psnr1= sky.compare_psnr(input,custom)
    print("CUSTOM c.r:"+str(imgINPUT/r1)+":1    psnr:"+str(psnr1));
    psnr2= sky.compare_psnr(input,direct)
    print("JPEG c.r :"+str(imgINPUT/r2)+":1     psnr:"+str(psnr2));


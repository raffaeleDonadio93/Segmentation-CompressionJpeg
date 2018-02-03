import os




for file in os.listdir("Compressi"):
    os.remove("Compressi\\" + file)
for file in os.listdir("Frammenti"):
        os.remove("Frammenti\\" + file)
for file in os.listdir("Maschere"):
        os.remove("Maschere\\" + file)

os.remove("RESULT\\result.jpeg")
os.remove("RESULT\\jpegDirect\\result.jpeg")
os.remove("RESULT\\segmentation.bmp")
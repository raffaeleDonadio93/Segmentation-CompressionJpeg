import os




for file in os.listdir("Compressi"):
    path="Compressi\\" + file
    if (os.path.exists(path)):
        os.remove(path)
for file in os.listdir("Frammenti"):
    path = "Frammenti\\" + file
    if (os.path.exists(path)):
        os.remove(path)
for file in os.listdir("Maschere"):
    path="Maschere\\" + file
    if(os.path.exists(path)):
        os.remove(path)

results=["RESULT\\result.jpeg","RESULT\\jpegDirect\\result.jpeg","RESULT\\segmentation.bmp"]
for r in results:
    if(os.path.exists(r)):
        os.remove(r)

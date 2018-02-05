import os,sys
import matplotlib.image as mpimg
import scipy.misc
from function.jpegNostro import jpeg_compress

def comprimi_frammenti(fram,forground,background):

    frammentiImportanti = fram.split(",")

    lista = []
    prova=os.listdir()
    for file in os.listdir("Frammenti"):
        lista.append(file)

    for s in lista:
        if s in frammentiImportanti:
            jpeg_compress("Frammenti\\" + s, "Compressi\\" + s, forground)
        else:
            jpeg_compress("Frammenti\\" + s, "Compressi\\" + s, background)
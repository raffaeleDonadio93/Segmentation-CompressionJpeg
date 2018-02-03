import os,sys
import matplotlib.image as mpimg
import scipy.misc
from function.jpeg import jpeg_comrpess
def usage():
    print("Come paramentro di imput mi serve una stringa in questo formato\n nomefile,altrofile,altrofile\nquesti verranno compressi con una perdita minore")
    sys.exit(1)

def comprimi_frammenti(fram,forground,background):

    ''' if len(sys.argv) != 2:
        usage()
        if (type(sys.argv[1])!= list):
            usage()''''''
    '''
    frammentiImportanti = fram.split(",")

    lista = []
    prova=os.listdir()
    for file in os.listdir("Frammenti"):
        lista.append(file)

    for s in lista:
        #params= 'java -classpath jj2000-5.1.jar JJ2KEncoder -i Frammenti\\'+s+' -o Compressi\\'+s.replace("ppm","ppm")+' -rate '
        if s in frammentiImportanti:
            print("fore:"+s);
            jpeg_comrpess("Frammenti\\"+s,"Compressi\\"+s,forground)
            #params=params + str(forground)
            #(params)
            #os.system(params)
        else:
            '''params = params + str(background)
            print(params)
            os.system(params)'''
            print("back:"+s);
            jpeg_comrpess("Frammenti\\" + s, "Compressi\\" + s, background)
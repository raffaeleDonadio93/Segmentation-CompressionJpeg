from PIL import Image

def jpeg_comrpess(pathImgInput,output,quality):
	
    prova= Image.open(pathImgInput)
    file = open(output, "w")
    prova.save(file.buffer, "JPEG", quality=quality)




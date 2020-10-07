# KEEP ALL FILES IN FOLDER ALONG WITH THIS CODE.
import os
from PIL import Image

if not os.path.exists('compressed'):
    os.makedirs('compressed')

def resize1024(currentsize):
	# preserves aspect ratio
	x,y= currentsize
	if x>1024:
		y= int(y*(1024/x))
		x=1024
	return x,y

JPG_PNG_LIST=[x for x in os.listdir() if 'png' in x or 'jpg' in x]

print(JPG_PNG_LIST)

for x in JPG_PNG_LIST:
	currentImg=Image.open(x).convert('RGB')
	currentImg=currentImg.resize(resize1024(currentImg.size),Image.ANTIALIAS)
	currentImg=currentImg.save('./compressed/'+x,quality=95,optimize=True)
	# size=currentImg.size
	# print(size)
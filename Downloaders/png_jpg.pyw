from PIL import Image
import os

for x in [x for x in os.listdir() if x.endswith('png')]:
	Image.open(x).save(x.replace('.png','.jpg'))
	print('saving ',x)
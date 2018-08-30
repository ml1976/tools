# keep this file in the same folder as images are
# converting from .png to .jpg

import glob
from PIL import Image
import os

count = 1

for filename in glob.glob('*.png'):
	im = Image.open(filename)
	rgb_im = im.convert('RGB')
	rgb_im.save("{0:03}".format(count) + '.jpg')
	count += 1
	os.remove(filename) # this will remove .png file one by one, each time it loops
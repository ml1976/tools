# put this file in the same folder as images, removes portrait images

from PIL import Image
import glob
import os

for filename in glob.glob('*.jpg'): #assuming jpg
	#print(filename)
	#file, ext = os.path.splitext(filename)
	image=Image.open(filename)
	width, height = image.size
	image.close()				#close the file before removing, if not you get an error
	if (height>width):
		#print(filename)
		os.remove(filename) # removes images smaller than size requested
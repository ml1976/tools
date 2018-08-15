# place this file in the same folder where images are, and run it


from PIL import Image
import glob
import os

maxsize = (1080, 720)

for filename in glob.glob('*.jpg'): #assuming jpg
	print(filename)
	file, ext = os.path.splitext(filename)
	image=Image.open(filename)
	'''
	for orientation in ExifTags.TAGS.keys():
		if ExifTags.TAGS[orientation]=='Orientation':
			break
	exif=dict(image._getexif().items())
	if exif[orientation] == 3:
		image=image.rotate(180, expand=True)
	elif exif[orientation] == 6:
		image=image.rotate(270, expand=True)
	elif exif[orientation] == 8:
		image=image.rotate(90, expand=True)
'''
	image.thumbnail(maxsize, Image.ANTIALIAS)
	image.save(file + ".jpg", "JPEG")

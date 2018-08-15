# make sure your images are placed in Images folder and let this file
# be outside of that folder, and then run the file

from PIL import Image
import os
from os import walk, getcwd
import datetime

wd = os.getcwd()
wd
	
folder = 'Images'
i = 13 # pick a new number for 'i' every time you plan renaming images
count = 1
for filename in os.listdir(folder):	
	names = filename.split('.')    
	if (names[-1].lower() == 'jpg'):
		newname = str(i) + '_' + "{0:03}".format(count) + '_' + str(datetime.date.today()) + '.jpg'      
		#newname = "{0:01}".format(count) + '.mp4' # + '_' + str(datetime.date.today()) + '.jpg'
		print(newname)
		count += 1
		infilename = os.path.join(folder, filename)
		print(infilename)
		newinfilename = os.path.join(folder, newname)
		print(newinfilename)
		output = os.rename(infilename, newinfilename)
    #else:
    	#print("There might exist images with extension different that .jpg, .jpeg, .png! Please check your images!")
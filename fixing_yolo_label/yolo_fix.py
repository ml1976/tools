# fixing yolo class label from 0 to 1

import cv2
import os
import sys

#listOfFiles = os.listdir('Yolo-Labels')
#print(listOfFiles)

for filename in os.listdir('Yolo-Labels'):
    print(filename)

    txt_path = './Yolo-Labels/' + filename
    txt_file = open(txt_path, "r")
    
    lines = txt_file.read().split('\n')   
    txt_file.close()

    txt_outpath = './Yolo-Labels/' + filename
    txt_outfile = open(txt_outpath, "w")

    for line in lines:
        if(len(line) >= 2):
            print(line[0])
            txt_outfile.write(str(2) + line[1:] + '\n')
    txt_outfile.close()
import os
from os import walk, getcwd
from PIL import Image

# This function helps convert the coordinates returned by Figure 8 to YOLO format
def convertYoloToRegular(size, box):

    x2 = int(((2*size[0]*float(coord[0]))+(size[0]*float(coord[2])))/2)
    x1 = int(((2*size[0]*float(coord[0]))-(size[0]*float(coord[2])))/2)

    y2 = int(((2*size[1]*float(coord[1]))+(size[1]*float(coord[3])))/2)
    y1 = int(((2*size[1]*float(coord[1]))-(size[1]*float(coord[3])))/2)
    return (x1,y1,x2,y2)


if __name__ == "__main__":
    text_file = open('32_001_2018-07-24.txt')
    lines = text_file.read().split()
    coord = lines[1:]
    #coord = [0.6234375000000001, 0.6333333333333333, 0.059375000000000004, 0.11944444444444445]

    im = Image.open('32_001_2018-07-24.jpg')
    width, height = im.size

    size = [width, height]
    print(convertYoloToRegular(size, coord))
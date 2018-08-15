import os
import cv2
import shutil
from PIL import Image
import sys

# This function helps convert the coordinates returned by Figure 8 to YOLO format
def convertYoloToRegular(size, box):

    x2 = int(((2*size[0]*float(coord[0]))+(size[0]*float(coord[2])))/2)
    x1 = int(((2*size[0]*float(coord[0]))-(size[0]*float(coord[2])))/2)

    y2 = int(((2*size[1]*float(coord[1]))+(size[1]*float(coord[3])))/2)
    y1 = int(((2*size[1]*float(coord[1]))-(size[1]*float(coord[3])))/2)
    return (x1,y1,x2,y2)


pathCleanDataRevolver = 'clean-data/Revolver' # create a name for folder
pathCleanDataMagazine = 'clean-data/Magazine'
if not os.path.exists(pathCleanDataRevolver): # if there is no folder create one 
    os.makedirs(pathCleanDataRevolver)        # with the name from above
if not os.path.exists(pathCleanDataMagazine):
    os.makedirs(pathCleanDataMagazine)

listOfFiles = os.listdir('Images')
#print(listOfFiles)

ind = 138

while ind < len(listOfFiles):
    print("Index is: " + str(ind))
    filename = listOfFiles[ind]
#for filename in os.listdir('Images'): # loop thru folder Images 
    names = filename.split('.')    
    if (names[-1].lower() == 'jpg'):
        newname = str(names[0])
        #print(newname)
        txtFileName = newname + '.txt'
        #print(txtFileName)
        txt_path = "./Yolo-Labels/" + txtFileName
        try:
            txt_file = open(txt_path, "r")
            lines = txt_file.read().split('\n')

        
            ct = 0

            img = cv2.imread('./Images/' + filename)
            output = img.copy()

            for line in lines:
            
            
                if(len(line) >= 2):
                    #print("This is TUng")
                    #print(line)
                    ct = ct + 1
                    coordinates = line.split()
                    coord = coordinates[1:]
                    width, height, channels = img.shape
                    #print(str(height) + " " + str(width))
                    size = [height, width]
                    #print(convertYoloToRegular(size, coord))
                    x,y,z,w = convertYoloToRegular(size,coord)
                    cv2.rectangle(output, (x, y), (z, w), (0, 0, 255), 2)
                    cv2.imshow(filename, output)

            k = cv2.waitKey(0)

            if k == ord('r'):
                print(filename + " copied to clean-data/Revolver folder!")
                cv2.imwrite(os.path.join(pathCleanDataRevolver, filename), img)
                shutil.copy2(txt_path, pathCleanDataRevolver) # complete target filename given
                ind += 1
            if k == ord('m'):
                print(filename + " copied to clean-data/Magazine folder!")
                cv2.imwrite(os.path.join(pathCleanDataMagazine, filename), img)
                shutil.copy2(txt_path, pathCleanDataMagazine)
                ind += 1
            elif k == ord('q'):
                sys.exit()
            elif k == ord('b'): # go backward
                ind -= 1
                if ind == -1:
                    ind += len(listOfFiles)
            else:
                ind += 1    
            cv2.destroyAllWindows()                
            txt_file.close()
        except(RuntimeError, TypeError, NameError, FileNotFoundError):
            print('The text file does not exist for: ' + filename)
            ind += 1
            pass
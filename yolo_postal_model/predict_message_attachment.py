from darkflow.net.build import TFNet
import cv2

from io import BytesIO
import time
import requests
from PIL import Image
import numpy as np
import smtplib
import mimetypes

options = {"model": "cfg/yolov2-fedtest.cfg", "load": "bin/yolov2-fed_33000.weights", "gpu": 1.0, "threshold": 0.1}
#options = {"model": "cfg/yolov2.cfg", "load": "bin/yolov2.weights", "threshold": 0.1}

tfnet = TFNet(options)

PersonSeen = 0
def handleBird():
    pass

while True:
    r = requests.get('http://192.168.1.84:5000/image.jpg') # replace with your ip address
    curr_img = Image.open(BytesIO(r.content))
    curr_img_cv2 = cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)

    # uncomment below to try your own image
    #imgcv = cv2.imread('./sample/bird.png')
    result = tfnet.return_predict(curr_img_cv2)
    #print(result)
    for detection in result:
        if detection['label'] == 'FedEx':
            print("FedEx detected")
            PersonSeen += 1
            curr_img.save('Persons/%i.jpg' % PersonSeen)

            img_attach = curr_img
            fp = open(img_attach, 'rb')
            att = email.mime.application.MIMEApplication(fp.read(),_subtype=".jpg")
            fp.close()
            att.add_header('Content','attachment',img_attach=img_attach)
            msg.attach(att)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("@gmail.com", "RaspberryPi2817")
 
            msg = "FedEx detected!!!"
            server.sendmail("@gmail.com", "@gmail.com", msg)
            #server.sendmail("@gmail.com", "@gmail.com", msg)
            server.sendmail("@gmail.com", "@gmail.com", msg)           
            server.quit()
        elif detection['label'] == 'UPS':
            print("UPS detected")
            PersonSeen += 1
            curr_img.save('Persons/%i.jpg' % PersonSeen)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("@gmail.com", "RaspberryPi2817")
 
            msg = "UPS detected!!!"
            server.sendmail("@gmail.com", "@gmail.com", msg)
            #server.sendmail("@gmail.com", "@gmail.com", msg)
            server.sendmail("@gmail.com", "@gmail.com", msg)           
            server.quit()
        elif detection['label'] == 'USPS':
            print("USPS detected")
            PersonSeen += 1
            curr_img.save('Persons/%i.jpg' % PersonSeen)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("@gmail.com", "RaspberryPi2817")
 
            msg = "USPS detected!!!"
            server.sendmail("@gmail.com", "@gmail.com", msg)
            #server.sendmail("@gmail.com", "96@gmail.com", msg)
            server.sendmail("@gmail.com", "@gmail.com", msg)           
            server.quit()
    print('running again')
    time.sleep(4)



 

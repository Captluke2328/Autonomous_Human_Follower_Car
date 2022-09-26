import jetson.inference
import jetson.utils
import sys
import threading
import time

import cv2
import collections
import argparse
import sys

#import detector as d
from camera import *
from detector import *
from time import sleep
from track import *

pError =0
pid =[0.5,0.4]

net = jetson.inference.detectNet("SSD-Mobilenet-v2",0.75)
camera = jetson.utils.videoSource("csi://0")

if __name__ == "__main__":
    print("Setting up the detector")  
    cam = Camera()
    
    while True:
        try:
            det = detector(cam)
            tr  = Track(cam)
            
            img, fps, info = det.get_detections()
            
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
            
            thread=threading.Thread(target=tr.trackObject, args=(frame,info,pid,pError))
            thread.start()
               
            cv2.imshow("Capture",frame)
            if cv2.waitKey(1) & 0XFF == ord('q'):
                cam.close_camera()
                break
            
        except Exception as e:
            print(str(e))
    
    cv2.destroyAllWindows()

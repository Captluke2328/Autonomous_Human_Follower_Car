from time import perf_counter
from turtle import pos
import jetson.inference
import jetson.utils
import cv2
import numpy as np
from camera import *
import arduino as sm

class Track:
    def __init__(self,C):
        self.ca = C
        self.net = C.net
        self.cam = C.camera
        self.posX = 0
        self.ser = sm.initConnection('/dev/ttyACM0',115200)
    
    def trackObject(self,img,info,pid,pError):
        w,h = self.ca.get_image_size()
        
        if (info[1]) !=0:
            error = w//2 - info[0][0]
            posX = int(pid[0]*error + pid[1]*(error-pError))
            posX = int(np.interp(posX, [-w//4, w//4], [-35,35]))
            pError=error
            
            sm.sendData(self.ser,[50,posX],4)
            
        else:
            sm.sendData(self.ser,[0,0],4)
            
        return img
            

import jetson.inference
import jetson.utils
import cv2
import numpy as np
from camera import *
from track import *
import threading

class detector:
    def __init__(self,C):
        self.ca = C
        self.net = C.net
        self.cam = C.camera
        self.label = False
        self.trackImg = Track(C) 
        
    def get_label(self) ->str:
        return self.label
        
    def get_detections(self):
        w,h = self.ca.get_image_size()
        
        myobjectListC = []
        myobjectListArea = []
        
        img = self.cam.Capture()
        detections = self.net.Detect(img)
        
        ID = None
        
        for detection in detections: 
            if detection.ClassID == 1:   
                ID       = detection.ClassID
                top      = int(detection.Top)
                left     = int(detection.Left)
                bottom   = int(detection.Bottom)
                right    = int(detection.Right)
                area     = int(detection.Area)
                location = detection.Center
                item     = self.net.GetClassDesc(ID)
                
                cx       = location[0]
                cy       = location[1]
                
                myobjectListArea.append(area)
                myobjectListC.append([cx,cy])

        fps = self.net.GetNetworkFPS()

        if len(myobjectListArea) > 0:
            self.label = True
            i = myobjectListArea.index(max(myobjectListArea))
            return jetson.utils.cudaToNumpy(img),fps, [myobjectListC[i],myobjectListArea[i]]

        else:
            self.label = False
            return jetson.utils.cudaToNumpy(img),fps, [[0,0],0]
        
        '''
        
        for detection in detections:
            try:
                ID       = detection.ClassID
                top      = int(detection.Top)
                left     = int(detection.Left)
                bottom   = int(detection.Bottom)
                right    = int(detection.Right)
                area     = int(detection.Area)
                location = detection.Center
                item     = self.net.GetClassDesc(ID)
                
                cx       = location[0]
                cy       = location[1]
                
                myobjectListArea.append(area)
                myobjectListC.append([cx,cy])
                    
            except:
                pass
        
        fps = self.net.GetNetworkFPS()
        
        if ID==1:
            ##return jetson.utils.cudaToNumpy(img), fps, [myobjectListC,myobjectListArea]
            i = myobjectListArea.index(max(myobjectListArea))
            return jetson.utils.cudaToNumpy(img),fps, [myobjectListC[i],myobjectListArea[i]]

        else:
            return jetson.utils.cudaToNumpy(img),fps, [[0,0],0]
                         
        '''

        
    

        

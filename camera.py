import jetson.inference
import jetson.utils
import cv2
import numpy as np

class Camera:
    def __init__(self):
        self.net = jetson.inference.detectNet("SSD-Mobilenet-v2")
        self.camera = jetson.utils.videoSource("csi://0")
        self.is_active = True
        
    def get_image_size(self):
        self.width = self.camera.GetWidth()
        self.height = self.camera.GetHeight()
        return self.width, self.height

    def close_camera(self):
        self.camera.Close()
        
    
    def visualise(self,img,data):
        
        # Draw Black Rectangle Bottom
        cv2.rectangle(img, (0,self.height-24),(self.width, self.height),(0,0,0),-1)
        
        # Draw Center Middle Line
        cv2.line(img,(self.width//2,0),(self.width//2,self.height-24), (255,0,255),3)
        
        # Draw Center Image
        cv2.circle(img, (self.width // 2, self.height // 2), 5, (0, 255, 0), cv2.FILLED)
        
        # Draw Arrowed Line
        cv2.arrowedLine(img, (int(self.width // 2), int(self.height // 2)), (int(data[0][0]), int(data[0][1])), (255, 0, 255), 5, 10)

        return img

        
        
        

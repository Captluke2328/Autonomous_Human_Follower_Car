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
        
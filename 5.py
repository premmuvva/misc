import cv2
import numpy as np

name ='drawing'
img =np.zeros ((512,512,3),np.uint8)
cv2.namedWindow(name)

def draw_circle(event ,x,y,flags ,parameters):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)

def main():
    
    while (True):
        cv2.imshow(name) 
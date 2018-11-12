# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:32:56 2018

@author: reddy
"""

#!S/usr/bin/python3
import cv2
#import matplotlib.pyplot as  plt

def main():
    name="REDDY"
    path='/home/reddy/Desktop/prog/output/video1'
    
    cv2.namedWindow(name)
    
    cap=cv2.VideoCapture(0) 
    print(cap)  
    codec=cv2.VideoWriter_fourcc('X','V','I','D')
    framerate=30
    resolution=(2000,2000)
    
    video = cv2.VideoWriter(path,codec,framerate,resolution)
    
    if cap.isOpened():
        ret,frame =cap.read()
    else :
        ret=False
    
    while ret:
        ret,frame =cap.read()
        video.write(frame)
        cv2.imshow(name,frame)
        if cv2.waitKey(1)==27:
            break
    
    cv2.destroyWindow(name)
    video.release()
    cap.release()
	
if __name__=='__main__':
    main()

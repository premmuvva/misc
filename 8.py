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
    cv2.namedWindow(name)
    cap=cv2.VideoCapture(0) 
    print (cap.get(3),cap.get(3))
    
    cap.set(3,2048)
    cap.set(4,2048)
    
    print (cap.get(3),cap.get(3))
    
    
    if cap.isOpened():
        ret,frame =cap.read()
    else :
        ret=False
    
    while ret:
        ret,frame =cap.read()
        
        cv2.imshow(name,frame)
        if cv2.waitKey(1)==27:
            break
    cv2.destroyWindow(name)
    cap.release()
	
if __name__=='__main__':
    main()
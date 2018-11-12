# -*- coding: utf-8 -*-
"""
Created on Sun May 27 13:32:56 2018

@author: reddy
"""

#!S/usr/bin/python3
import cv2
#import matplotlib.pyplot as  plt
import numpy as np

def main():
    name="REDDY"
    
    cv2.namedWindow(name)
    
    cap=cv2.VideoCapture(0) 
    
    if cap.isOpened():
        ret,frame =cap.read()
    else :
        ret=False
    
    while ret:
        ret,frame =cap.read()
        
        grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        edges=cv2.Canny(grey,50,250,apertureSize=5,L2gradient=True)
        
        lines=cv2.HoughLines(edges,1,np.pi/180,200)
        print(lines)
        if lines is not None:
            for rho , theta in lines[0]:
                a =np.cos (theta)
                b =np.sin (theta)
                x=a*rho
                y=b*rho
                pts=(int(x+1000*-b),int(y+1000*a))
                pts2=(int(x+1000-b),int(y-1000*a))
                cv2.line(frame,pts,pts2,(0,255,0),4)
        
        cv2.imshow(name,frame)
        if cv2.waitKey(1)==27:
            break
    
    cv2.destroyWindow(name)
    cap.release()
	
if __name__=='__main__':
    main()

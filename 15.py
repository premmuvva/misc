# -- coding: utf-8 --
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import time
t=0
def main():
   wn="Live vidio capture"
   cv2.namedWindow(wn)
   cap=cv2.VideoCapture(0)
   x=True
  
   start = time.time()
   while x:
       global t
       x,y=cap.read()
       #img1=cv2.cvtColor(y,cv2.COLOR_BGR2RGB)
       img2=cv2.cvtColor(y,cv2.COLOR_BGR2GRAY)
       cv2.imshow(wn,y)
       cv2.imshow("GRAYSCALE",img2)
       t+=1
       if cv2.waitKey(1)==27:
           break
       
   end = time.time() 
   print (end - start)
   
   cv2.destroyAllWindows()
   cap.release() 
      
       
if __name__=="__main__":
    main()
print(t)
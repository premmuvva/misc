import cv2
import numpy as np

def main():
    
    img=np.zeros((512,512,3),np.uint8) #to place a black background 
    
    cv2.line(img,(0,99),(10,99),(255,0,0),2)
    
    cv2.rectangle(img,(10,9),(99,99),(0,255,0),-2)
    
    cv2.circle(img,(10,0),50,(0,255,0),1)
    
    cv2.ellipse(img,(160,260),(50,20),0,0,90,(0,255,0),1)
    
    text = "PREM KUMAR REDDY MUUVA"
    cv2.putText(img , text , (100,100 ), cv2.FONT_HERSHEY_SIMPLEX , 5 ,(255,255,0))

    
    cv2.imshow('Lena',img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')


    
if __name__=='__main__':
    main()

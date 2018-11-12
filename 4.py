import cv2
import numpy as np

def func():
    pass

def main():
    
    img=np.zeros((512,512,3),np.uint8) #to place a black background 
    
    name='reddy '
    cv2.namedWindow(name)
    
    cv2.createTrackbar('B', name ,0,255,func)
    cv2.createTrackbar('g', name ,0,255,func)
    cv2.createTrackbar('r', name ,0,255,func)
    while(True):
        cv2.imshow(name,img)
        
        if cv2.waitKey(1)==27:
            break
        blue = cv2.getTrackbarPos('B',name)
        green= cv2.getTrackbarPos('g',name)
        red= cv2.getTrackbarPos('r',name)
    
        img[:]=[blue, green, red]
        print(blue,green,red)
    
    cv2.destroyWindow('name')


    
if __name__=='__main__':
    main()

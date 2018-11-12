#!S/usr/bin/python3
import cv2
import matplotlib.pyplot as  plt

def main():
    cap=cv2.VideoCapture(0) 
    if cap.isOpened():
        ret,frame =cap.read()
    else :
        ret=False
    
    im=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    im2=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
    #im3=cv2.cvtColor(im2,cv2.COLOR_BGR2RGB)
#    plt.imshow(im)
    plt.imshow(im2)
    plt.show()
    cap.release()
	
if __name__=='__main__':
    main()  
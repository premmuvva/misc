#!S/usr/bin/python3
import cv2
import matplotlib.pyplot as  plt

def main():
    imgpath="/home/reddy/Downloads/DIP3E_Original_Images_CH01/Fig0101(1921 digital image).tif"
    img=cv2.imread(imgpath)
    plt.imshow(img)
    plt.show()
	
if __name__=='__main__':
    main()

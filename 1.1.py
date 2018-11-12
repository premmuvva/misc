#!S/usr/bin/python3
import cv2
def main():
    
	imgpath="/home/reddy/Downloads/DIP3E_Original_Images_CH01/Fig0101(1921 digital image).tif"
	img=cv2.imread(imgpath)

	cv2.imshow('lena',img)
	imgpath1="/home/reddy/Downloads/DIP3E_Original_Images_CH01/Fig0101(1921 digital image).tif"
	img1=cv2.imread(imgpath1)
	print (img)

	cv2.imshow('lena1',img1)
 	cv2.waitKey(0)
	cv2.destroyWindow("lena")
	cv2.waitKey(0)
	cv2.destroyWindow("lena1")
if __name__=='__main__':
    main()

#!S/usr/bin/python3
import cv2
def main():
    
	imgpath="/home/reddy/Downloads/DIP3E_Original_Images_CH01/Fig0101(1921 digital image).tif"
	img=cv2.imread(imgpath)

	print(type (img))
	print(img.dtype)
	print(img.shape)
	print(img.ndim)

	cv2.imshow('lena',img)

	imgpath1="/home/reddy/Downloads/DIP3E_Original_Images_CH01/Fig0101(1921 digital image).tif"
	img1=cv2.imread(imgpath1,0)

	print(type (img1))
	print(img1.dtype)
	print(img1.shape)
	print(img1.ndim)

	#print (img)

	cv2.imshow('lena1',img1)
	cv2.waitKey(0)
	cv2.destroyWindow("lena")
	cv2.waitKey(0)
	cv2.destroyWindow("lena1")
if __name__=='__main__':
    main()

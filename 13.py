import cv2
import os
def ef():
    pass
def main():
    path="/home/reddy/Documents/pic1"
#    print(os.listdir(path))
    A=[]
    wn="djf"
    cv2.namedWindow(wn)
    j=1
    for i in range(400):
       A.insert(i,str(j)+'.jpg')
       j+=1
    cv2.createTrackbar('speed',wn,0,40,ef)
    t=0
    for i in range(400):
        
        img = cv2.imread(os.path.join(path,A[i]))
        img=cv2.resize(img,None,fx=t,fy=0.1,interpolation=cv2.INTER_AREA)
        
        cv2.imshow(wn,img)
        if cv2.waitKey(1)==27:
            break
        
        z=cv2.getTrackbarPos('speed',wn)
        t=z
     
    
        
    
         
    cv2.destroyAllWindows()
    
    
if __name__=="__main__":
    main()
import cv2
import os

# Opens the Video file
cap= cv2.VideoCapture('./Video/1.mp4')
i=0

# go to required directory 
os.chdir('./Image/Left_MovingCam')

# save frame as image
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('Left_MovingCam2_'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()

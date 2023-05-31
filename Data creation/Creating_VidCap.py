import cv2
import os

# Create an object to read from camera
video = cv2.VideoCapture(0)		# for using stero cam --> '/dev/video6')

# We need to check if camera is opened previously or not
if (video.isOpened() == False):
	print("Error reading video file")

# We need to set resolutions. So, convert them from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

# Below VideoWriter object will create a frame of above defined The output is stored in 'filename.mp4' file.
result = cv2.VideoWriter('./Video/Test.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 5, size)
	
while(True):
	ret, frame = video.read()

	if ret == True:

		# Write the frame into the file 'filename.mp4'
		result.write(frame)

		# Display the frame saved in the file
		cv2.imshow('Frame', frame)

		# Press S on keyboard to stop the process
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# Break the loop
	else:
		break

# When everything done, release the video capture and video write objects
video.release()
result.release()
	
# Closes all the frames
cv2.destroyAllWindows()


# Opens the Video file
cap= cv2.VideoCapture('./Video/Test.mp4')
i=0

# go to required directory 
os.chdir('./Image/Test')

# save frame as image
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('Testsds_'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()

print("The video was successfully saved")

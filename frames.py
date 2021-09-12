#example to get the frames from one specific video 
import test
import cv2
import os
cam = cv2.VideoCapture("C:\\Users\\kaush\\Desktop\\task-itiom\\JK Wedding Entrance Dance.mp4") #path where the video is stored
try:
	
	if not os.path.exists('frames'): #creating a folder named frames to store the image frames from the video
		os.makedirs('frames')

except OSError:
	print ('Error: Could not create the desired directory')

currentframe = 0 #counter to count the number of frames
while(True):
	
	ret,frame = cam.read() #reading the video file
	if ret: #if the video is still playing
		
		name = './data/frame' + str(currentframe) + '.png' #naming the frames with .png extension
		print ('Creating...' + name) 
		cv2.imwrite(name, frame)
		currentframe += 1 #increment the number of frames
	else:
		break
cam.release()
cv2.destroyAllWindows()

#https://pyimagesearch.com/2021/01/11/opencv-video-augmented-reality/
# import the necessary packages
from augmented_reality import find_and_warp
from imutils.video import VideoStream
from collections import deque
import argparse
import imutils
import time
import cv2 
import numpy as np

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True,help="path to input video file for augmented reality")
ap.add_argument("-c", "--cache", type=int, default=-1,
help="whether or not to use reference points cache")
args = vars(ap.parse_args())  

# load the ArUCo dictionary and grab the ArUCo parameters
print("[INFO] initializing marker detector...")
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_100)
arucoParams = cv2.aruco.DetectorParameters_create()

#Load the 3D Model 
print("[INFO] accessing video stream...")
model = np.load(args["input"],allow_pickle=True)

# Create the renderer
renderer = cv2.renderer.Render3D()

# # initialize the video file stream
# print("[INFO] accessing video stream...")
# vf = cv2.VideoCapture(args["input"])

# initialize a queue to maintain the next frame from the video stream
Q = deque(maxlen=128)

# # we need to have a frame in our queue to start our augmented reality
# # pipeline, so read the next frame from our video file source and add
# # it to our queue
# (grabbed, source) = vf.read()
# Q.appendleft(source)

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while len(Q) > 0:
	
	# grab the frame from our video stream and resize it
	frame = vs.read()
	frame = imutils.resize(frame, width=600)
	
	# attempt to find the ArUCo markers in the frame, and provided
	# they are found, take the current source image and warp it onto
	# input frame using our augmented reality technique
	warped = find_and_warp(
		frame, source,
		cornerIDs=(13, 44, 92, 66),
		arucoDict=arucoDict,
		arucoParams=arucoParams,
		useCache=args["cache"] > 0)

	# if the warped frame is not None, then we know (1) we found the
	# four ArUCo markers and (2) the perspective warp was successfully
	# applied
	if warped is not None:
		# set the frame to the output augment reality frame and then
		# grab the next video file frame from our queue
		frame = warped
		source = Q.popleft()
	# for speed/efficiency, we can use a queue to keep the next video
	# frame queue ready for us -- the trick is to ensure the queue is
	# always (or nearly full)
	if len(Q) != Q.maxlen:
		# read the next frame from the video file stream
		(grabbed, nextFrame) = vf.read()
		# if the frame was read (meaning we are not at the end of the
		# video file stream), add the frame to our queue
		if grabbed:
			Q.append(nextFrame)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

# import cv2
# import numpy as np

# # Load the Aruco dictionary
# aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_X5_100)

# # Create the Aruco marker detector
# aruco_detector = cv2.aruco.DetectorParameters_create()

# # Load the 3D model
# model = np.load("model.npz")

# # Create the renderer
# renderer = cv2.renderer.Render3D()

# # Capture the image
# cap = cv2.VideoCapture(0)

# while True:
#     # Capture the frame
#     ret, frame = cap.read()

#     # Detect the Aruco markers
#     corners, ids, rejected_img_points = aruco_detector.detectMarkers(frame, aruco_dict)

#     # If an Aruco marker is detected
#     if ids is not None:
#         # Calculate the pose of the Aruco marker
#         pose = aruco_detector.estimatePoseSingleMarkers(corners, ids, 0.05)

#         # Transform the 3D model to the pose of the Aruco marker
#         transformed_model = renderer.transform(model, pose)

#         # Render the 3D model on the image
#         renderer.draw(transformed_model, frame)

#     # Display the image
#     cv2.imshow("Frame", frame)

#     # Wait for a key press
#     key = cv2.waitKey(1)

#     # If the key `q` is pressed, quit
#     if key == ord("q"):
#         break

# # Release the capture
# cap.release()

# # Close all windows
# cv2.destroyAllWindows()


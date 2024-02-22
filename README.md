This Python project creates a webcam monitoring system that detects motion and sends email alerts when motion is detected. Here's a brief description of how it works:

#Video Capture: 
The script captures video from the webcam using OpenCV's VideoCapture.

###Motion Detection:
It detects motion in the video stream by comparing consecutive frames and identifying areas where significant changes occur.

###Object Detection:
When motion is detected, the script identifies the object(s) causing the motion by drawing bounding rectangles around them.

###Image Capture: 
It captures images of the detected object(s) and saves them to a folder.

###Email Alert: 
Upon detecting motion, it triggers an email alert by sending an email with the captured image(s) attached.

###Threading: 
Threading is used to perform tasks concurrently, such as sending email alerts and cleaning up the image folder.

###Cleanup:
Periodically, the script cleans up the image folder to remove older images.

Overall, this system provides a basic webcam monitoring solution with motion detection capabilities and email alerts for real-time notification of detected motion.

#!/usr/bin/env python3
# Implementation of an endless video stream to STDOUT

import os
import sys
import picamera

print("Content-Type: video/h264")
print()

# Reopen STDOUT for writing bytes
stream = os.fdopen(sys.stdout.fileno(), "wb")

with picamera.PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.start_recording(stream, "h264")
	
	# Record forever while saving cpu load
	while True:
		camera.wait_recording(1)

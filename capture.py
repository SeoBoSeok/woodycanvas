# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QLinearGradient
from PyQt5.QtCore import Qt, QProcess, QTimer

# import Opencv module
import cv2

from time import sleep
import RPi.GPIO as GPIO
import os
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
button1=20
GPIO.setup(button1,GPIO.IN)

num = 1
#camera = PiCamera()
# camera.exposure_mode = 'sports'

while(1):
	if GPIO.input(button1)==1:
		print ("Button 1 is Fucking Pressed!")
		
		if num == 10:
	            num = 1
            
		
		#os.system('raspistill -roi 0.3,0.3,0.7,0.7 -rot 90 -o test_%s.jpg' % str(num))
		#num += 1
		#camera = PiCamera()
		# camera.start_preview()
		camera = PiCamera()
		camera.exposure_mode = 'snow'
		camera.capture('test_capture_%s.jpg' % str(num))
		num += 1
		camera.close()
		sleep(.1)
	else:
		print ("Button 1 is not Pressed Yet")
		sleep(.1)



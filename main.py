# always seem to need this
import sys
import os
from time import sleep
import subprocess

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QLinearGradient
from PyQt5.QtCore import Qt, QProcess, QTimer

# import Opencv module
import cv2

# This is our window from QtCreator
import mainwindow_test4

# Splash Screen
class SplashScreen(QWidget):
  def __init__(self) -> None:
    super().__init__()
    self.setWindowTitle("WOODY CANVAS")
    self.setFixedSize(460, 500)
    self.setWindowFlag(Qt.FramelessWindowHint)
    self.setAttribute(Qt.WA_TranslucentBackground)
    
    self.counter = 0
    self.n = 300
    
    self.initUI()
    self.timer = QTimer()
    self.timer.timeout.connect(self.loading)
    self.timer.start(30)
    
  def initUI(self):
    layout = QVBoxLayout()
    self.setLayout(layout)
    
    self.frame = QFrame()
    layout.addWidget(self.frame)
    
    self.labelTitle = QLabel(self.frame)
    self.labelTitle.setObjectName('LabelTitle')
    
    pixmap = QPixmap('./icons/logo.png')
    lbl_img = QLabel(self.frame)
    lbl_img.setPixmap(pixmap)
    lbl_img.setAlignment(Qt.AlignCenter)
    
    self.labelTitle.resize(self.width() - 10, 150)
    self.labelTitle.move(0, 40) # x, y
    self.labelTitle.setText("WOODY CANVAS")
    self.labelTitle.setAlignment(Qt.AlignCenter)
    
    self.labelDescription = QLabel(self.frame)
    self.labelDescription.resize(self.width() - 10, 50)
    self.labelDescription.move(0, self.labelTitle.height())
    self.labelDescription.setObjectName("LabelDescription")
    self.labelDescription.setText("<strong>Working on Woody Module #1</strong>")
    self.labelDescription.setAlignment(Qt.AlignCenter)
    
    self.progressBar = QProgressBar(self.frame)
    self.progressBar.resize(self.width() - 200 - 10, 20)
    self.progressBar.move(100, self.labelDescription.y() + 130)
    self.progressBar.setAlignment(Qt.AlignCenter)
    self.progressBar.setFormat('%p%')
    self.progressBar.setTextVisible(True)
    self.progressBar.setRange(0, self.n)
    self.progressBar.setValue(20)
    
    self.labelLoading = QLabel(self.frame)
    self.labelLoading.resize(self.width() - 10, 30)
    self.labelLoading.move(0, self.progressBar.y() + 70)
    self.labelLoading.setObjectName("LabelLoading")
    self.labelLoading.setAlignment(Qt.AlignCenter)
    self.labelLoading.setText('loading...')
  
  def loading(self):
    self.progressBar.setValue(self.counter)
    if self.counter == int(self.n * 0.3):
      self.labelDescription.setText('<strong>Working on Woody Camera #2</strong>')
    elif self.counter == int(self.n * 0.6):
      self.labelDescription.setText('<strong>Working on Woody Interface #3</strong>')
    elif self.counter >= self.n:
      self.timer.stop()
      self.form = MainWindow()
      self.form.show()
      
      self.close()
      
      # sleep(1)
   	
    self.counter += 2
    
    
  
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_test4.Ui_MainWindow):
  
# access variables inside of the UI's file
	def pressedPreviewButton(self):
		print("PreviewButton")
		# self.liveView = False
		self.controlTimer()
		# sleep(1)
		self.lblCamView.clear()
		myPixmap = QPixmap('/home/pi/test/picam/img/image.jpg')
		myScaledPixmap = myPixmap.scaled(self.lblCamView.size(), Qt.KeepAspectRatio)
		self.lblCamView.setPixmap(myScaledPixmap)
		# self.viewCam()
		# self.controlTimer()
		# self.pressedSettingsButton()

	def pressedSnapButton(self):
		print("Pressed Snap")
		# self.lblCamView.clear()
		self.controlTimer()

	def pressedSettingsButton(self):
		self.p = QProcess()
		self.p.start("python",  ["scanTest_V1.py"])
		
		print("Auto Settings pressed")

		'''
		self.lblCamView.clear()
		myPixmap = QPixmap('/home/pi/woodycanvas/img/image.jpg')
		myScaledPixmap = myPixmap.scaled(self.lblCamView.size(), Qt.KeepAspectRatio)
		self.lblCamView.setPixmap(myScaledPixmap)
  	'''
   
		self.timer.stop()
		self.cap.release()
		self.lblCamView.clear()
  
		myPixmap = QPixmap('/home/pi/test/picam/img/image.jpg')
		myScaledPixmap = myPixmap.scaled(self.lblCamView.size(), Qt.KeepAspectRatio)
		self.lblCamView.setPixmap(myScaledPixmap)
   
		# self.pressedPreviewButton()
   
		# self.lblCamView.clear()
		# myPixmap = QPixmap('/home/pi/woodycanvas/img/image.jpg')
		# myScaledPixmap = myPixmap.scaled(self.lblCamView.size(), Qt.KeepAspectRatio)
		# self.lblCamView.setPixmap(myScaledPixmap)
  
		# sleep(2)
		# self.pressedPreviewButton()
		#self.lblCamView.clear()
		#self.runCommand("raspistill -t 2000 -o image.jpg")
		#os.system("raspistill -t 2000 -o image.jpg");
		print("capturing image")
		sleep(70)
		self.p.close()
		#self.p = QProcess()
		#self.p.start("raspistill", ["-t", "2000", "-o", "testImage.jpg"])
		#self.p.start("raspistill", ["-roi","0.1, 0.1, 0.7, 0.7","-rot" ,"90" ,"-t", "18000", "-tl", "2000", "-o", "image_num_%03d_today.jpg"])
		#self.p.waitForFinished()
		#sleep(10)
		print("merge start")
		self.p = QProcess()
		self.p.start("python3",  ["merge.py"])
		self.p.waitForFinished()
		#subprocess.run(['python3', 'merge.py'], capture_output=True)
		sleep(3)
		print("merge end")
		self.p = QProcess()
		self.p.start("rsync",  ["-azvh", "/home/pi/test/picam/img/image.jpg", "/home/pi/pi-camera-stream-flask/static/"])
		self.p.waitForFinished()
		#subprocess.run(['rsync', '-azvh', "/home/pi/test/picam/img/image.jpg", "/home/pi/pi-camera-stream-flask/static/"], capture_output=True)
		#sleep(3)
		print("async End")
  
		self.pressedPreviewButton()
		#sleep(1)
		# self.controlTimer()
		# self.pressedPreviewButton()
	#def runCommand(self):
        #pass
        #p = os.popen(command)
        #if p:
            #self.editorOutput.clear()
            #output = p.read()
            #self.editorOutput.insertPlainText(output)

	# view camera
	def viewCam(self):
			# self.cap = cv2.VideoCapture(0)
   		# start timer
			# self.timer.start(20)
			# read image in BGR format
			ret, image = self.cap.read()
			cimage = cv2.transpose(image)
			image = cv2.flip(cimage, 1)
   
			# convert image to RGB format
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			# get image infos
			height, width, channel = image.shape
			step = channel * width
			# create QImage from image
			qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
			# show image in img_label
			# self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
			self.lblCamView.setPixmap(QPixmap.fromImage(qImg))
	# start/stop timer
	def controlTimer(self):
			# self.lblCamView.clear()
			# if timer is stopped
			if not self.liveView:
					# create video capture
					self.cap = cv2.VideoCapture(0)
					# start timer
					self.timer.start(10)
					# update control_bt text
					# self.btnSnap.setText("stop")
					# self.ui.control_bt.setText("Stop")
					self.liveView = True
			# if timer is started
			else:
					# stop timer
					self.timer.stop()
					# release video capture
					self.cap.release()
					# update control_bt text
					# self.ui.control_bt.setText("Start")
					self.liveView = False
					self.lblCamView.clear()
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) # gets defined in the UI file

		# create a timer
		self.timer = QTimer()
		# set timer timeout callback function
		self.timer.timeout.connect(self.viewCam)  

		sleep(2)
		self.liveView = False
		self.controlTimer()

		# Tie buttons to clicks
		self.btnSnap.clicked.connect(lambda: self.controlTimer())
		self.btnPreview.clicked.connect(lambda: self.pressedPreviewButton())
		self.btnSettings.clicked.connect(lambda: self.pressedSettingsButton()) # auto


def main():
	# a new app instance
	app = QApplication(sys.argv)
	app.setStyleSheet('''
			#LabelTitle {
					font-size: 40px;
					color: black;
			}

			#LabelDesc {
					font-size: 20px;
					color: #c2ced1;
			}

			#LabelLoading {
					font-size: 20px;
					color: #e8e8eb;
			}

			QFrame {
					background-color: white;
			}

			QProgressBar {
					background-color: #DA7B93;
					color: rgb(200, 200, 200);
					border-style: none;
					border-radius: 5px;
					text-align: center;
					font-size: 20px;
			}

			QProgressBar::chunk {
					border-radius: 5px;
					background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
			}
   
			#btnPreview {
				
			}
	''')
  
	splash = SplashScreen()
	splash.show()
		
	# form = MainWindow()
	# form.show()
	# without this, the script exits immediately.
	sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
	main()
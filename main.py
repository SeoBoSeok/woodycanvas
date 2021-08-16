# always seem to need this
import sys
import os
from time import sleep

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QLinearGradient
from PyQt5.QtCore import Qt, QProcess, QTimer

# import Opencv module
import cv2

# This is our window from QtCreator
import mainwindow_auto

# Splash Screen
class SplashScreen(QWidget):
  def __init__(self) -> None:
    super().__init__()
    self.setWindowTitle("WOODY CANVAS")
    self.setFixedSize(1100, 500)
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
    self.progressBar.resize(self.width() - 200 - 10, 50)
    self.progressBar.move(100, self.labelDescription.y() + 130)
    self.progressBar.setAlignment(Qt.AlignCenter)
    self.progressBar.setFormat('%p%')
    self.progressBar.setTextVisible(True)
    self.progressBar.setRange(0, self.n)
    self.progressBar.setValue(20)
    
    self.labelLoading = QLabel(self.frame)
    self.labelLoading.resize(self.width() - 10, 50)
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
   	
    self.counter += 1
    
    
  
# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
# access variables inside of the UI's file
	def pressedPreviewButton(self):
		print("Pressed Preview!")
		self.controlTimer()
		sleep(1)
		self.lblCamView.clear()
		myPixmap = QPixmap('/home/pi/woodycanvas/img/image.jpg')
		myScaledPixmap = myPixmap.scaled(self.lblCamView.size(), Qt.KeepAspectRatio)
		self.lblCamView.setPixmap(myScaledPixmap)
		# self.viewCam()
		# self.controlTimer()

	def pressedSnapButton(self):
		print("Pressed Snap")
		# self.lblCamView.clear()

	def pressedSettingsButton(self):
		print("Settings pressed")
		self.pressedPreviewButton()
		#self.lblCamView.clear()
		#self.runCommand("raspistill -t 2000 -o image.jpg")
		#os.system("raspistill -t 2000 -o image.jpg");
		self.p = QProcess()
		#self.p.start("raspistill", ["-t", "2000", "-o", "testImage.jpg"])
		self.p.start("raspistill", ["-roi","0.1, 0.1, 0.7, 0.7","-rot" ,"90" ,"-t", "18000", "-tl", "2000", "-o", "image_num_%03d_today.jpg"])
		self.p.waitForFinished()
		#sleep(10)
		print("merge start")
		self.p = QProcess()
		self.p.start("python3",  ["merge.py"])
		self.p.waitForFinished()
		print("merge end")
		self.p.start("rsync",  ["-azvh", "/home/pi/picam/img/image.jpg", "/home/pi/pi-camera-stream-flask/static/"])
		self.p.waitForFinished()
		print("async End")
  
		# self.pressedPreviewButton()
		self.controlTimer()
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
			if not self.timer.isActive():
					# create video capture
					self.cap = cv2.VideoCapture(0)
					# start timer
					self.timer.start(20)
					# update control_bt text
					self.btnSnap.setText("stop")
					# self.ui.control_bt.setText("Stop")
			# if timer is started
			else:
					# stop timer
					self.timer.stop()
					# release video capture
					self.cap.release()
					# update control_bt text
					# self.ui.control_bt.setText("Start")
					self.lblCamView.clear()
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) # gets defined in the UI file

		# create a timer
		self.timer = QTimer()
		# set timer timeout callback function
		self.timer.timeout.connect(self.viewCam)  

		sleep(2)
		self.controlTimer()

		# Tie buttons to clicks
		self.btnSnap.clicked.connect(lambda: self.controlTimer())
		self.btnPreview.clicked.connect(lambda: self.pressedPreviewButton())
		self.btnSettings.clicked.connect(lambda: self.pressedSettingsButton())


def main():
	# a new app instance
	app = QApplication(sys.argv)
	app.setStyleSheet('''
			#LabelTitle {
					font-size: 60px;
					color: #93deed;
			}

			#LabelDesc {
					font-size: 30px;
					color: #c2ced1;
			}

			#LabelLoading {
					font-size: 30px;
					color: #e8e8eb;
			}

			QFrame {
					background-color: #2F4454;
					color: rgb(220, 220, 220);
			}

			QProgressBar {
					background-color: #DA7B93;
					color: rgb(200, 200, 200);
					border-style: none;
					border-radius: 10px;
					text-align: center;
					font-size: 30px;
			}

			QProgressBar::chunk {
					border-radius: 10px;
					background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);
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
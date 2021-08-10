# always seem to need this
import sys
import os
from time import sleep

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QProcess

# This is our window from QtCreator
import mainwindow_auto

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
# access variables inside of the UI's file
	def pressedPreviewButton(self):
		print("Pressed Preview!")
		myPixmap = QPixmap('/home/pi/test/picam/img/image.jpg')
		myScaledPixmap = myPixmap.scaled(self.lblCamView.size(), Qt.KeepAspectRatio)
		self.lblCamView.setPixmap(myScaledPixmap)

	def pressedSnapButton(self):
		print("Pressed Snap")
		# self.lblCamView.clear()

	def pressedSettingsButton(self):
		print("Settings pressed")
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
		self.p.start("rsync",  ["-azvh", "/home/pi/test/picam/img/image.jpg", "/home/pi/pi-camera-stream-flask/static/"])
		self.p.waitForFinished()
		print("async End")
	#def runCommand(self):
        #pass
        #p = os.popen(command)
        #if p:
            #self.editorOutput.clear()
            #output = p.read()
            #self.editorOutput.insertPlainText(output)


	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self) # gets defined in the UI file


		# Tie buttons to clicks
		self.btnSnap.clicked.connect(lambda: self.pressedSnapButton())
		self.btnPreview.clicked.connect(lambda: self.pressedPreviewButton())
		self.btnSettings.clicked.connect(lambda: self.pressedSettingsButton())


def main():
	# a new app instance
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	# without this, the script exits immediately.
	sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
	main()
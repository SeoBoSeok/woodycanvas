# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_test4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 800)
        MainWindow.setMinimumSize(QtCore.QSize(320, 480))
        MainWindow.setMaximumSize(QtCore.QSize(480, 800))
        MainWindow.setBaseSize(QtCore.QSize(320, 480))
        MainWindow.setStyleSheet("QPushButton#btnSettings:hover {\n"
"                background-color: #86BC26;\n"
"            }")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(320, 480))
        self.centralWidget.setMaximumSize(QtCore.QSize(480, 800))
        self.centralWidget.setBaseSize(QtCore.QSize(320, 480))
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 610, 461, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_1.setContentsMargins(11, 0, 11, 11)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.btnPreview_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPreview_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreview_4.sizePolicy().hasHeightForWidth())
        self.btnPreview_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnPreview_4.setFont(font)
        self.btnPreview_4.setAutoFillBackground(False)
        self.btnPreview_4.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"border: 2px solid white;\n"
"border-radius: 20px;\n"
"color: white;")
        self.btnPreview_4.setObjectName("btnPreview_4")
        self.horizontalLayout_1.addWidget(self.btnPreview_4)
        self.btnPreview_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPreview_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreview_3.sizePolicy().hasHeightForWidth())
        self.btnPreview_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnPreview_3.setFont(font)
        self.btnPreview_3.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"border: 2px solid white;\n"
"border-radius: 20px;\n"
"color: white;")
        self.btnPreview_3.setObjectName("btnPreview_3")
        self.horizontalLayout_1.addWidget(self.btnPreview_3)
        self.btnPreview_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPreview_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreview_2.sizePolicy().hasHeightForWidth())
        self.btnPreview_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnPreview_2.setFont(font)
        self.btnPreview_2.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"border: 2px solid white;\n"
"border-radius: 20px;\n"
"color: white;")
        self.btnPreview_2.setObjectName("btnPreview_2")
        self.horizontalLayout_1.addWidget(self.btnPreview_2)
        self.btnPreview = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPreview.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPreview.sizePolicy().hasHeightForWidth())
        self.btnPreview.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnPreview.setFont(font)
        self.btnPreview.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"border: 2px solid white;\n"
"border-radius: 20px;\n"
"color: white;")
        self.btnPreview.setObjectName("btnPreview")
        self.horizontalLayout_1.addWidget(self.btnPreview)
        self.btnSnap = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSnap.sizePolicy().hasHeightForWidth())
        self.btnSnap.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnSnap.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnSnap.setFont(font)
        self.btnSnap.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"border: 2px solid white;\n"
"border-radius: 20px;\n"
"color: white;")
        self.btnSnap.setObjectName("btnSnap")
        self.horizontalLayout_1.addWidget(self.btnSnap)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 461, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnSettings_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSettings_4.sizePolicy().hasHeightForWidth())
        self.btnSettings_4.setSizePolicy(sizePolicy)
        self.btnSettings_4.setStyleSheet("background-color: rgba(0, 0, 0, 70);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"color: white;")
        self.btnSettings_4.setCheckable(False)
        self.btnSettings_4.setChecked(False)
        self.btnSettings_4.setFlat(False)
        self.btnSettings_4.setObjectName("btnSettings_4")
        self.horizontalLayout_2.addWidget(self.btnSettings_4)
        self.btnSettings_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSettings_3.sizePolicy().hasHeightForWidth())
        self.btnSettings_3.setSizePolicy(sizePolicy)
        self.btnSettings_3.setStyleSheet("background-color: rgba(0, 0, 0, 70);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"color: white;")
        self.btnSettings_3.setObjectName("btnSettings_3")
        self.horizontalLayout_2.addWidget(self.btnSettings_3)
        self.btnSettings_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSettings_2.sizePolicy().hasHeightForWidth())
        self.btnSettings_2.setSizePolicy(sizePolicy)
        self.btnSettings_2.setStyleSheet("background-color: rgba(0, 0, 0, 70);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"color: white;")
        self.btnSettings_2.setObjectName("btnSettings_2")
        self.horizontalLayout_2.addWidget(self.btnSettings_2)
        self.btnSettings = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSettings.sizePolicy().hasHeightForWidth())
        self.btnSettings.setSizePolicy(sizePolicy)
        self.btnSettings.setStyleSheet("background-color: rgba(0, 0, 0, 70);\n"
"border: 2px solid white;\n"
"border-radius: 30px;\n"
"color: white;")
        self.btnSettings.setAutoDefault(False)
        self.btnSettings.setFlat(False)
        self.btnSettings.setObjectName("btnSettings")
        self.horizontalLayout_2.addWidget(self.btnSettings)
        self.lblCamView = QtWidgets.QLabel(self.centralWidget)
        self.lblCamView.setGeometry(QtCore.QRect(0, -10, 480, 800))
        self.lblCamView.setMinimumSize(QtCore.QSize(320, 460))
        self.lblCamView.setMaximumSize(QtCore.QSize(480, 800))
        self.lblCamView.setBaseSize(QtCore.QSize(480, 800))
        self.lblCamView.setText("")
        self.lblCamView.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCamView.setObjectName("lblCamView")
        self.lblCamView.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPreview_4.setText(_translate("MainWindow", "MENU"))
        self.btnPreview_3.setText(_translate("MainWindow", "3mm"))
        self.btnPreview_2.setText(_translate("MainWindow", "6mm"))
        self.btnPreview.setText(_translate("MainWindow", "400 feed"))
        self.btnSnap.setText(_translate("MainWindow", "GO"))
        self.btnSettings_4.setText(_translate("MainWindow", "SNAP"))
        self.btnSettings_3.setText(_translate("MainWindow", "POSITION"))
        self.btnSettings_2.setText(_translate("MainWindow", "WOOD"))
        self.btnSettings.setText(_translate("MainWindow", "SCAN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

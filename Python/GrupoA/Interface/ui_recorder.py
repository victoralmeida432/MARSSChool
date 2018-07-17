from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Recorder(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 120, 181, 81))
        self.pushButton.setStyleSheet("QPushButton {\n"
"  background-color: rgb(73, 220, 107);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 200, 181, 81))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"  background-color: rgb(73, 220, 107);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 200, 201, 81))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  background-color: rgb(73, 220, 107);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 381, 121))
        self.label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"  border: 1px solid gray;\n"
"  font: 16pt \"MS Shell Dlg 2\";\n"
"  background-color : rgb(170, 0, 255);\n"
"}")
        self.label.setObjectName("label")
        self.recordBar = QtWidgets.QProgressBar(self.centralwidget)
        self.recordBar.setGeometry(QtCore.QRect(180, 120, 141, 31))
        self.recordBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.recordBar.setProperty("value", 0)
        self.recordBar.setObjectName("recordBar")
        self.playBar = QtWidgets.QProgressBar(self.centralwidget)
        self.playBar.setGeometry(QtCore.QRect(180, 150, 141, 21))
        self.playBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.playBar.setProperty("value", 0)
        self.playBar.setObjectName("playBar")
        self.uploadBar = QtWidgets.QProgressBar(self.centralwidget)
        self.uploadBar.setGeometry(QtCore.QRect(180, 170, 141, 31))
        self.uploadBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}")
        self.uploadBar.setProperty("value", 0)
        self.uploadBar.setObjectName("uploadBar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 120, 61, 31))
        self.label_2.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"  border: 1px solid gray;\n"
"  background-color : white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 170, 61, 31))
        self.label_3.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"  border: 1px solid gray;\n"
"  background-color : white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 150, 61, 21))
        self.label_4.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignCenter\';\n"
"  border: 1px solid gray;\n"
"  background-color : white;\n"
"}")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Record"))
        self.pushButton_3.setText(_translate("MainWindow", "Play Message"))
        self.pushButton_4.setText(_translate("MainWindow", "Send Message"))
        self.label.setText(_translate("MainWindow", "A Message To Mars"))
        self.label_2.setText(_translate("MainWindow", "Gravando"))
        self.label_3.setText(_translate("MainWindow", "Upload"))
        self.label_4.setText(_translate("MainWindow", "Play"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Recorder()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


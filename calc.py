# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputlabel.setFont(font)
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.outputlabel.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.outputlabel.setLineWidth(2)
        self.outputlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.outputlabel.setObjectName("outputlabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget)
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget)
        self.cButton.setGeometry(QtCore.QRect(98, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget)
        self.arrowButton.setGeometry(QtCore.QRect(188, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget)
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.multplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.multplyButton.setGeometry(QtCore.QRect(275, 195, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multplyButton.setFont(font)
        self.multplyButton.setObjectName("multplyButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(10, 195, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(188, 195, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(98, 195, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(275, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(188, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(10, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)             
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(98, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(275, 366, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(98, 366, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(10, 366, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(188, 366, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.piusminusButton = QtWidgets.QPushButton(self.centralwidget)
        self.piusminusButton.setGeometry(QtCore.QRect(10, 453, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.piusminusButton.setFont(font)
        self.piusminusButton.setObjectName("piusminusButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(275, 453, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.decumalButton = QtWidgets.QPushButton(self.centralwidget)
        self.decumalButton.setGeometry(QtCore.QRect(188, 453, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decumalButton.setFont(font)
        self.decumalButton.setObjectName("decumalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(98, 453, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputlabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.multplyButton.setText(_translate("MainWindow", "x"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        #tk.Button(command=lambda add_digit):
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.piusminusButton.setText(_translate("MainWindow", "+/-"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.decumalButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())


import tkinter as tk
def add_digit(digit):
    calc.insert(0,digit)



calc = tk.Entry(win)
calc.grid(row=0, column=0, columnspan=3)

tk.Button(text='1').grid(row=1, column=0, stick='wens')

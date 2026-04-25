from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1366, 700)
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BackGround = QtWidgets.QLabel(self.centralwidget)
        self.BackGround.setGeometry(QtCore.QRect(0, 0, 1366, 710))
        self.BackGround.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.BackGround.setText("")
        self.BackGround.setScaledContents(False)
        self.BackGround.setObjectName("BackGround")
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(900, 440, 141, 51))
        self.Start_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Start_Button.setStyleSheet("font: 20pt \"Eras Demi ITC\";\n"
"background-color:transparent;")
        self.Start_Button.setCheckable(False)
        self.Start_Button.setFlat(False)
        self.Start_Button.setObjectName("Start_Button")
        self.Exit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_Button.setGeometry(QtCore.QRect(1080, 440, 141, 51))
        self.Exit_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit_Button.setStyleSheet("font: 20pt \"Eras Demi ITC\";\n"
"background-color:transparent;")
        self.Exit_Button.setObjectName("Exit_Button")
        self.Interface = QtWidgets.QLabel(self.centralwidget)
        self.Interface.setGeometry(QtCore.QRect(0, 0, 1366, 695))
        self.Interface.setText("")
        self.Interface.setPixmap(QtGui.QPixmap("DataBase/Gui Materials/Interface.png"))
        self.Interface.setScaledContents(True)
        self.Interface.setObjectName("Interface")
        self.Visualizing = QtWidgets.QLabel(self.centralwidget)
        self.Visualizing.setGeometry(QtCore.QRect(480, 400, 411, 281))
        self.Visualizing.setStyleSheet("")
        self.Visualizing.setText("")
        self.Visualizing.setPixmap(QtGui.QPixmap("DataBase/Gui Materials/Visualizing.gif"))
        self.Visualizing.setScaledContents(True)
        self.Visualizing.setObjectName("Visualizing")
        self.Terminal = QtWidgets.QLabel(self.centralwidget)
        self.Terminal.setGeometry(QtCore.QRect(537, 110, 751, 291))
        self.Terminal.setText("")
        self.Terminal.setPixmap(QtGui.QPixmap("DataBase/Gui Materials/Border.png"))
        self.Terminal.setScaledContents(True)
        self.Terminal.setObjectName("Terminal")
        self.Clock = QtWidgets.QLabel(self.centralwidget)
        self.Clock.setGeometry(QtCore.QRect(90, 140, 411, 221))
        self.Clock.setText("")
        self.Clock.setPixmap(QtGui.QPixmap("DataBase/Gui Materials/Clock.png"))
        self.Clock.setScaledContents(True)
        self.Clock.setObjectName("Clock")
        self.Remove = QtWidgets.QLabel(self.centralwidget)
        self.Remove.setGeometry(QtCore.QRect(499, 529, 31, 31))
        self.Remove.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Remove.setText("")
        self.Remove.setObjectName("Remove")
        self.Remove_2 = QtWidgets.QLabel(self.centralwidget)
        self.Remove_2.setGeometry(QtCore.QRect(495, 540, 31, 16))
        self.Remove_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Remove_2.setText("")
        self.Remove_2.setObjectName("Remove_2")
        self.Remove_3 = QtWidgets.QLabel(self.centralwidget)
        self.Remove_3.setGeometry(QtCore.QRect(368, 497, 33, 31))
        self.Remove_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Remove_3.setText("")
        self.Remove_3.setObjectName("Remove_3")
        self.Remove_4 = QtWidgets.QLabel(self.centralwidget)
        self.Remove_4.setGeometry(QtCore.QRect(845, 533, 25, 31))
        self.Remove_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Remove_4.setText("")
        self.Remove_4.setObjectName("Remove_4")
        self.Remove_5 = QtWidgets.QLabel(self.centralwidget)
        self.Remove_5.setGeometry(QtCore.QRect(854, 543, 25, 18))
        self.Remove_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Remove_5.setText("")
        self.Remove_5.setObjectName("Remove_5")
        self.Cut = QtWidgets.QLabel(self.centralwidget)
        self.Cut.setGeometry(QtCore.QRect(894, 405, 21, 71))
        self.Cut.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 italic 45pt \"Arial\";")
        self.Cut.setObjectName("Cut")
        self.Cut_2 = QtWidgets.QLabel(self.centralwidget)
        self.Cut_2.setGeometry(QtCore.QRect(1074, 405, 21, 71))
        self.Cut_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 italic 45pt \"Arial\";")
        self.Cut_2.setObjectName("Cut_2")
        self.Cut_3 = QtWidgets.QLabel(self.centralwidget)
        self.Cut_3.setGeometry(QtCore.QRect(1200, 454, 21, 71))
        self.Cut_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 italic 45pt \"Arial\";")
        self.Cut_3.setObjectName("Cut_3")
        self.Cut_4 = QtWidgets.QLabel(self.centralwidget)
        self.Cut_4.setGeometry(QtCore.QRect(1211, 445, 21, 71))
        self.Cut_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 italic 45pt \"Arial\";")
        self.Cut_4.setObjectName("Cut_4")
        self.Cut_5 = QtWidgets.QLabel(self.centralwidget)
        self.Cut_5.setGeometry(QtCore.QRect(1031, 445, 21, 71))
        self.Cut_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 italic 45pt \"Arial\";")
        self.Cut_5.setObjectName("Cut_5")
        self.Cut_6 = QtWidgets.QLabel(self.centralwidget)
        self.Cut_6.setGeometry(QtCore.QRect(1020, 454, 21, 71))
        self.Cut_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 italic 45pt \"Arial\";")
        self.Cut_6.setObjectName("Cut_6")
        self.Sleeping = QtWidgets.QLabel(self.centralwidget)
        self.Sleeping.setEnabled(True)
        self.Sleeping.setGeometry(QtCore.QRect(440, 370, 491, 339))
        self.Sleeping.setText("")
        self.Sleeping.setPixmap(QtGui.QPixmap("DataBase/Gui Materials/Sleeping.gif"))
        self.Sleeping.setScaledContents(True)
        self.Sleeping.setObjectName("Sleeping")
        self.Terminal_Output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Terminal_Output.setGeometry(QtCore.QRect(655, 192, 543, 152))
        self.Terminal_Output.setStyleSheet("background-color:transparent;\n"
"font: 75 10pt \"Arial Narrow\";\n"
"font: 11pt \"Eras Demi ITC\";\n"
"color: rgb(42, 155, 210);")
        self.Terminal_Output.setReadOnly(True)
        self.Terminal_Output.setPlainText("")
        self.Terminal_Output.setObjectName("Terminal_Output")
        self.Recognize = QtWidgets.QLabel(self.centralwidget)
        self.Recognize.setGeometry(QtCore.QRect(440, 362, 491, 331))
        self.Recognize.setText("")
        self.Recognize.setPixmap(QtGui.QPixmap("DataBase/Gui Materials/Recognizing.gif"))
        self.Recognize.setScaledContents(True)
        self.Recognize.setObjectName("Recognize")
        self.Listening = QtWidgets.QLabel(self.centralwidget)
        self.Listening.setGeometry(QtCore.QRect(209, 380, 271, 111))
        self.Listening.setText("")
        self.Listening.setPixmap(QtGui.QPixmap("DataBase/Gui Materials/Listening.gif"))
        self.Listening.setScaledContents(True)
        self.Listening.setObjectName("Listening")
        self.Date = QtWidgets.QTextBrowser(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(323, 148, 125, 31))
        self.Date.setStyleSheet("background-color: transparent;\n"
"color: rgb(41, 151, 205);\n"
"font: 12pt \"Eras Demi ITC\";\n"
"border: 2px solid white;\n"
"border-color: rgb(41, 150, 203);\n"
"align=\"center\"")
        self.Date.setObjectName("Date")
        self.Day = QtWidgets.QTextBrowser(self.centralwidget)
        self.Day.setGeometry(QtCore.QRect(330, 229, 104, 31))
        self.Day.setStyleSheet("background-color: transparent;\n"
"color: rgb(41, 151, 205);\n"
"font: 13pt \"Eras Demi ITC\";\n"
"border: 2px solid white;\n"
"border-color: rgb(41, 150, 203);\n"
"align=\"center\"")
        self.Day.setObjectName("Day")
        self.Time = QtWidgets.QTextBrowser(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(320, 288, 131, 31))
        self.Time.setStyleSheet("background-color: transparent;\n"
"color: rgb(41, 151, 205);\n"
"font: 13pt \"Eras Demi ITC\";\n"
"border: 2px solid white;\n"
"border-color: rgb(41, 150, 203);\n"
"align=\"center\"")
        self.Time.setObjectName("Time")
        self.Start = QtWidgets.QLabel(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(900, 440, 141, 51))
        self.Start.setStyleSheet("border: 2px Solid White;\n"
"background-color:rgb(0, 85, 181);\n"
"border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.0284091 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Start.setText("")
        self.Start.setScaledContents(True)
        self.Start.setObjectName("Start")
        self.Exit = QtWidgets.QLabel(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(1080, 440, 141, 51))
        self.Exit.setStyleSheet("border: 2px Solid White;\n"
"background-color:rgb(0, 85, 181);\n"
"border-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.0284091 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Exit.setText("")
        self.Exit.setScaledContents(True)
        self.Exit.setObjectName("Exit")
        self.BackGround.raise_()
        self.Listening.raise_()
        self.Recognize.raise_()
        self.Visualizing.raise_()
        self.Sleeping.raise_()
        self.Interface.raise_()
        self.Remove.raise_()
        self.Remove_2.raise_()
        self.Remove_3.raise_()
        self.Remove_4.raise_()
        self.Remove_5.raise_()
        self.Clock.raise_()
        self.Date.raise_()
        self.Day.raise_()
        self.Time.raise_()
        self.Terminal.raise_()
        self.Terminal_Output.raise_()
        self.Start.raise_()
        self.Exit.raise_()
        self.Cut.raise_()
        self.Cut_2.raise_()
        self.Cut_3.raise_()
        self.Cut_4.raise_()
        self.Cut_5.raise_()
        self.Cut_6.raise_()
        self.Start_Button.raise_()
        self.Exit_Button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Eric"))
        self.Start_Button.setText(_translate("MainWindow", "Start"))
        self.Exit_Button.setText(_translate("MainWindow", "Exit"))
        self.Cut.setText(_translate("MainWindow", "/"))
        self.Cut_2.setText(_translate("MainWindow", "/"))
        self.Cut_3.setText(_translate("MainWindow", "/"))
        self.Cut_4.setText(_translate("MainWindow", "/"))
        self.Cut_5.setText(_translate("MainWindow", "/"))
        self.Cut_6.setText(_translate("MainWindow", "/"))
        self.Date.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Eras Demi ITC\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Day.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Eras Demi ITC\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Time.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Eras Demi ITC\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

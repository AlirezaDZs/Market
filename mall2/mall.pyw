from PyQt5 import QtCore, QtGui, QtWidgets
from starter import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.ilabel = QtWidgets.QLineEdit(self.centralwidget)
        self.ilabel.setGeometry(QtCore.QRect(240, 40, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ilabel.setFont(font)
        self.ilabel.setObjectName("ilabel")

        self.qlabel = QtWidgets.QLineEdit(self.centralwidget)
        self.qlabel.setGeometry(QtCore.QRect(240, 100, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qlabel.setFont(font)
        self.qlabel.setObjectName("qlabel")

        self.cashbut = QtWidgets.QPushButton(self.centralwidget, clicked= lambda:self.cash())
        self.cashbut.setGeometry(QtCore.QRect(290, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cashbut.setFont(font)
        self.cashbut.setObjectName("cashbut")

        self.rembut = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.remove())
        self.rembut.setGeometry(QtCore.QRect(30, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rembut.setFont(font)
        self.rembut.setObjectName("rembut")

        self.subbut = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.sub())
        self.subbut.setGeometry(QtCore.QRect(160, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subbut.setFont(font)
        self.subbut.setObjectName("subbut")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 200, 381, 412))
        self.textBrowser.setObjectName("textBrowser")
        a = rewrite()
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">{a}</span></p></body></html>")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def sub(self):
        item = self.ilabel.text()
        quantity = self.qlabel.text()
        self.ilabel.setText("")
        self.qlabel.setText("")
        check(item, quantity)
        a = rewrite()
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">{a}</span></p></body></html>")

    def remove(self):
        item = self.ilabel.text()
        quantity = self.qlabel.text()
        self.ilabel.setText("")
        self.qlabel.setText("")
        remove(item, quantity)
        a = rewrite()
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">{a}</span></p></body></html>")

    def cash(self):
        calculate()
        f = open("check.txt","w")
        f.close()
        a = rewrite()
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">{a}</span></p></body></html>")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter the items ID"))
        self.label_2.setText(_translate("MainWindow", "Enter the items #"))
        self.cashbut.setText(_translate("MainWindow", "CASH"))
        self.rembut.setText(_translate("MainWindow", "REMOVE"))
        self.subbut.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookFetcher.ui'
#
# Created by: PyQt5 UI code generator 5.11
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(857, 428)
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(9)
        Form.setFont(font)
        self.Price = QtWidgets.QLabel(Form)
        self.Price.setGeometry(QtCore.QRect(80, 120, 73, 27))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(14)
        self.Price.setFont(font)
        self.Price.setObjectName("Price")
        self.Copy = QtWidgets.QLabel(Form)
        self.Copy.setGeometry(QtCore.QRect(50, 250, 102, 27))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(14)
        self.Copy.setFont(font)
        self.Copy.setObjectName("Copy")
        self.total = QtWidgets.QLabel(Form)
        self.total.setGeometry(QtCore.QRect(70, 340, 83, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setGeometry(QtCore.QRect(172, 49, 441, 26))
        self.t1.setObjectName("t1")
        self.t3 = QtWidgets.QLineEdit(Form)
        self.t3.setGeometry(QtCore.QRect(172, 255, 421, 27))
        self.t3.setObjectName("t3")
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setGeometry(QtCore.QRect(610, 260, 151, 26))
        self.b2.setObjectName("b2")
        self.t4 = QtWidgets.QLineEdit(Form)
        self.t4.setGeometry(QtCore.QRect(170, 340, 610, 27))
        self.t4.setObjectName("t4")
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setGeometry(QtCore.QRect(172, 129, 610, 27))
        self.t2.setObjectName("t2")
        self.BookTitle = QtWidgets.QLabel(Form)
        self.BookTitle.setGeometry(QtCore.QRect(13, 49, 150, 26))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BookTitle.setFont(font)
        self.BookTitle.setObjectName("BookTitle")
        self.b1 = QtWidgets.QPushButton(Form)
        self.b1.setGeometry(QtCore.QRect(620, 50, 151, 27))
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.EnterTitle)
        self.b2.clicked.connect(self.FindTotal)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Price.setText(_translate("Form", "Price :"))
        self.Copy.setText(_translate("Form", "Copies :"))
        self.total.setText(_translate("Form", "Total :"))
        self.b2.setText(_translate("Form", "Find Total"))
        self.BookTitle.setText(_translate("Form", "Book Title :"))
        self.b1.setText(_translate("Form", "Find Price"))

    def EnterTitle(self):
        import sqlite3
        Data1=sqlite3.connect('fetcher.db')
        c=Data1.cursor()
        t=self.t1.text()
        c.execute("SELECT Price FROM BOOKDATA WHERE Name='"+t+"';")
        rec=c.fetchone()
        if rec!=None:
            self.pr=rec[0]
            self.t2.setText(str(self.pr))
        else:
            self.t2.setText('Book not found')

    def FindTotal(self):
        self.tot=self.pr*float(self.t3.text())
        self.t4.setText(str(self.tot))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


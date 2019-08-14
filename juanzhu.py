# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'juanzhu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from img import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 410)
        # self.graphicsView = QtWidgets.QGraphicsView(Form)
        # self.graphicsView.setGeometry(QtCore.QRect(60, 30, 251, 191))
        # self.graphicsView.setObjectName("graphicsView")

        pic = QtGui.QPixmap(":/123.png")
        pic = pic.scaled(318, 322)
        self.label_pic = QtWidgets.QLabel(Form)
        self.label_pic.setGeometry(QtCore.QRect(30, 30, 318, 322))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_pic.setFont(font)
        self.label_pic.setObjectName("label_pic")
        self.label_pic.setPixmap(pic)


        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 370, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "捐助作者"))
        self.label.setText(_translate("Form", "您的慷慨是我不断前进的动力，感谢您的捐助!"))


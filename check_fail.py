# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    check_fail_msg = """您的网络好像除了问题，无法验证通过。请检查网络连接"""
    
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 100)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 390, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText(self.check_fail_msg)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "验证失败"))




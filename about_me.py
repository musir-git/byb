# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    about_me_str = """
    
    关于我：                              -----  重要必读！重要必读！ -----
    
    作者：光远
    邮箱：ycxymjg@163.com
    QQ: 362366434
    下载地址：http://39.100.3.77:81
    
    免责声明：
    1、本软件为单机软件，不会上传任何文件信息，或者将文件保存至互联网上，请放心使用。
    2、由于本软件为未完善软件，没有经过任何系统性测试，故由本软件产生的错误造成的您的任何后果以及其带来的风险均由软件使用者承担。
    3、软件使用者使用了本软件请仔细阅读此说明文档，一旦使用，均代表认同本协议。
    4、如果您对本软件源码感兴趣，可联系本人进行索取。
    5、本软件为免费软件，但由于开发、bug修复、以及优化等均需一定成本，如果你愿意，可对软件开发者进行捐助。
    6、如果您在使用本软件过程中，遇到bug，可以通过邮件向本人反馈，也可反馈改进建议或者意见。
    
    感谢您的认真阅读以及使用，祝您使用愉快，工作开心！
    """
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(900, 500)
        self.about_me = QtWidgets.QTextBrowser(Form)
        self.about_me.setGeometry(QtCore.QRect(0, 0, 900, 500))
        self.about_me.setObjectName("about_me")
        font = QtGui.QFont()
        font.setPointSize(11)

        self.about_me.setFont(font)
        self.about_me.setText(self.about_me_str)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关于我"))




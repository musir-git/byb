# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 40, 21, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.days = QtWidgets.QLineEdit(self.centralwidget)
        self.days.setGeometry(QtCore.QRect(245, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.days.setFont(font)
        self.days.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.days.setObjectName("days")
        self.zhandui_name = QtWidgets.QLineEdit(self.centralwidget)
        self.zhandui_name.setGeometry(QtCore.QRect(430, 40, 100, 30))
        self.zhandui_name.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.zhandui_name.setObjectName("zhandui_name")
        self.daka_but = QtWidgets.QToolButton(self.centralwidget)
        self.daka_but.setGeometry(QtCore.QRect(120, 30, 71, 40))
        self.daka_but.setObjectName("daka_but")
        self.info_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.info_text.setGeometry(QtCore.QRect(20, 90, 621, 141))
        self.info_text.setObjectName("info_text")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 40, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.rst_but = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.rst_but.setGeometry(QtCore.QRect(170, 340, 185, 41))
        self.rst_but.setObjectName("rst_but")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 40, 21, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.all_but = QtWidgets.QToolButton(self.centralwidget)
        self.all_but.setGeometry(QtCore.QRect(20, 30, 71, 40))
        self.all_but.setObjectName("all_but")
        self.run_but = QtWidgets.QToolButton(self.centralwidget)
        self.run_but.setGeometry(QtCore.QRect(250, 270, 201, 41))
        self.run_but.setObjectName("run_but")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 45, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.level = QtWidgets.QLineEdit(self.centralwidget)
        self.level.setGeometry(QtCore.QRect(600, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.level.setFont(font)
        self.level.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.level.setObjectName("level")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.all_but.clicked.connect(MainWindow.close)
        self.daka_but.clicked.connect(MainWindow.close)
        self.run_but.clicked.connect(MainWindow.close)
        self.rst_but.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "第"))
        self.daka_but.setText(_translate("MainWindow", "打卡名单"))
        self.label_5.setText(_translate("MainWindow", "战队名称："))
        self.rst_but.setText(_translate("MainWindow", "CommandLinkButton"))
        self.label_4.setText(_translate("MainWindow", "天"))
        self.all_but.setText(_translate("MainWindow", "全部名单"))
        self.run_but.setText(_translate("MainWindow", "生成榜单"))
        self.label.setText(_translate("MainWindow", "级别："))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import xlrd
import xlwt
from ctypes import cdll
from time import time
import os
import traceback
import logging

from about_me import Ui_Form
from juanzhu import Ui_Form as juanzu_form
from check_fail import Ui_Form as check_fail_form

logging.basicConfig(filename='log.log')


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, id, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = id

    def focusInEvent(self, e):
        # print("输入焦点在", self.id)
        QtWidgets.QLineEdit.focusInEvent(self, e)

    def focusOutEvent(self, e):
        # print(self.id,"失去输入焦点")

        if self.id == "days":
            if not self.text().isdigit() or int(self.text())>7 or int(self.text())<1:
                QMessageBox.critical(self, "错误", "天数得是数字而且只能大于0小于7才行 ！")
                self.setText("")
        if self.id == "level":
            if not self.text().isdigit():
                QMessageBox.critical(self, "错误", "级别得是数字才行！")
                self.setText("")
        QtWidgets.QLineEdit.focusOutEvent(self, e)



class Ui_MainWindow(QtWidgets.QMainWindow):
    _sopen = cdll.msvcrt._sopen
    _close = cdll.msvcrt._close
    _SH_DENYRW = 0x10

    default_dir = os.path.dirname(os.path.realpath(__file__))
    bangdan_dir = r"%s\bangdan.xls"%os.path.dirname(os.path.realpath(__file__))
    info_text_s = ""
    all_stu = ""
    daka_stu = ""
    flower = "❀"

    zone = {
        "1": {
            "0": "潜力无限区",
            "1": "学霸区"
        },
        "2": {
            "0": "默默无闻区",
            "1": "厚积薄发区",
            "2": "超级学霸区",
        },
        "3": {
            "0": "花骨朵区",
            "1": "萌芽区",
            "2": "含苞待放区",
            "3": "盛开区",
        },
        "4": {
            "0": "潜水区",
            "1": "冒泡区",
            "2": "泉水区",
            "3": "专心致志区",
            "4": "持之以恒区",
        },
        "5": {
            "0": "准备出发区",
            "1": "步行区",
            "2": "小碎步区",
            "3": "沿途观景区",
            "4": "勇攀高峰区",
            "5": "看日出区",
        },
        "6": {
            "0": "闭目养神区",
            "1": "懒洋洋区",
            "2": "悠闲区",
            "3": "猫步区",
            "4": "雀跃区",
            "5": "欢呼区",
            "6": "冲鸭区"
        },
        "7": {
            "0": "0%",
            "1": "14%",
            "2": "29%",
            "3": "43%",
            "4": "57%",
            "5": "71%",
            "6": "86%",
            "7": "100%",
        }
    }

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 40, 21, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.days = MyLineEdit("days", self.centralwidget)
        self.days.setGeometry(QtCore.QRect(245, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.days.setFont(font)
        self.days.setObjectName("days")
        self.zhandui_name = MyLineEdit("zhandui_name", self.centralwidget)
        self.zhandui_name.setGeometry(QtCore.QRect(430, 40, 100, 30))
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
        # self.rst_but = QtWidgets.QCommandLinkButton(self.centralwidget)
        # self.rst_but.setGeometry(QtCore.QRect(170, 340, 185, 41))
        # self.rst_but.setObjectName("rst_but")
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
        self.level = MyLineEdit("level", self.centralwidget)
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
        self.fileMenu = self.menubar.addMenu('&关于')
        aboutme = QAction('关于我', self)
        aboutme.triggered.connect(self.about_me)
        banbenshuoming = QAction('版本说明', self)
        banbenshuoming.triggered.connect(self.versions)
        self.fileMenu.addAction(aboutme)
        self.fileMenu.addAction(banbenshuoming)
        MainWindow.setMenuBar(self.menubar)

        self.juanzhuMenu = self.menubar.addMenu('&捐助作者')
        weixinjuanzhu = QAction('微信捐助', self)
        weixinjuanzhu.triggered.connect(self.juan_zeng)
        self.juanzhuMenu.addAction(weixinjuanzhu)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.all_but.clicked.connect(self.openfile_1)
        self.daka_but.clicked.connect(self.openfile_2)
        self.run_but.clicked.connect(self.run_1)
        # self.rst_but.clicked.connect(MainWindow.close)
        self.days.setFocusPolicy(QtCore.Qt.ClickFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.child_dialog = QDialog()
        self.child_ui = Ui_Form()
        self.child_ui.setupUi(self.child_dialog)

        self.juanzeng_dialog = QDialog()
        self.juanzeng_ui = juanzu_form()
        self.juanzeng_ui.setupUi(self.juanzeng_dialog)

        # self.menubar = self.menuBar()
        # self.fileMenu = self.menubar.addMenu('&File')
        # self.fileMenu.addAction(self.msg_txt)

        # if self.file_is_open(self.bangdan_dir):
        #     QMessageBox.critical(self, "错误", "桌面上已有【bangdan.xls】并打开。请关闭并删除文件。")
        #     self.close()



        if os.path.isfile(self.bangdan_dir):
            print("has file")
            try:
                os.remove(self.bangdan_dir)
            except Exception as e:
                logging.error(str(e))
                s = traceback.format_exc()
                logging.error(s)
                QMessageBox.critical(self, "错误", "【表扬榜】文件可能已经打开，请先关闭")
                self.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "榜单生成工具"))
        self.label_3.setText(_translate("MainWindow", "第"))
        self.daka_but.setText(_translate("MainWindow", "打卡名单"))
        self.label_5.setText(_translate("MainWindow", "战队名称："))
        # self.rst_but.setText(_translate("MainWindow", "CommandLinkButton"))
        self.label_4.setText(_translate("MainWindow", "天"))
        self.all_but.setText(_translate("MainWindow", "全部名单"))
        self.run_but.setText(_translate("MainWindow", "生成榜单"))
        self.label.setText(_translate("MainWindow", "级别："))

    def openfile_1(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', self.default_dir, 'Excel files(*.xlsx , *.xls)')
        self.all_stu = openfile_name[0]
        self.info_text_s = "全体学生名单：%s \n" % openfile_name[0]
        self.info_text.setText(self.info_text_s)

    def openfile_2(self):
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', self.default_dir, 'Excel files(*.xlsx , *.xls)')
        self.daka_stu = openfile_name[0]
        self.info_text_s = self.info_text_s +"打卡学生名单：%s \n" % openfile_name[0]
        self.info_text.setText(self.info_text_s)

    def run_1(self):
        try:
            self.run()
        except Exception as e:
            logging.error(str(e))
            s = traceback.format_exc()
            logging.error(s)


    def run(self):
        days = self.days.text()
        zhandui_name = self.zhandui_name.text()
        if not days:
            QMessageBox.critical(self, "错误", "天数不能为空！")
        if not zhandui_name:
            QMessageBox.critical(self, "错误", "战队名称不能为空！")
        if not self.all_stu:
            QMessageBox.critical(self, "错误", "所有学员名单必填！")
        if not self.daka_stu:
            QMessageBox.critical(self, "错误", "打卡学员名单必填！")
        self.info_text_s = self.info_text_s + "%s 战队 第 %s 打卡 \n\n" % (zhandui_name, days)
        self.info_text.setText(self.info_text_s)
        self.info_text_s = self.info_text_s + "榜单正在生成中..."
        self.info_text.setText(self.info_text_s)

        all_data = xlrd.open_workbook(self.all_stu)
        all_table = all_data.sheets()[0]
        students = all_table.col_values(0)
        del students[0]

        daka = xlrd.open_workbook(self.daka_stu)
        daka_table = daka.sheets()[0]
        daka_students = daka_table.col_values(1)

        daka_list = []
        all_daka = []
        daka_dict = {}
        for i, v in enumerate(daka_students):
            if i == 0:
                continue
            if v not in students or ("%s" % v).find("1") == 0:
                continue
            if v not in all_daka:
                all_daka.append(v)
            if v in daka_dict:
                o_v = daka_dict[v]
                n_v = int(daka_table.cell(i, 8).value)
                if o_v + n_v > int(self.days.text()):
                    daka_dict[v] = int(self.days.text())
                else:
                    daka_dict[v] = o_v + n_v
            else:
                daka_dict[v] =  int(daka_table.cell(i, 8).value)

        for i_k, i_v in daka_dict.items():
            daka_list.append({
                "name": i_k,
                "count": i_v
            })

        nodaka_list = list(set(students) - set(all_daka))
        for i, v in enumerate(nodaka_list):
            if v not in students or ("%s" % v).find("1") == 0:
                continue
            daka_list.append({
                "name": v,
                "count": "0"
            })

        def takeCount(elem):
            return int(elem["count"])

        daka_list.sort(key=takeCount, reverse=True)

        workbook = xlwt.Workbook()

        paihang = workbook.add_sheet('paihang')

        xlwt.add_palette_colour("colour0", 0x09)
        workbook.set_colour_RGB(0x09, 251, 0, 7)

        xlwt.add_palette_colour("colour1", 0x21)
        workbook.set_colour_RGB(0x21, 251, 221, 205)

        xlwt.add_palette_colour("colour2", 0x22)
        workbook.set_colour_RGB(0x22, 219, 236, 209)

        xlwt.add_palette_colour("colour3", 0x23)
        workbook.set_colour_RGB(0x23, 233, 233, 233)

        xlwt.add_palette_colour("colour4", 0x24)
        workbook.set_colour_RGB(0x24, 208, 217, 239)

        xlwt.add_palette_colour("colour5", 0x25)
        workbook.set_colour_RGB(0x25, 255, 255, 11)

        xlwt.add_palette_colour("colour6", 0x26)
        workbook.set_colour_RGB(0x26, 130, 202, 63)

        al = xlwt.Alignment()
        al.horz = 0x02  # 设置水平居中
        al.vert = 0x01  # 设置垂直居中

        font = xlwt.Font()
        font.height = 11 * 20
        font.name = '宋体'

        style = xlwt.XFStyle()
        style.font = font
        style.alignment = al

        font1 = xlwt.Font()
        font1.height = 15 * 20
        # font1.name = 'name Times New Roman'
        font1.colour_index = 9

        style1 = xlwt.XFStyle()
        style1.font = font1
        style1.alignment = al

        font2 = xlwt.Font()
        font2.height = 10 * 20
        font2.colour_index = 9
        style2 = xlwt.XFStyle()
        style2.font = font2
        style2.alignment = al

        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 0x21
        style.pattern = pattern
        style1.pattern = pattern
        style2.pattern = pattern

        font_h_1 = xlwt.Font()
        font_h_1.height = 11 * 20
        font_h_1.name = '宋体'
        font_h_1.bold = True
        style_h_1 = xlwt.XFStyle()
        style_h_1.font = font_h_1
        style_h_1.alignment = al
        # style_h_1.alignment.wrap = 1
        pattern_1 = xlwt.Pattern()
        pattern_1.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern_1.pattern_fore_colour = 0x25
        style_h_1.pattern = pattern_1

        font_h_2 = xlwt.Font()
        font_h_2.height = 18 * 20
        font_h_2.name = '宋体'
        font_h_2.bold = True
        style_h_2 = xlwt.XFStyle()
        style_h_2.font = font_h_2
        style_h_2.alignment = al
        pattern_2 = xlwt.Pattern()
        pattern_2.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern_2.pattern_fore_colour = 0x26
        style_h_2.pattern = pattern_2

        x = 3
        y = 0
        d = 0
        index = 1

        day = int(self.days.text())

        paihang.write(2, 0, "序号", style_h_1)
        paihang.write(2, 1, "打卡人", style_h_1)
        paihang.write(2, 2, "近7日打卡天数", style_h_1)
        paihang.write(2, 3, "所在区域", style_h_1)
        paihang.write(2, 4, "获得奖励", style_h_1)

        paihang.write(2, 5, "序号", style_h_1)
        paihang.write(2, 6, "打卡人", style_h_1)
        paihang.write(2, 7, "近7日打卡天数", style_h_1)
        paihang.write(2, 8, "所在区域", style_h_1)
        paihang.write(2, 9, "获得奖励", style_h_1)

        paihang.write(2, 10, "序号", style_h_1)
        paihang.write(2, 11, "打卡人", style_h_1)
        paihang.write(2, 12, "近7日打卡天数", style_h_1)
        paihang.write(2, 13, "所在区域", style_h_1)
        paihang.write(2, 14, "获得奖励", style_h_1)

        title_1 = "Level %s 课前打卡榜单 Day %s" % (self.level.text(), self.days.text())
        title_2 = "-%s战队" % self.zhandui_name.text()
        paihang.write_merge(0, 0, 0, 14, title_1, style_h_2)
        paihang.write_merge(1, 1, 0, 14, title_2, style_h_2)

        for i, item in enumerate(daka_list):
            paihang.write(x, y, index, style)
            paihang.write(x, y + 1, item["name"], style)
            paihang.write(x, y + 2, item["count"], style)

            #if day < int(item["count"]):
            #    day = int(item["count"])

            paihang.write(x, y + 3, self.zone[str(day)][str(item["count"])], style)
            if int(item["count"]) > 0:
                paihang.write(x, y + 4, self.flower * int(item["count"]), style1)
            else:
                paihang.write(x, y + 4, self.flower, style2)

            if x > 40 and d == 0:
                x = 3
                y = 5
                index = 1
                d = 1
                pattern = xlwt.Pattern()
                pattern.pattern = xlwt.Pattern.SOLID_PATTERN
                pattern.pattern_fore_colour = 0x22
                style.pattern = pattern
                style1.pattern = pattern
                style2.pattern = pattern

            elif x > 40 and d == 1:
                x = 3
                y = 10
                index = 1
                d = 2

                pattern = xlwt.Pattern()
                pattern.pattern = xlwt.Pattern.SOLID_PATTERN
                pattern.pattern_fore_colour = 0x23
                style.pattern = pattern
                style1.pattern = pattern
                style2.pattern = pattern
            elif x > 40 and d == 2:

                break;
            # x = 2
            # y = 15
            # index = 1
            # d = 3
            # pattern = xlwt.Pattern()
            # pattern.pattern = xlwt.Pattern.SOLID_PATTERN
            # pattern.pattern_fore_colour = 0x24
            # style.pattern = pattern
            # style1.pattern = pattern
            # style2.pattern = pattern
            elif x > 40 and d == 3:
                break;
            # x = 2
            # y = 20
            # index = 1
            # d = 4
            # pattern = xlwt.Pattern()
            # pattern.pattern = xlwt.Pattern.SOLID_PATTERN
            # pattern.pattern_fore_colour = 5
            # style.pattern = pattern
            # style1.pattern = pattern
            # style2.pattern = pattern
            else:
                x = x + 1
                index = index + 1

        workbook.save(self.bangdan_dir)
        # self.rst_but.setText(self.bangdan_dir)
        self.info_text_s = self.info_text_s + "生成完成 \n\n"
        self.info_text_s = self.info_text_s + "路径：%s \n\n" % self.bangdan_dir
        self.info_text.setText(self.info_text_s)

    def versions(self):
        QMessageBox.information(self, "版本信息", "当前版本为：1.0.1")

    def about_me(self):
        self.child_dialog.show()

    def juan_zeng(self):
        self.juanzeng_dialog.show()



    # def file_is_open(self, filename):
    #     if not os.access(filename, os.F_OK):
    #         return False  # file doesn't exist
    #     h = self._sopen(filename, 0, self._SH_DENYRW, 0)
    #     if h == 3:
    #         self._close(h)
    #         return False  # file is not opened by anyone else
    #     return True  # file is already open

def get_mac_address():
    import uuid
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

def check_license():
    import requests
    formdata = {
        "num": "AUTO",
        "info": "AUTO",
        "mac": get_mac_address()
    }
    headers = {
        "client-type": "571298649840749533"
    }
    url = "http://39.100.3.77:18081/byb/check"
    response = requests.post(url, data=formdata, headers=headers)
    print(response.text)
    if response.status_code == 200 and response.text == "HELLO":
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        logging.info('version: 1.0.1')
        import sys
        check_rst = check_license()
        print("checkrst : %s"%str(check_rst))
        app = QtWidgets.QApplication(sys.argv)
        if not check_rst:
            check_dialog = QDialog()
            check_fail_ui = check_fail_form()
            check_fail_ui.setupUi(check_dialog)
            check_dialog.show()
            sys.exit(app.exec_())
        else:

            MainWindow = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()

            child_dialog = QDialog()
            child_ui = Ui_Form()
            child_ui.setupUi(child_dialog)
            child_dialog.show()
            sys.exit(app.exec_())
    except Exception as e:
        logging.error(str(e))
        s = traceback.format_exc()
        logging.error(s)


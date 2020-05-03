# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denglu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(650, 437)
        Form.setMinimumSize(QtCore.QSize(650, 437))
        Form.setMaximumSize(QtCore.QSize(650, 437))
        Form.setStyleSheet("")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 650, 437))
        self.listView.setStyleSheet("border-image: url(:/bg1/登陆.jpg);")
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 140, 121, 41))
        self.label.setStyleSheet("background-color: rgb(200, 199, 196,200);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 230, 121, 41))
        self.label_2.setStyleSheet("background-color: rgb(200, 194, 186,200);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.zhanghaolineEdit = QtWidgets.QLineEdit(Form)
        self.zhanghaolineEdit.setGeometry(QtCore.QRect(280, 140, 281, 41))
        self.zhanghaolineEdit.setStyleSheet("background-color: rgb(255, 255, 255,80);\n"
"font: 9pt \"Agency FB\";")
        self.zhanghaolineEdit.setObjectName("zhanghaolineEdit")
        self.passwordtext = QtWidgets.QLineEdit(Form)
        self.passwordtext.setGeometry(QtCore.QRect(280, 230, 281, 41))
        self.passwordtext.setStyleSheet("background-color: rgb(255, 255, 255,80);")
        self.passwordtext.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordtext.setObjectName("passwordtext")
        self.denglupushButton = QtWidgets.QPushButton(Form)
        self.denglupushButton.setGeometry(QtCore.QRect(120, 330, 150, 46))
        self.denglupushButton.setObjectName("denglupushButton")
        self.tuichupushButton = QtWidgets.QPushButton(Form)
        self.tuichupushButton.setGeometry(QtCore.QRect(360, 330, 150, 46))
        self.tuichupushButton.setObjectName("tuichupushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 321, 71))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,120);\n"
"font:9pt \"幼圆\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登陆界面"))
        self.label.setText(_translate("Form", "账户"))
        self.label_2.setText(_translate("Form", "密码"))
        self.denglupushButton.setText(_translate("Form", "登陆"))
        self.tuichupushButton.setText(_translate("Form", "退出"))
        self.label_3.setText(_translate("Form", "欢迎使用教师管理系统"))
import images

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 511)
        MainWindow.setMinimumSize(QtCore.QSize(740, 511))
        MainWindow.setMaximumSize(QtCore.QSize(740, 511))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(260, 30, 211, 411))
        self.groupBox.setObjectName("groupBox")
        # 采集
        self.GetGestureButton = QtWidgets.QPushButton(self.groupBox)
        self.GetGestureButton.setGeometry(QtCore.QRect(20, 40, 171, 51))
        self.GetGestureButton.setObjectName("GetGestureButton")
        # 提示
        self.HelpButton = QtWidgets.QPushButton(self.groupBox)
        self.HelpButton.setGeometry(QtCore.QRect(20, 310, 171, 51))
        self.HelpButton.setObjectName("HelpButton")
        # 执行
        self.ExcuteGestureButton = QtWidgets.QPushButton(self.groupBox)
        self.ExcuteGestureButton.setGeometry(QtCore.QRect(20, 170, 171, 51))
        self.ExcuteGestureButton.setObjectName("ExcuteGestureButton")

        # 关闭
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(540, 370, 111, 31))
        self.CloseButton.setObjectName("CloseButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.CloseButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "操作按钮"))
        self.GetGestureButton.setText(_translate("MainWindow", "数据采集"))
        self.HelpButton.setText(_translate("MainWindow", "操作提示"))
        self.ExcuteGestureButton.setText(_translate("MainWindow", "手语翻译"))
        self.CloseButton.setText(_translate("MainWindow", "关闭"))

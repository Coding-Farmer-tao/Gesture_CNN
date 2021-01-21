# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cap_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import Gesture_CNN
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from Frame3 import *
import sys


class mywindow1(Ui_Dialog, QtWidgets.QWidget):
    def __init__(self):
        super(mywindow1, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./ges_ico/frame.ico'))
        self.video_timer = QtCore.QTimer()
        self.photo_pb.clicked.connect(self.display_img)  # 显示每一帧图像
        self.clear_pb.clicked.connect(self.help)

    # 关闭
    def closeEvent(self, QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, "确认", "确认退出吗?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.video_timer.stop()
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

            # 视频流

    def display_img(self):
        Gesture_CNN.auto_pilot()

    def showtxt(self, value):
        self.photo_num.setText(str(value))  # 显示当前采集的照片数量

    def help(self):
        QMessageBox.information(self, "操作提示框", "通过摄像头实时传输模型，然后通过训练好的模型进行实时翻译\n""按键Q可结束.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow1()
    w.setObjectName('Window')
    qssStyle = '''
                  QPushButton[color='gray']{
                  background-color:rgb(205,197,191)
                  }
                  QPushButton[color='same']{
                  background-color:rgb(225,238,238)
                  }
                  #Window{
                  background-color:rgb(162,181,205) 
                  }
             '''
    w.setStyleSheet(qssStyle)
    w.show()
    sys.exit(app.exec_())

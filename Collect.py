# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cap_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import SaveGesture
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from Frame2 import *
import sys


class mywindow(Ui_Dialog, QtWidgets.QWidget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./frame.ico'))
        self.video_timer = QtCore.QTimer()
        self.label_3.setAlignment(Qt.AlignCenter)
        self.photo_pb.clicked.connect(self.display_img)  # 显示每一帧图像
        self.img_list = []  # 保存截图
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
        self.photo_num.setText(str(len(self.img_list)))
        SaveGesture.saveGesture()

        self.photo_num.setText(str(SaveGesture.img.shape[0]))  # 显示当前采集的照片数量
        self.label_7.setText(str(SaveGesture.num_list[0]))  # Fist
        self.label_8.setText(str(SaveGesture.num_list[1]))  # Good
        self.label_9.setText(str(SaveGesture.num_list[2]))  # No
        self.label_10.setText(str(SaveGesture.num_list[3]))  # Three
        self.label_11.setText(str(SaveGesture.num_list[4]))  # Two
        self.label_12.setText(str(SaveGesture.num_list[5]))  # One

    def help(self):
        QMessageBox.information(self, "操作提示框", "通过键盘控制采集各种不同手语样本\n""Q--结束采集保存数据。\n"
                                               "W--Fist\n"
                                               "A--Good\n"
                                               "D--No\n"
                                               "S--Three\n"
                                               "I--Two\n"
                                               "J--One\n"
                                )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mywindow()
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

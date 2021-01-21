from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 580)
        Dialog.setMinimumSize(QtCore.QSize(580, 580))
        Dialog.setMaximumSize(QtCore.QSize(580, 580))
        # 采集照片
        self.photo_pb = QtWidgets.QPushButton(Dialog)
        self.photo_pb.setGeometry(QtCore.QRect(210, 140, 151, 41))
        self.photo_pb.setStyleSheet("font: 14pt \"华文行楷\";")
        self.photo_pb.setObjectName("photo_pb")
        # 操作指南
        self.clear_pb = QtWidgets.QPushButton(Dialog)
        self.clear_pb.setGeometry(QtCore.QRect(210, 190, 151, 41))
        self.clear_pb.setStyleSheet("font: 14pt \"华文行楷\";")
        self.clear_pb.setObjectName("clear_pb")
        self.photo_num = QtWidgets.QLabel(Dialog)
        self.photo_num.setGeometry(QtCore.QRect(360, 240, 21, 41))
        self.photo_num.setText("")
        self.photo_num.setObjectName("photo_num")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "翻译界面"))
        self.photo_pb.setText(_translate("Dialog", "开始"))
        self.clear_pb.setText(_translate("Dialog", "操作提示"))

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QDateTime, QThread
from PyQt5.QtGui import QIcon
from SaveGesture import *
from Frame1 import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)  # 在界面文件Frame中以及根据界面自动定义了
        self.initUI()

    def initUI(self):
        # 给按钮连接槽函数（CloseButton在Frame中自动连接了）
        self.HelpButton.clicked.connect(self.help)

        # 窗口设置美化
        self.setWindowTitle('手语识别')
        self.setWindowIcon(QIcon('./frame.ico'))
        self.resize(750, 485)
        self.groupBox.setAlignment(Qt.AlignCenter)

        # 线程操作用于显示时间
        self.initxianceng()

        # 单独给CloseButton添加标签
        self.CloseButton.setProperty('color', 'gray')  # 自定义标签
        self.GetGestureButton.setProperty('color', 'same')
        self.ExcuteGestureButton.setProperty('color', 'same')
        self.HelpButton.setProperty('color', 'same')

    def closeEvent(self, QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, "确认", "确认退出吗?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    def help(self):
        QMessageBox.information(self, "操作提示框", "数据采集：通过OpenCV和摄像头获取照片。\n"
                                               "手语翻译：根据训练好的模型进行实时翻译。")

    def initxianceng(self):
        # 创建线程
        self.backend = BackendThread()
        # 信号连接槽函数
        self.backend.update_date.connect(self.handleDisplay)
        # 开始线程
        self.backend.start()

    # 将当期时间输出到文本框
    def handleDisplay(self, data):
        self.statusBar().showMessage(data)


# 后台线程更新时间
class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            currTime = date.toString('yyyy-MM-dd hh:mm:ss')
            self.update_date.emit(str(currTime))
            time.sleep(1)  # 推迟执行的1秒


if __name__ == "__main__":
    app = QApplication(sys.argv)  # sys.argv是一个命令行参数列表
    myWin = MyMainWindow()
    myWin.setObjectName('Window')
    # 给窗口背景上色
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
    myWin.setStyleSheet(qssStyle)
    myWin.show()
    sys.exit(app.exec_())

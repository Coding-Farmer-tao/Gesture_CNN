from Main import MyMainWindow
from Collect import mywindow
from Translate import mywindow1
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    child = mywindow()
    child_1 = mywindow1()
    window.setObjectName('Window')
    child.setObjectName('Window')
    child_1.setObjectName('Window')
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
    child_1.setStyleSheet(qssStyle)
    child.setStyleSheet(qssStyle)
    window.setStyleSheet(qssStyle)
    # 通过toolButton将两个窗体关联
    btn = window.GetGestureButton
    btn.clicked.connect(child.show)
    btn_1 = window.ExcuteGestureButton
    btn_1.clicked.connect(child_1.show)
    # 显示
    window.show()
    sys.exit(app.exec_())

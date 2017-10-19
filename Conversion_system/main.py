# !/usr/bin/env python
# -*- encoding:utf-8 -*-


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from  MyWindow import *
from TabWidget import *

app = QtWidgets.QApplication(sys.argv)  # 当前application
window = MyWindow()  # 当前窗口
# tabWiget = Ui_TabWidget()


def createLayout():
    # tabWiget.setupUi(window)
    # window.show()

    # app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('helloworld')
    w.show()
    sys.exit(app.exec_())  # 结束进程


if __name__ == "__main__":
    createLayout()

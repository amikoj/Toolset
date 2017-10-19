# !/usr/bin/env python
# -*-encoding:utf-8 -*-

from PyQt5 import QtWidgets   # QtWidgets通用窗口类

class MyWindow(QtWidgets.QTabWidget):
    def __init__(self):
        print "创建窗口..."
        super(MyWindow,self).__init__()



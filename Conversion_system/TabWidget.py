# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt4.QtCore import Qt
from PyQt5.QtGui import QFont, QBrush
from PyQt5.QtWidgets import QTableWidget


class Ui_TabWidget(object):



    def setupUi(self,TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(962, 618)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(310, 30, 54, 21))
        self.label.setObjectName("label")
        self.fontComboBox = QtWidgets.QFontComboBox(self.tab)
        self.fontComboBox.setGeometry(QtCore.QRect(350, 20, 161, 31))
        self.fontComboBox.setObjectName("fontComboBox")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(530, 20, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 20, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        # self.tableView = QtWidgets.QTableWidget(self.tab)
        # self.tableView.setColumnCount(4)
        # self.tableView.setRowCount(6)
        # self.horizontalHeader = ["2进制","8进制","10进制","16进制"]
        # self.tableView.setHorizontalHeaderLabels(self.horizontalHeader)
        # self.tableView.setEditTriggers(QTableWidget.NoEditTriggers)
        # self.tableView.setSelectionBehavior(QTableWidget.SelectColumns)
        # self.tableView.setSelectionMode(QTableWidget.SingleSelection)
        #
        # for index in range(self.tableView.columnCount()):
        #     headItem = self.tableView.horizontalHeaderItem(index)
        #     headItem.setFont(QFont=QFont("song",12,QFont.Bold))
        #     headItem.setForeground(QBrush(Qt.gray))
        #     headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        #
        # self.tableView.setColumnWidth(4, 100)
        # self.tableView.setRowHeight(0, 40)
        # self.tableView.setObjectName("tableWight")
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        TabWidget.addTab(self.tab1, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        TabWidget.setToolTip(_translate("TabWidget", "<html><head/><body><p>任意进制转换</p></body></html>"))
        self.label.setText(_translate("TabWidget", "进制"))
        self.pushButton.setText(_translate("TabWidget", "Add"))
        self.pushButton_2.setText(_translate("TabWidget", "Clear"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "任意进制转化"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "关于"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supplies.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SuppliesGui(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1231, 871)
        Frame.setStyleSheet("background-color:#eeeeee")
        self.gridLayoutWidget = QtWidgets.QWidget(Frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 100, 1232, 761))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.suppliesLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.suppliesLayout.setContentsMargins(0, 0, 0, 0)
        self.suppliesLayout.setSpacing(0)
        self.suppliesLayout.setObjectName("suppliesLayout")
        self.categoriesLabel = QtWidgets.QLabel(Frame)
        self.categoriesLabel.setGeometry(QtCore.QRect(467, 24, 301, 61))
        self.categoriesLabel.setStyleSheet("font-family: Roboto;\n"
"font-size:40px;\n"
"font-weight:500;\n"
"color:#1E2F97;\n"
"text-align:center;")
        self.categoriesLabel.setObjectName("categoriesLabel")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.categoriesLabel.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:30pt;\">Categories</span></p></body></html>"))

import MainGUI.resources
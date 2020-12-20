# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(703, 554)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_host = QtWidgets.QLineEdit(Form)
        self.lineEdit_host.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.horizontalLayout.addWidget(self.lineEdit_host)
        self.btn_con = QtWidgets.QPushButton(Form)
        self.btn_con.setObjectName("btn_con")
        self.horizontalLayout.addWidget(self.btn_con)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_search = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_2.addWidget(self.lineEdit_search)
        self.btn_sort_up = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sort_up.sizePolicy().hasHeightForWidth())
        self.btn_sort_up.setSizePolicy(sizePolicy)
        self.btn_sort_up.setObjectName("btn_sort_up")
        self.horizontalLayout_2.addWidget(self.btn_sort_up)
        self.btn_sort_down = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sort_down.sizePolicy().hasHeightForWidth())
        self.btn_sort_down.setSizePolicy(sizePolicy)
        self.btn_sort_down.setObjectName("btn_sort_down")
        self.horizontalLayout_2.addWidget(self.btn_sort_down)
        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.listView = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.listView.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.label_count = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_count.setObjectName("label_count")
        self.verticalLayout_2.addWidget(self.label_count)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 13)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_info = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_info.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.textEdit_info.setObjectName("textEdit_info")
        self.verticalLayout.addWidget(self.textEdit_info)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btn_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setMaximumSize(QtCore.QSize(64, 48))
        self.btn_add.setText("")
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_3.addWidget(self.btn_add)
        self.btn_modify = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_modify.sizePolicy().hasHeightForWidth())
        self.btn_modify.setSizePolicy(sizePolicy)
        self.btn_modify.setMaximumSize(QtCore.QSize(64, 48))
        self.btn_modify.setText("")
        self.btn_modify.setObjectName("btn_modify")
        self.horizontalLayout_3.addWidget(self.btn_modify)
        self.btn_del = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        self.btn_del.setMaximumSize(QtCore.QSize(64, 48))
        self.btn_del.setText("")
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout_3.addWidget(self.btn_del)
        self.btn_info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_info.sizePolicy().hasHeightForWidth())
        self.btn_info.setSizePolicy(sizePolicy)
        self.btn_info.setMaximumSize(QtCore.QSize(64, 48))
        self.btn_info.setText("")
        self.btn_info.setObjectName("btn_info")
        self.horizontalLayout_3.addWidget(self.btn_info)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textEdit_value = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_value.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.textEdit_value.setObjectName("textEdit_value")
        self.verticalLayout.addWidget(self.textEdit_value)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 8)
        self.verticalLayout_3.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_host.setText(_translate("Form", "127.0.0.1:6379:0"))
        self.btn_con.setText(_translate("Form", "连接"))
        self.lineEdit_search.setPlaceholderText(_translate("Form", "搜索..."))
        self.btn_sort_up.setText(_translate("Form", "↑"))
        self.btn_sort_down.setText(_translate("Form", "↓"))
        self.label_count.setText(_translate("Form", "KEYS=        "))

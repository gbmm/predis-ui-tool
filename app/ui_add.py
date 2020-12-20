# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 237)
        self.lineEdit_key = QtWidgets.QLineEdit(Form)
        self.lineEdit_key.setGeometry(QtCore.QRect(60, 10, 281, 20))
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 10, 54, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 40, 281, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 54, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit_value = QtWidgets.QTextEdit(Form)
        self.textEdit_value.setGeometry(QtCore.QRect(60, 70, 281, 121))
        self.textEdit_value.setObjectName("textEdit_value")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 200, 71, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "key"))
        self.comboBox.setItemText(0, _translate("Form", "string"))
        self.label_2.setText(_translate("Form", "类型"))
        self.pushButton.setText(_translate("Form", "添加"))

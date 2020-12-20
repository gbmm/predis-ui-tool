# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(742, 561)
        self.label_key0 = QtWidgets.QLabel(Form)
        self.label_key0.setGeometry(QtCore.QRect(60, 30, 181, 91))
        self.label_key0.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"font: 28pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.label_key0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_key0.setObjectName("label_key0")
        self.label_memory = QtWidgets.QLabel(Form)
        self.label_memory.setGeometry(QtCore.QRect(290, 30, 181, 91))
        self.label_memory.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"font: 28pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.label_memory.setAlignment(QtCore.Qt.AlignCenter)
        self.label_memory.setObjectName("label_memory")
        self.label_client = QtWidgets.QLabel(Form)
        self.label_client.setGeometry(QtCore.QRect(510, 30, 181, 91))
        self.label_client.setStyleSheet("background-color: rgb(85, 170, 127);\n"
"font: 28pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.label_client.setAlignment(QtCore.Qt.AlignCenter)
        self.label_client.setObjectName("label_client")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 170, 681, 371))
        self.textEdit.setStyleSheet("font: 14pt \"微软雅黑\";\n"
"color: rgb(89, 89, 89);\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 130, 71, 31))
        self.label_4.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(360, 130, 71, 31))
        self.label_5.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(570, 130, 71, 31))
        self.label_6.setStyleSheet("font: 14pt \"微软雅黑\";")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_key0.setText(_translate("Form", "0"))
        self.label_memory.setText(_translate("Form", "0"))
        self.label_client.setText(_translate("Form", "0"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("Form", "db0:key"))
        self.label_5.setText(_translate("Form", "内存"))
        self.label_6.setText(_translate("Form", "连接数"))

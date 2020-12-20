# -*- coding: utf-8 -*-
# ----------------------
# @file: add_widget.py
# @time: 2019-10-07 21:28
# ----------------------
from .ui_add import Ui_Form
from PyQt5.QtWidgets import QDialog,QMessageBox
from PyQt5.QtCore import pyqtSignal


class AddWidget(QDialog):
    closeInfo = pyqtSignal(str,str,str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('ADD')
        self.ui.pushButton.clicked.connect(self.add)

    def add(self):
        key = self.ui.lineEdit_key.text()
        _type = self.ui.comboBox.currentText()
        value = self.ui.textEdit_value.toPlainText()
        self.closeInfo.emit(key, _type, value)
        self.close()





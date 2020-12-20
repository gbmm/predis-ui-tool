# -*- coding: utf-8 -*-
# ----------------------
# @file: main.py
# @time: 2019-09-28 14:06
# ----------------------
import sys
from PyQt5 import QtWidgets
from app.widget import MainWidget

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWidget()
    MainWindow.show()
    sys.exit(app.exec_())

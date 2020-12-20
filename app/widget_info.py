# -*- coding: utf-8 -*-
# ----------------------
# @file: widget_info.py
# @time: 2019-10-11 21:25
# ----------------------

import json
import redis
from .ui_info import Ui_Form
from PyQt5.QtWidgets import  QWidget


class InfoWidget(QWidget):
    def __init__(self, pool):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('信息')
        self.redis_pool = pool
        self.show_redis_info()

    def show_redis_info(self):
        r = redis.Redis(connection_pool=self.redis_pool)
        info = r.info()
        self.ui.label_key0.setText(str(info['db0']['keys']))
        self.ui.label_memory.setText(info['used_memory_rss_human'])
        self.ui.label_client.setText(str(info['connected_clients']))
        self.ui.textEdit.setText(json.dumps(info, sort_keys=True, indent=3))

    def closeEvent(self, e):
        self.deleteLater()

# -*- coding: utf-8 -*-
# ----------------------
# @file: widget.py
# @time: 2019-09-28 15:30
# ----------------------
import json
import redis
import pickle
import PyQt5.sip
from .ui_widget import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QAbstractItemView, \
    QCompleter, QMessageBox, QSplitter
from PyQt5 import QtCore, Qt
from .widget_add import AddWidget
from .widget_info import InfoWidget
from .redis_ import get_redis_connect


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        desk = QApplication.desktop().availableGeometry()
        self.setGeometry(100, 50, int(desk.width() * 0.8), int(desk.height() * 0.9))

        self.add_widget = None
        self.redis_pool = None
        self.timer = QtCore.QTimer()
        self.list_keys = []
        self.model = None
        self.set_ui()
        self.init_data()

    def init_data(self):
        try:
            with open('config.json', 'r') as f:
                data = json.load(f)
                self.ui.lineEdit_host.setText(data.get('host', '127.0.0.1:6379:0'))
        except json.JSONDecodeError:
            pass

    def init_redis(self, host, port, db=0):
        if self.redis_pool is not None:
            del self.redis_pool
            self.redis_pool = None
        self.redis_pool = redis.ConnectionPool(host=host, port=port, db=db)

    def set_ui(self):
        # UI
        self.setWindowTitle('REDIS CLI UI')
        self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.completer = QCompleter()
        self.completer.popup().setStyleSheet("background-color:#fdffdf;")
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.lineEdit_search.setCompleter(self.completer)

        self.ui.splitter.setStretchFactor(0, 3.5)
        self.ui.splitter.setStretchFactor(1, 6.5)

        self.ui.btn_del.setStyleSheet("QPushButton{border-image: url(img/del_u.png)}"
                                      "QPushButton:pressed{border-image: url(img/del_d.png)}")
        self.ui.btn_add.setStyleSheet("QPushButton{border-image: url(img/add_u.png)}"
                                      "QPushButton:pressed{border-image: url(img/add_d.png)}")
        self.ui.btn_modify.setStyleSheet("QPushButton{border-image: url(img/put_u.png)}"
                                         "QPushButton:pressed{border-image: url(img/put_d.png)}")
        self.ui.btn_info.setStyleSheet("QPushButton{border-image: url(img/info_u.png)}"
                                       "QPushButton:pressed{border-image: url(img/info_d.png)}")

        # 定时器
        self.timer.timeout.connect(self.show_db_size)

        # 信号
        self.ui.listView.doubleClicked.connect(self.list_clicked)
        # self.completer.activated[QtCore.QModelIndex].connect(self.list_clicked)
        self.completer.activated[str].connect(self.completer_clicked)
        self.ui.btn_con.clicked.connect(self.btn_con_clicked)
        self.ui.btn_del.clicked.connect(self.btn_del_clicked)
        self.ui.btn_modify.clicked.connect(self.btn_modify_clicked)
        self.ui.btn_add.clicked.connect(self.btn_add_clicked)
        self.ui.btn_info.clicked.connect(self.btn_info_clicked)
        self.ui.btn_sort_up.clicked.connect(self.sort_up)
        self.ui.btn_sort_down.clicked.connect(self.sort_down)

        self.timer.start(1000)

    def set_list_key(self, keys=[]):
        """设置lisview"""
        self.list_keys = [one.decode() for one in keys]
        if self.model is not None:
            del self.model
        self.model = QtCore.QStringListModel()
        self.model.setStringList(self.list_keys)
        self.ui.listView.setModel(self.model)
        self.completer.setModel(self.model)
        self.ui.label_count.setText('KEYS=%s' % len(self.list_keys))

    def btn_con_clicked(self):
        info = self.ui.lineEdit_host.text()
        cfg = json.loads(info)
        r = get_redis_connect(cfg)
        # host, port, db = info.split(':')
        # self.init_redis(host, int(port), int(db))
        # r = get_redis_connect()
        self.set_list_key(r.scan_iter('*'))

    def completer_clicked(self, key):
        r = get_redis_connect()
        _type = r.type(key).decode()
        key_info = "[1] 键名: {0}\n" \
                   "[2] 类型: {1}\n" \
                   "[3] TTL : {2}\n".format(key, _type, r.ttl(key))
        self.ui.textEdit_info.setText(key_info)
        self.ui.textEdit_value.setText(self.read_value(_type, key))

    def list_clicked(self, model_index):
        # print(model_index.row())
        key = self.list_keys[model_index.row()]
        r = get_redis_connect()
        _type = r.type(key).decode()
        key_info = "[1] 键名: {0}\n" \
                   "[2] 类型: {1}\n" \
                   "[3] TTL : {2}\n".format(key, _type, r.ttl(key))
        self.ui.textEdit_info.setText(key_info)
        self.ui.textEdit_value.setText(self.read_value(_type, key))
        # QMessageBox.information(self, '选择', '你选择了：' + self.list_keys[model_index.row()])

    def load_object(self, value):
        """The reversal of :meth:`dump_object`.  This might be called with
        None.
        """
        if value is None:
            return None

        try:
            return json.dumps(pickle.loads(value), sort_keys=True, indent=4, separators=(',', ':'))
        except:
            return value
        #
        # try:
        #     return int(value)
        # except ValueError:
        #     # before 0.8 we did not have serialization.  Still support that.
        #     return value

    def read_value(self, v_type, key):
        r = get_redis_connect()
        if v_type == 'string':
            try:
                return str(self.load_object(r.get(key)))
            except:
                return str(r.get(key))
        if v_type == 'list':
            try:
                v = [one.decode() for one in r.lrange(key, 0, -1)]
            except:
                v = [one for one in r.lrange(key, 0, -1)]
            return json.dumps(v, sort_keys=True, indent=4)
        if v_type == 'hash':
            try:
                r = {k.decode(): v.decode() for k, v in r.hgetall(key).items()}
            except:
                r = {str(k): str(v) for k, v in r.hgetall(key).items()}
            return json.dumps(r, sort_keys=True, indent=4)
        if v_type == 'set':
            try:
                return str({v.decode() for v in r.smembers(key)})
            except:
                return str({v for v in r.smembers(key)})
        if v_type == 'zset':
            try:
                return str([(v[0].decode(), v[1]) for v in r.zrange(key, 0, -1, withscores=True)])
            except:
                return str([(v[0], v[1]) for v in r.zrange(key, 0, -1, withscores=True)])

    def get_current_key(self):
        info = self.ui.textEdit_info.toPlainText()
        tmp = info.split('\n')
        if len(tmp) < 3:
            QMessageBox.warning(self, '警告', 'key不正确', QMessageBox.Yes)
            return None, None
        return tmp[0].split(':')[-1].strip(), tmp[1].split(':')[-1].strip()

    def btn_del_clicked(self):
        """删除key"""
        key, _type = self.get_current_key()
        if key is None:
            return
        reply = QMessageBox.question(self, '删除', '确定删除？' + key, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            r = get_redis_connect()
            r.delete(key)
            self.ui.textEdit_info.clear()
            self.ui.textEdit_value.clear()
            self.set_list_key(r.keys('*'))

    def btn_modify_clicked(self):
        """修改数据"""
        key, _type = self.get_current_key()
        if key is None:
            return
        r = get_redis_connect()
        if _type == 'string':
            r.set(key, self.ui.textEdit_value.toPlainText())
            QMessageBox.question(self, '修改', '修改成功！' + key, QMessageBox.Yes)
        else:
            QMessageBox.question(self, '修改', '非string类型不能修改！', QMessageBox.Yes)

    def btn_add_clicked(self):
        self.add_widget = AddWidget()
        self.add_widget.closeInfo.connect(self.add_value)
        self.add_widget.showNormal()
        self.add_widget.exec()
        del self.add_widget
        self.add_widget = None

    def add_value(self, key, _type, value):
        r = get_redis_connect()
        if _type == "string":
            r.set(key, value)
            self.set_list_key(r.keys('*'))

    def closeEvent(self, e):
        url = self.ui.lineEdit_host.text()
        with open('config.json', 'w+') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = dict()
            data['host'] = url
            f.write(json.dumps(data))

    def btn_info_clicked(self):
        self.info_widget = InfoWidget(self.redis_pool)
        self.info_widget.show()
        # self.info_widget.exec()
        # del self.info_widget
        # self.info_widget = None

    def sort_up(self):
        """key 排序 up"""
        self.list_keys.sort()
        self.model.setStringList(self.list_keys)

    def sort_down(self):
        """key 排序 down"""
        self.list_keys.sort(reverse=True)
        self.model.setStringList(self.list_keys)

    def show_db_size(self):
        if self.model is not None:
            r = get_redis_connect()
            self.ui.label_count.setText('KEYS=%s' % r.dbsize())
            if r.dbsize() != len(self.list_keys):
                self.set_list_key(r.scan_iter('*'))

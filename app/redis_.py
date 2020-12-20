# -*- coding: utf-8 -*-
# ----------------------------------
# @Time    : 2020/12/17 20:30
# @File    : redis_.py
# ----------------------------------
import redis
import pickle
from redis.sentinel import Sentinel

REDIS_CFG = {
    "type": '0',  # 0 正常模式 1哨兵模式
    "host": "",
    "pass": "",
    "port": "",
    "name": "",
    "db": ""
}

pool = None
CFG = None


def get_redis_connect(cfg={}):
    """
    获取连接
    :param cfg:
    :return:
    """
    global pool
    global CFG
    if CFG is None:
        CFG = cfg
    else:
        cfg = CFG
    try:
        if cfg.get('type', 'normal') == 'normal':
            if pool is None:
                pool = redis.ConnectionPool(host=cfg['host'],
                                            port=cfg['port'],
                                            password=cfg['pass'],
                                            db=cfg['db'])
            con = redis.Redis(connection_pool=pool)
            return con
        else:
            if pool is None:
                pool = Sentinel(cfg['host'], socket_timeout=0.5)
            con = pool.master_for(cfg['name'],
                                  socket_timeout=0.5,
                                  password=cfg['pass'],
                                  db=cfg['db'])
            return con
    except Exception as e:
        print(e)
        raise e

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import logging
from config.conf import LOG_PATH
from tools.times import datetime_strftime


class Log(object):
    def __init__(self):
        self.logger = logging.getLogger()  # 初始化,创建日志对象
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

        # 创建一个handle将日志写入文件对象
        fh = logging.FileHandler(self.log_path, encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 创建一个handle将日志输出到控制台对象
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志输出格式
        formatter = logging.Formatter(self.fmt)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # logger日志对象加载2个流对象
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    @property
    def log_path(self):
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        return os.path.join(LOG_PATH, '{}.log'.format(datetime_strftime()))

    @property
    def fmt(self):
        return '%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s'


log = Log().logger

if __name__ == '__main__':
    log.info('你好')
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import configparser
from config.conf import INI_PATH

HOST = 'HOST'
username = 'username'
password = 'password'


class ReadConfig:
    """配置文件"""

    def __init__(self):
        if not os.path.exists(INI_PATH):
            raise FileNotFoundError("配置文件%s不存在!" % INI_PATH)
        self.config = configparser.RawConfigParser()
        self.config.read(INI_PATH, encoding='utf-8')

    def _get(self, section, option):
        """获取"""
        return self.config.get(section, option)

    def _set(self, section, option, value):
        """更新"""
        self.config.set(section, option, value)
        with open(INI_PATH, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)

    @property
    def username(self):
        return self._get(username, username)

    @property
    def password(self):
        return self._get(password, password)


ini = ReadConfig()
if __name__ == '__main__':
    print(ini.url)
    print(ini.username)
    print(ini.password)

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

login = Element('login')


class LoginPage(WebPage):
    """登录类"""

    def login(self, username, password):
        """输入用户名，密码"""
        self.input_text(login['用户名'], txt=username)
        self.input_text(login['密码'], txt=password)
        sleep()

    def click_login(self):
        """点击登录"""
        self.is_click(login['登录按钮'])


if __name__ == '__main__':
    pass

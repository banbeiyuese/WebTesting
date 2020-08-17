#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import os
import pytest
import allure
from tools.logger import log
from common.readconfig import ini
from tools.times import sleep
from page_object.loginpage import LoginPage
from page_object.homepage import HomePage, OrgMenu


@allure.feature("测试登录模块")
class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_page(self, drivers):
        """打开登录页面"""
        search = LoginPage(drivers)
        search.get_url(ini.url)

    @allure.story("登录测试用例")
    def test_001(self, drivers):
        """测试登录成功"""
        login = LoginPage(drivers)
        login.login(ini.username, ini.password)
        login.click_login()
        sleep(5)
        info = re.search(r'赵春艳1', login.get_source)
        assert info


class TestBackground:
    @allure.story("进入企业后台测试用例")
    def test_002(self, drivers):
        """测试进入企业后台成功"""
        homepage = HomePage(drivers)
        homepage.enter_corporate_background()
        # info = re.search(r'创建及管理社区', homepage.get_source)
        # assert info

    # @allure.story("进入组织类型管理页面测试用例")
    # def test_003(self, drivers):
    #     """测试进入组织类型管理页面成功"""
    #     org = OrgMenu(drivers)
    #     org.create_and_manage_communities()
    #     org.organization_type_management()
    #     sleep(5)
    #
    # @allure.story("进入新增组织类型窗口")
    # def test_004(self, drivers):
    #     """测试点击新增按钮，弹出新增组织类型窗口"""
    #     org = OrgMenu(drivers)
    #     org.new_button()
    #     sleep(3)


if __name__ == '__main__':
    pytest.main(['TestCase/test_login.py'])
    os.system('allure serve report/allure')

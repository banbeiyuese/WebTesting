#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from common.readelement import Element
from page.webpage import WebPage
from tools.times import sleep
homepage = Element('homepage')


class HomePage(WebPage):
    """首页类"""

    def switching_unit(self):
        """切换单位"""
        self.move_to_element(homepage['切换单位按钮'])
        self.is_click(homepage['春艳之家222'])

    def enter_corporate_background(self):
        """进入企业后台"""
        self.move_to_element(homepage['后台按钮'])
        sleep(3)
        # self.is_click(homepage['企业管理'])

    def enter_community_background(self):
        """进入社区后台"""
        self.is_click(homepage['社区后台'])


class OrgMenu(WebPage):
    """组织类型管理菜单类"""

    def create_and_manage_communities(self):
        """创建及管理社区菜单"""
        self.is_click(homepage['创建及管理社区菜单'])

    def organization_type_management(self):
        """组织类型管理"""
        self.is_click(homepage['组织类型管理'])

    def new_button(self):
        """新增组织类型"""
        self.is_click(homepage['新增组织类型'])

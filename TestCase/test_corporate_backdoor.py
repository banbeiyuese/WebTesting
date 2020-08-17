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
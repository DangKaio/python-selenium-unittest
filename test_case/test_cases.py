#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-08-29 14:35:26
# @Last Modified time: 2018-09-20 10:52:44
# @E-mail: 1370465454@qq.com
# @Description:
import time
from time import sleep
import sys
sys.path.append('../')
from common import my_test
import unittest
from base_page import IndexPage_handle


class OpenHideLocators:
    # 隐藏的属性需要更改之后才能获取到
    js = "document.getElementById('checkWay').style.display='block'"
    # js1 = "document.getElementById('js-signin-btn').click()"


class Page_Login(my_test.My_Test):

    def test_1login_success(self):
        '''登陆成功,username名字  password密码'''
        IndexPage_handle.login(self, "username", "password")
        sleep(3)
        # self.dr.execute_script(OpenHideLocators.js1)
        # time.sleep(10)
        self.dr.find_element_by_css_selector(
            "#captchaBox > div > div.geetest_btn > div.geetest_radar_btn > div.geetest_radar_tip").click()
        time.sleep(10)
        # links = self.dr.find_element_by_css_selector("#input1").sendkey()
        # for link in links:
        #     if not "_blank" in link.get_attribute("target") and ("google" in link.get_attribute("href") or not "http" in link.get_attribute("href")):
        #         link.click()

        #         self.dr.back()
        # self.dr.find_element_by_id("js-signin-btn").click()
        # sleep(5)
        # self.dr.execute_script(OpenHideLocators.js1)
        # self.dr.find_element_by_link_text("登录").click()
        # self.dr.find_element_by_partial_link_text("登录").click()
        # # self.dr.find_element_by_xpath("//*[@id="js-signin-btn"]").click()

    @unittest.skip("I don't want to run this case.")
    def test_2login_pwd_error(self):
        '''密码错误'''
        # self.dr.get_screenshot_as_file(self.save_path + "login_pwd_error.png")
        # 用assertTrue(x)方法来断言  bool(x) is True 登录成功后固定字段span里

    @unittest.skip("I don't want to run this case.")
    def test_3login_pwd_null(self):
        '''密码为空'''
        # self.dr.get_screenshot_as_file(self.save_path + "login_pwd_null.png")

    @unittest.skip("I don't want to run this case.")
    def test_4login_user_error(self):  # 账号不存在
        '''账号不存在'''
        # self.dr.get_screenshot_as_file(self.save_path + "login_user_null.png")

    @unittest.skip("I don't want to run this case.")
    def test_5login_user_null(self):
        '''账号为空'''
        # self.dr.get_screenshot_as_file(self.save_path + "login_user_null.png")

    @unittest.skip("I don't want to run this case.")
    def test_6exit(self):
        '''用户退出'''
        # self.dr.get_screenshot_as_file(self.save_path + "login_user_exit.png")

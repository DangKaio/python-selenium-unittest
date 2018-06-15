#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/5/22 17:25
# @Email   : 1370465454@qq.com
# @File    : log.py
# @Description:将测试用例初始化分离出来

import unittest
import sys
sys.path.append('../')
from common.pyselenium import PySelenium
from config import globalparam
# sys.path.append(globalparam.config_file_path)
from common.log import Log
logger = Log()


class My_Test(unittest.TestCase):
    """docstring for My_Test"""
    # def __init__(self, arg):
    #     super(My_Test, self).__init__()
    #     self.arg = arg
    driver=PySelenium.browser(globalparam.browser)
    @classmethod#增加装饰器来满足每个用例浏览器一次启动一次退出
    def setUpClass(cls,dr=driver):
        cls.dr=dr
        cls.logger = Log()
        cls.logger.info(
            '############################### START ###############################')
        # self.dr = pyselenium.PySelenium.browser(globalparam.browser)
        # self.dr=dr#将全局变量赋值给dr,锁定dr
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(30)
        cls.dr.verificationErrors =[]
        cls.dr.accept_next_alert =True

    @classmethod
    def tearDownClass(cls):
        cls.logger.info(
            '############################### END ###############################')
        cls.driver.refresh()#将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
        # cls.dr.quit()
    # # driver=pyselenium.PySelenium.browser(globalparam.browser)#全局定义driver,实现了一次启动
    # def setUp(self,dr=driver):
    #     self.logger = Log()
    #     self.logger.info(
    #         '############################### START ###############################')
    #     # self.dr = pyselenium.PySelenium.browser(globalparam.browser)
    #     self.dr=dr#将全局变量赋值给dr,锁定dr
    #     self.dr.maximize_window()
    #     self.dr.implicitly_wait(30)
    #     self.verificationErrors =[]
    #     self.accept_next_alert =True
        
    # def tearDown(self):
    #     self.logger.info(
    #         '############################### End ###############################')
    #     try:
    #         self.driver.refresh()#将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
    #     except ConnectionRefusedError as e:
    #         print(e)
    #     finally:
    #         self.assertEqual([], self.verificationErrors)
        

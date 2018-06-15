#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/5/22 17:25
# @Email   : 1370465454@qq.com
# @File    : log.py
# @Description:

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *  # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
sys.path.append('../')
from config import globalparam


class PySelenium(object):
    original_window = None

    def __init__(self, driver):  # ,base_url,pagetitle
        """
        :param driver:打开浏览器驱动
        :param base_url:输入测试url
        :param pagetitle:输入页面title
        """
        self.driver = driver
        # self.base_url = base_url
        # self.pagetitle = pagetitle

    def browser(browser="Chrome"):
        """打开浏览器函数，Firefox，chrome，IE，phantomjs
           默认Chrome浏览器
        """
        try:
            if browser == "Chrome":
                options = webdriver.ChromeOptions()
                prefs = {'profile.default_content_settings.popups': 0,
                         'download.default_directory': globalparam.download_path}
                options.add_experimental_option('prefs', prefs)
                # cap=webdriver.DesiredCapabilities.CHROME()
                # cap..set
                driver = webdriver.Chrome(chrome_options=options)
                return driver
            elif browser == "firefox":
                driver = webdriver.Firefox()
                return driver
            elif browser == "IE":
                driver = webdriver.Ie()
                return driver
            else:
                print("找不到驱动")
        except Exception as msg:
            print("%s" % msg)

    def browser_back():
        """浏览器后退"""
        self.driver.back()

    def browser_forward():
        """浏览器前进"""
        self.driver.forward()

    def open_url(self,url):
        """打开站点"""
        self.driver.get(url)

    if __name__ == '__main__':
        open_url(self,"https://www.imooc.com/")

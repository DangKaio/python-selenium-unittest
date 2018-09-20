#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/5/23 17:25
# @Email   : 1370465454@qq.com
# @File    : log.py
# @Description:将测试用例初始化分离出来
from time import sleep
import sys
sys.path.append('../')
from config import globalparam

class IndexPage_handle:
    def login(self, username, password):
        # 登录页面
        self.dr.get(globalparam.base_url)
        self.dr.find_element_by_css_selector('#span_userinfo > a:nth-child(1)').click()
        self.dr.find_element_by_css_selector('#input1').send_keys(username)
        # # PySelenium.get_element(self, 'id->userId').clear()
        # # PySelenium.get_element(self, 'id->userId').send_keys(username)
        # self.dr.find_element_by_css_selector('#input2').clear()
        self.dr.find_element_by_css_selector('#input2').send_keys(password)
        self.dr.find_element_by_css_selector('#signin').click()

    def login_cookies(self):
        '''使用cookies登录'''
        self.dr.get(globalparam.base_url)
        print(self.dr.get_cookies())

    def input_search_key(self,values):
        """输入搜索关键词"""
        self.dr.clear_type('id->kw',values)
    def click_search_button(self):
        """点击搜索按钮"""
        self.dr.click('id->su')
    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()
    if __name__ == '__main__':
        login_cookies(self)












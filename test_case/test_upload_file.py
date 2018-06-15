#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/5/24 17:25
# @Email   : 1370465454@qq.com
# @File    : log.py
# @Description:
from time import sleep
import sys
sys.path.append("../")
from common import my_test,publicfunction
from config import globalparam
# sys.path.append(globalparam.config_file_path)
import unittest


class Yuexiu_Upload_File(my_test.My_Test):
    @unittest.skip("I don't want to run this case.")
    def test_upload_File(self):
        '''上传文件成功'''
        login(self, 'admin', 'admin')
        sleep(2)
        self.dr.switch_to.frame('PageContainer')
        upload = self.dr.find_element_by_css_selector('#SelectFileInput')
        upload.send_keys('D:\\Pyproject\\Test_Login\\companyInfo.xlsx')
        sleep(2)
        self.dr.find_element_by_id('UploadBtn').click()
        sleep(2)
    @unittest.skip("I don't want to run this case.")
    def test_upload_fail(self):
        '''不上传任何文件'''
        login(self, 'admin', 'admin')
        sleep(2)
        self.dr.switch_to.frame('PageContainer')
        self.dr.find_element_by_id('UploadBtn').click()
        alert = self.dr.switch_to.alert  # 处理js弹窗
        sleep(2)
        # print(alert.text)
        self.assertEqual("请选择文件", alert.text)
        alert.accept()  # alert对话框属于警告对话框，我们这里只能接受弹窗
    @unittest.skip("I don't want to run this case.")
    def test_upload_file_jpg(self):
        '''不上传任何文件'''
        login(self, 'admin', 'admin')
        sleep(2)
        self.dr.switch_to.frame('PageContainer')
        upload = self.dr.find_element_by_css_selector('#SelectFileInput')
        upload.send_keys('D:\\Pyproject\\Test_Login\\ReadMe.md')
        sleep(2)
        self.dr.find_element_by_id('UploadBtn').click()
        alert = self.dr.switch_to.alert  # 处理js弹窗
        print(alert.text)
        sleep(2)
        try:
            self.assertEqual("只持.xlsx格式文件", alert.text)
            # alert.accept()  # alert对话框属于警告对话框，我们这里只能接受弹窗
        except AssertionError as e:
            # print(sys._getframe().f_code.co_name)
            # alert.accept()
            # publicfunction.get_img(self.dr, sys._getframe().f_code.co_name)
            publicfunction.window_screenshoot(sys._getframe().f_code.co_name)
    @unittest.skip("I don't want to run this case.")
    def test_download(self):
        '''下载模板'''

        login(self, 'admin', 'admin')
        sleep(2)
        self.dr.switch_to.frame('PageContainer')
        self.dr.find_element_by_css_selector('#DowmLoadBtn').click()
        sleep(20)
if __name__ == '__main__':
    # unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，如果设为
    # 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果
    unittest.main()
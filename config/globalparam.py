#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/5/22 17:25
# @Email   : 1370465454@qq.com
# @File    : log.py
# @Description:定义一些默认参数、路径等
import sys
import os
sys.path.append('../')
prj_path = os.getcwd()
# config_file_path = os.path.split(os.path.realpath(__file__))[0]
# print(config_file_path)
# read_config = Read_Config(os.path.join(config_file_path, 'config.ini'))
# # 项目参数设置
# prj_path = read_config.get_Value('projectConfig', 'project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'Log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'test_report')
# 默认浏览器
browser = 'Chrome'
# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'test_data')
# 浏览器地址
base_url = 'https://www.cnblogs.com/'
# base_success_url='http:******'
# 上传文件路径(包括上传文件名+后缀)
upload_file_path = os.path.join(prj_path, 'data', 'upload')
# 下载路径
download_path = os.path.join(prj_path, 'data', 'download')

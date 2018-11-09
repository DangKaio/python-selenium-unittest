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
base_url = ''
# base_success_url='http:******'
# 上传文件路径(包括上传文件名+后缀)
upload_file_path = os.path.join(prj_path, 'data', 'upload')
# 下载路径
download_path = os.path.join(prj_path, 'data', 'download')

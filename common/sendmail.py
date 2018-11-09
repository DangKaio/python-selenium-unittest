#!user/bin/env python
# coding=utf-8
# @Author  : Dang
# @Time    : 2018/5/22 17:25
# @Email   : 1370465454@qq.com
# @File    : log.py
# @Description:

import os
import sys
sys.path.append("../")
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import globalparam
from common.log import Log
# 测试报告的路径
reportPath = globalparam.report_path
# 配置收发件人
recvaddress = ['1370465454@qq.com']
# 163的用户名和密码
sendaddr_name = ''
sendaddr_pswd = ''
logger = Log()


class Send_Mail:

    def __init__(self, recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(reportPath)
        # print(dirs)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname

    def __take_messages(self):
        """生成邮件的内容，和html报告附件"""
        newreport = self.__get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '测试报告主题'
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
        self.msg.attach(html)

        # html附件
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = '"attachment; filename="' + \
            self.msg['date'] + "TestReport.html"
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name
        try:
            smtp = smtplib.SMTP('服务器地址')
            smtp.login(sendaddr_name, sendaddr_pswd)
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string())
            smtp.close()
            logger.info("发送邮件成功")
        except Exception:
            logger.error('发送邮件失败')
            raise

if __name__ == '__main__':
    sendMail = Send_Mail()
    sendMail.send()

#!user/bin/env python
# coding=utf-8

import configparser
import codecs


class Read_Config:
    '''专门读取配置文件的,.ini文件格式'''

    def __init__(self, filename):
        configpath = filename
        fd = open(configpath,'r',encoding='gbk')
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codes.open(configpath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_Value(self, env, name):
        """
        [projectConfig]
        project_path=D:\Pyproject\Test_Login
        :param env:[projectConfig]
        "param name:project_path"
        :return:D:\Pyproject\Test_Login
        """
        return self.cf.get(env, name)

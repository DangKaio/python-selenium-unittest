#!user/bin/env python
# coding=utf-8
# @Author  : DangKai
# @Time    : 2018/6/10 17:25
# @Email   : 1370465454@qq.com
# @File    :
# @Description:给文件添加头信息

import os
import time


def file_path(path):

    dirs = os.listdir(path)
    for i in range(len(dirs)):
        # print(dirs[i])
        open_file(dirs[i])
    
    


def open_file(filename):
    f = open(filename, "r+",encoding='UTF-8')
    f.seek(0, 0)
    # print(f.read())
    content = ["#!user/bin/env python\n", "# coding=utf-8\n", "# @Author  : DangKai\n",
               "# @Time    : " + time.strftime('%Y/%m/%d %H:%M:%S') + "\n",
               "# @Email   : 1370465454@qq.com\n", "# @File    :" + filename + "\n", "# @Description:\n"]
    
    lines= f.readlines()
    if lines!=[]:
        if content[0]==lines[0] and content[1]==lines[1] and content[2]==lines[2]:
            print("%s 文件已存在该内容" % filename)
        else:
            f.writelines(content)
    else:
        f.writelines(content)
    f.close()
    # print(content[0])
    # print(lines)
if __name__ == '__main__':
    file_path("D:\\Pyproject\\linux_login")
    # open_file("login.py")
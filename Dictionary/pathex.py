# -*- coding:UTF-8 -*-

import os
import sys

#获取当前执行文件绝对路径
def getCurrentPath():
    #当前程序执行的绝对路径
    #root = os.path.abspath(os.path.dirname(sys.argv[0]))
    root = os.path.abspath('.')
    return root
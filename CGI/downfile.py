# -*- coding:UTF-8 -*-

import Dictionary.direx as direx, Dictionary.pathex as pathex
import os

#获取当前文件执行路径
root = pathex.getCurrentPath()
#构造文件存储目录
fileTmpDir = os.path.join(root, 'tempdir')

file = '{}\PostMain.html'.format(fileTmpDir)

print('Content-Disposition: attachment;filename="file"\r\n\r\n')

fo = open(file, 'rb')
str = fo.read()

print(str)

fo.close()

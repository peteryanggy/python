# -*- coding:UTF-8 -*-

import Dictionary.direx as direx, Dictionary.pathex as pathex
import os


#获取当前文件执行路径
root = pathex.getCurrentPath()
fileTmpDir = os.path.join(root, 'tmp')
#创建文件目录
direx.mkdir(fileTmpDir)

print(root)
print(fileTmpDir)


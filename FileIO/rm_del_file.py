# -*- coding: UTF-8 -*-

'''
重命名和删除文件
'''

import os

filename = "F:\Tmp\earth-globe.png"
filename_new = "F:\Tmp\earth-globe_new.png"

#文件重命名
#os.rename(filename, filename_new)

#删除文件
#os.remove(filename_new)

#目录操作

dir_new = 'F:\Tmp\python'
#os.mkdir(dir_new)   #在一个已存在的目录下创建新的文件夹

print(os.getcwd())  #os.getcwd() 显示当前工作目录

#os.rmdir(dir_new)   #删除文件夹，必须确保文件夹里面没有任何文件，才可正常删除文件夹


print('os.access')
print('F_OK:{}'.format(os.access(dir_new, os.F_OK)))    #存在
print('R_OK:{}'.format(os.access(dir_new, os.R_OK)))    #可读
print('W_OK:{}'.format(os.access(dir_new, os.W_OK)))    #可写
print('X_OK:{}'.format(os.access(dir_new, os.X_OK)))    #可执行

#修改文件或目录权限
import sys, stat

os.chmod(dir_new, stat.S_IXGRP) #设置文件可以通过用户组执行
os.chmod(dir_new, stat.S_IWOTH) #设置文件可以被其他用户写入

print('setting success!')







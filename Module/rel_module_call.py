# -*- coding: UTF-8 -*-

import sys

print('sys.argv:{}'.format(sys.argv)) #是一个List,包含所有命令行参数
#sys.stdout sys.stdin sys.stderr    #分别表示标准输出、输入、错误输出的文件
#a = sys.stdin.readline()    #从标准输入读取一行
#sys.stdout.write(a)         #输出

#sys.exit(0) #退出程序

print('sys.modules():{}'.format(sys.modules.keys()))    #表示系统中所有可能的module

print('sys.platform:{}'.format(sys.platform))   #获取运行的操作系统的环境

print('sys.path:{}'.format(sys.path))   #表示所有查找到的module、package的路径

print('')

import os

print('os.environ:{}'.format(os.environ))   #包含环境变量的映射关系

print('os.environ["TMP"]:{}'.format(os.environ["TMP"]))   #得到环境变量TMP的值
print('os.environ["USERNAME"]:{}'.format(os.environ["USERNAME"]))

#os.chdir('f:\\Tmp') #改变当前目录

print('os.getcwd:{}'.format(os.getcwd()))   #获取当前目录
#print('os.getegid:{}'.format(os.getegid())) #获取有效组id
#print('os.getgid:{}'.format(os.getgid()))   #获取组id

#print('os.getgruops():{}'.format(os.getgroups()))   #获取用户组名称列表














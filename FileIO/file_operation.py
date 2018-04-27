# -*- coding: UTF-8 -*-

#文件读取+写入操作

file = open("F:\Tmp\python-file.txt", 'r+', 500)

print('文件名称:{}'.format(file.name))
print('是否已关闭:{}'.format(file.closed))
print('访问模式:{}'.format(file.mode))
print('末尾是否强制加空格:{}'.format(file.softspace))

import time,datetime

tm = datetime.datetime.now()

file.write('{} \r\nwww.baidu.com!\nVery good site!'.format(tm)) #写入

content = file.read()
print('content:{}'.format(content))
file.seek(0)

#循环读取每一行
print('\r\n循环读取文件中的每一行:')
done = 0
while not done:
    aline = file.readline()
    if(aline != ''):
        print(aline)
    else:
        done = 1

file.seek(0)
#读取全部内容
lines = file.readlines()
print('\r\nlines:{}'.format(lines))

print('for line file:')
file.seek(0)
for line in file:
    if(line == ''): break
    print(line)

file.close()    #关闭文件
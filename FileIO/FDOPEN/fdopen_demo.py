# -*- coding: UTF-8 -*-

import os, sys

# 打开文件
fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )

# 获取以上文件的对象
fo = os.fdopen(fd, "w+", 100)

# 获取当前文章
print "Current I/O pointer position :%d" % fo.tell()

# 写入字符串
wlen =os.write(fd, "Python is a great language.\nYeah its great!!\n")
print('Writed data length:{}'.format(wlen))
#fd.write("Python is a great language.\nYeah its great!!\n") #该方法不能正常将数据写入到文件中

# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "Read String is : ", str

# 获取当前位置
print "Current I/O pointer position :%d" % fo.tell()

# 关闭文件
os.close( fd )

print "关闭文件成功!!"


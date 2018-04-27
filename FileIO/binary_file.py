# -*- coding: UTF-8 -*-

import struct

filename = "F:\Tmp\\binary.dat"
mode = "rb+"    #读取二进制文件
filecachesize = 1024

try:
    file = open(filename, mode, filecachesize)
    bytes = bytearray([0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39])   #创建一个字节数组
    file.write(bytes)

    print('seek before curPos:{}'.format(file.tell()))  #打印文件内当前位置
    '''
    seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
    如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。
    '''
    file.seek(0, 0) #设置文件对象指针偏移量到文件开始位置 seek(offset[,from])
    print('seek after curPos:{}'.format(file.tell()))

    tmp = file.read(1)  #读取文件开始字节数据
    print(struct.unpack('B', tmp))  #将字节数据转换为 Int
    while tmp != '':    #文件结束判断
        tmp = file.read(1)  #循环读取文件中每一个字节数据
        if(len(tmp) > 0):   #读取内容检查
            print('0x{:2x}'.format(list(struct.unpack('B', tmp))[0]))  #将字节数据转换为 Int 并输出
        print('curPos:{}'.format(file.tell()))

finally:
    file.close()


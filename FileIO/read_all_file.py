# -*- coding: UTF-8 -*-

'''
逐行读取文件全部内容
'''
def readall(file):
    list = []
    try:
        line = file.readline()
        list.append(line)
        while line:
            list.append(line)
            line = file.readline()
    finally:
        file.close()
    return list


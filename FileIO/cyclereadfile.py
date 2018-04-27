# -*- coding: UTF-8 -*-

import read_all_file

filename = "F:\Tmp\explorer.png"
file = open(filename, "rb", 1024)

#逐行读取文件全部内容
lines = read_all_file.readall(file)
for line in lines:
    print(line)


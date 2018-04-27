# -*- coding: UTF-8 -*-

'''
pass 是空语句，是为了保持程序结构的完整性
pass 不做任何事情，一般用做点位语句
'''

for letter in 'Python':
    if letter == 'h':
        pass
        print('This is a pass block')
    print('current letter :'),
    print(letter)

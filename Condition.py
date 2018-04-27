# -*- coding: UTF-8 -*-

'''
条件判断
'''

flag = False
name = 'peter'
name = 'john'

if name == 'peter':
    flag = True
    print('welcome boss: ' + name)
elif name == 'john':
    print('welcome colleague: ' + name)
else:
    print(name)

print(flag)

print('\nif语句多个条件，目前python没有switch语句，只能用if条件的多重组合来实现')

num = 9
if (num >= 0) and (num <= 10):
    print('hello')

num = 10
if (num < 0) or (num > 10):
    print('hello')
else:
    print('undefine')

num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')
else:
    print('undefine')



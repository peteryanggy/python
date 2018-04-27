# -*- coding: UTF-8 -*-

'''
运算符
'''

print('** 幂 - 返回x的y次幂')
print(2**4)

print('\n//取整除 - 返回商的整数部分')
print(9//2)

#注意：Python2.x 里，整数除整数，只能得出整数。如果要得到小数部分，把其中一个数改成浮点数即可。
print(1/2)
print(1/float(2))

print('\n比较运算符')
a = 9
b = 5
if a > b:
    print("a > b")
else:
    print("a <= b")

print('\n逻辑运算符: and / or / not，非 0 为true，0为 false')
c = -1
if a and c:
    print('a 与 c 都为非0')
else:
    print('a 与 c 其中至少一个为0')

print('\n成员运算符: in / not in')
lst = [1, 2, 3, 4, 5, 6]
member = 2
member2 = 50

if member in lst:
    print(str(member) + '在列表lst中')
else:
    print(str(member) + '不在列表lst中')

if member2 not in lst:
    print(str(member2) + '不在列表lst中')
else:
    print(str(member2) + '在列表lst中')

print('\n身份运算符(身份运算符用于比较两个对象的存储单元): is / is not')
x = 0
y = 10

if x is y:
    print('x 与 y 有相同标识')
else:
    print('x 与 y 没有相同标识')

lst1 = lst
lst2 = [1, 2, 3, 4]

if lst1 is not lst2:
    print('lst1 与 lst2 没有相同标识')
else:
    print('lst1 与 lst2 有相同标识')

print('lst1 id='),
print(id(lst1)) #id() 用于获取对象内存地址
print('lst2 id='),
print(id(lst2))

#Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。









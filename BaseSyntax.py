# -*- coding: UTF-8 -*-
# 单行注释，注释以 # 开头
'''
基础语法
'''

import sys; x = 'runoob'; sys.stdout.write(x + '\n') #同一行显示多条语句

print "你好 Python"
# raw_input("按下 enter 键退出，其他任意键显示....\n")

x = 'a'
y = 'b'

print(x) #print默认输出后会换行
print(y)

print(x), #最后添加,号，作用是不换行输出
print(y),

print("\n")
print x,y

#输出结果
'''
a
b
a b 

a b
'''

counter = 100 #整型变量
miles = 1036.523566985562541235897 #浮点型
name = 'Peter' #字符串

print(counter)
print(miles)
print(name)

#多个变量赋值
a = b = c = 1
a1, a2, a3 = 1, 2, 'peter' #对应赋值，ES6 目前也支持这种赋值形式

print(a)
print(b)
print(c)

print(a1)
print(a3)
print(a2)

#Python字符串
s = "abcdefghijklmnopqrstuvwxyz"
print(s[1:3])#1->2，但不包含 3
print(s[0:])#0->结束
print(s[1])
print(s[1:3] * 2) # 输出字符串两次

#列表
list = ['hello', 100, 3.1415926, 'peter', 70.2]
tinylist = [123, 'ruby']

print('列表')
print(list)
print(list[0])
print(list[1:3]) #1->2，不包含3
print(list[2:])
print(tinylist * 2)
print(list + tinylist)

#元组，注意 元组中的元素不能二次赋值，相当于只读列表
tuple = ( 'ruby', 768, 3.14, 'john', 78.9)
tinytuple = (123, 'ruby')

print('\n元组')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple)
print(tuple + tinytuple)

#字典，与JS中的数组相似

dict = {}
dict['one'] = 'this is a apple'
dict[2] = 'fuzhou'
dict[3] = 100

tinydict = {'name': 'john', 'code': 0x64, 3: 'world'}

print('\n字典')
print(dict['one'])
print(dict[2])
print(dict[3])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())















































# -*- coding: UTF-8 -*-

tuple1 = (50,)  #元组中只包含一个元素时，需要在元素后面添加逗号
print(tuple1)
print(type(tuple1))

num = (50)  #数值类型
print(num)
print(type(num))

tuple2 = (23,)
tuple12 = tuple1 + tuple2
print(tuple12)

print(tuple12 * 2)  #重复

print('\ndel 删除整个元组')
del tuple1
#print(tuple1)







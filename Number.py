# -*- coding: UTF-8 -*-

#数字

var1 = 1
var2 = 10
var3 = 1

print(id(var1))
print(id(var3))
print(id(var2))

del var1    #删除对象引用
print(id(var3))

import sys

print(sys.getsizeof(1))
print(sys.getsizeof(1L))
print(sys.getsizeof(3.14))
print(sys.getsizeof(complex))

print('')
print(type(20))
print(sys.maxint)
print(sys.maxsize)
print(type(sys.maxint + 1))
print(type(sys.maxint))

print('\n不同数值类型所占用的字节数是多少？\n')

none = None

#随机数函数
import random

print('\n随机数函数')
ranlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(ranlist))   #从序列的元素中随机挑选一个元素

print('\nrandrange: 返回指定递增基数集合中的一个随机数，基数缺省值为 1')
count = 5
while count > 0:
    print(random.randrange(1, 10, 2)),
    count -= 1

print('')
count = 5
while count > 0:
    print(random.randrange(1, 10, 3)),
    count -= 1

print('\nrandom: 随机生成下一个实数，它在[0,1)范围内。')
print(random.random())
print(random.random())

random.seed(50)
print(random.random())
print(random.random())

print('\nshuffle: 将序列的所有元素随机排序')
for num in ranlist:
    print(num),

count = 3
while count > 0:
    random.shuffle(ranlist)
    print('\n随机排序后:')
    for num in ranlist:
        print(num),
    count -= 1

print('\nunifrom: 随机生成下一个实数，它在[x,y]范围内。')
count = 5
while count > 0:
    print(random.uniform(1, 10)),
    count -= 1

print('\n')
print(random._pi)   #数学常量 pi（圆周率，一般以π来表示）
print(random._e)    #数学常量 e，e即自然常数（自然常数）











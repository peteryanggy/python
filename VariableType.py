# -*- coding: UTF-8 -*-

'''
数据类型转换
'''

#数据类型转换
print('int')
print(int('64', 16))
print(int('64', 10))
print(int('64', 8))

print('\nlong')
print(long('64', 16))
print(long('64', 10))
print(long('64', 8))

print('\nfloat')
print(float('64.5997'))

print('\ncomplex')
print(complex(1, 56.597))

listvar = [1, 2, 3, 4, 5]
dictvar = {'one': 1, 'two': 2, 'three': 3}

print('\nstr') #将对象 x 转换为字符串
print(str(64.2365))
print(str(listvar)) #相当于toString

print('\nrepr') #将对象 x 转换为表达式字符串
print(repr(listvar))
print(repr(dictvar))

print('\nset 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。')
sx = set('runoob')
sy = set('google')

print(sx)
print(sy)

print('交集'),
print(sx & sy)

print('并集'),
print(sx | sy)

print('差集'),
print(sx - sy)
print(sy - sx)

print('\ndict')
print(dict())   #创建空字典
print(dict(a='a', b='b', t='t'))    #传入关键字
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))    #映射函数方法来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)])) #可迭代对象方法来构造字典

print('\ntuple')
print(tuple([1, 2, 3, 4]))
print(tuple({1:2, 3: 4}))   #针对字典 会返回字典的key组成的tuple
print((1, 2, 3, 4)) #元组会返回元组自身
print(tuple([123, 'xyz', 'tuple', 3.14]))

print('\nlist')
print(list((123, 'xyz', 'hello', 32)))
print(list({'one': 1, 'two': 2}))   #针对字典 会返回字典的key组成的list

print('\neval')
ex = 10
print(eval('3 * ex'))
print(eval('pow(2, 3)'))
print(eval('2 + 2'))

print('\nfrozenset')
a = frozenset(range(10))
print(a)
b = frozenset('runoob')
print(b)
c = [123, 'xyz', 32]
print(frozenset(c))

print('\nchr 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。')
print(chr(0x30)),
print(chr(0x31)),
print(chr(0x61))

print(chr(48)),
print(chr(49)),
print(chr(97))

print('\nunichr')
print(unichr(0x31))
print(unichr(97))

print('\nord 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，'
      '它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode '
      '字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。')
print(ord('1'))
print(ord('a'))

print('\nhex 将一个整数转换为一个十六进制字符串')
print(hex(255))
print(hex(0x12))
print(type(hex(100)))

print('\noct 将一个整数转换成8进制字符串')
print(oct(255))
print(oct(0x12))
print(oct(12))















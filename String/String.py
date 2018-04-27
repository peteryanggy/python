# -*- coding: UTF-8 -*-

'''
字符串
'''

str1 = 'hello'
print(id(str1))
str1 = 'world'
print(id(str1))
str2 = 'hello'
print(id(str2))

print('\n字符串运算符')
print(r'\n')    #r/R 输出原始字符串
print(R'\n')
print(r'\t')

print('\n*: 重复输出字符串')
print('$' * 3)

print('\n字符串格式化')
print('My name is %s and weight is %d kg!' % ('peter', 65))
print('chr: %c%c%c%c' % (0x31, 0x32, 0x33, 0x34))   #格式化字符及ASCII码
print('0x%x\t0x%X' % (100, 0xe1))   #十六进制
addr = id(str2)
print(addr)
#print('%p' % (addr))

print('%#x\t%#X' % (100, 0xe2)) #在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
print('%1.5f' % 10.3265899744)
print('%+d' % 1)
#print('%-d' % 23)
#print('%*d' % 5)
#print('%<sp>d' % 5)
print('%%%d' % 50)  #%50


print('\n三引号: 允许一个字符串跨行，字符串中可以包含换行符、制表符以及其他特殊字符')
hi = '''welcome home
 peter!'''
print(hi)

print('')
unichr = u'hello world!'    #"u"表示这里创建的是一个 Unicode 字符串
print(unichr)

#如果你想加入一个特殊字符，可以使用 Python 的 Unicode-Escape 编码
unichr2 = u'hello\u0020world'   # \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）
print(unichr2)













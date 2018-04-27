# -*- coding: UTF-8 -*-

print('{} {}'.format('hello', 'world'))
print('{0} {1}'.format('hello', 'world'))
print('{1} {0} {1}'.format('y', 'e'))
print('{name},{age}'.format(name='peter', age=32))  #按照参数名称

site = {'name': 'peter', 'age': 32}
print('{name},{age}'.format(**site))

mylist = ['peter', 32]
print('{0[0]},{0[1]}'.format(mylist))   #0必须设置

#class定义
class AssignValue(object):
    def __init__(self, value):
        self.value = value
myvalue = AssignValue(6)
print('value:{0.value}'.format(myvalue))    #输入对象

print('\n数字格式化')
print('{:.2f}'.format(3.1415926))   #保留小数点后两位
print('{:+.2f}'.format(3.1415926))  #带符号保留小数点后两位
print('{:+.2f}'.format(-3.1415926)) #带符号保留小数点后两位
print('{:.0f}'.format(3.1415926))   #不带小数
print('{:x<4d}'.format(1))  #左对齐，右补x，宽度4，不足的位以x填充
print('{:x<4d}'.format(10))
print('{:0>4d}'.format(2))  #右对齐，左补0，宽度4，不足的位以0填充
print('{:0>4d}'.format(22))

print('{:,}'.format(123456789)) #以逗号分隔的数字格式，输出 123,456,789
print('{:,.5f}'.format(123456789.23657947)) #以逗号分隔的数字格式，并保留小数点后5位，输出 123,456,789.23658
print('{:.2%}'.format(0.659841))    #百分比格式，输出 65.98%
print('{:.2e}'.format(1268000000))  #指数记法，输出 1.27e+09

print('{:10d}'.format(13))  #右对齐(默认)，左补0，宽度为 10
print('{:<10d}'.format(13)) #左对齐，右补0，宽度为 10
print('{:^10d}'.format(13)) #中间对齐，宽度为 10

print('\n进制')
print('{:b}'.format(10))    #二进制
print('{:d}'.format(10))    #十进制
print('{:o}'.format(10))    #八进制
print('{:x}'.format(10))    #十六进制
print('{:#x}'.format(11))   #十六进制
print('{:#X}'.format(11))   #十六进制

#大括号 {} 来转义大括号
print('{} 对应的位置是 {{0}}'.format('peter'))    #输出 peter 对应的位置是 {0}




















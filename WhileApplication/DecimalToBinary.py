# -*- coding: UTF-8 -*-

#十进制转二进制

denum = input('输入十进制数:')
print(denum),
print('(10)'),

binnum = []
#二进制
while denum > 0:
    binnum.append(str(denum % 2))   #(取模 - 返回除法的余数)栈压入
    denum //= 2 #取整除 - 返回商的整数部分
print('= '),
while len(binnum) > 0:
    import sys
    sys.stdout.write(binnum.pop())  #无空格输出

#END
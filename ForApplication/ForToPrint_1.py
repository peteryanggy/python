# -*- coding: UTF-8 -*-

#等腰直角三角形
rows = int(raw_input('输入列数:'))
#i = j = k = 1   #声明变量，i用于控制外层循环(图形行数)，j用于控制空格的个数，k用于控制*的个数
print('等腰直角三角形1')
for i in range(0, rows):
    for k in range(0, rows - i):
            print(' * '),
            k += 1
    i += 1
    print('')

print('\n')

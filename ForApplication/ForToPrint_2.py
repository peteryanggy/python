# -*- coding: UTF-8 -*-

rows = int(raw_input('输入列数:'))
#打印实心等边三角形
print('打印空心等边三角形，这里去掉if-else条件判断就是实心的')
for i in range(0, rows + 1):
    for j in range(0, rows - i):
        print(' '),
        j += 1
    for k in range(0, 2 * i - 1):
        if (k == 0) or (k == 2 * i - 2) or (i == rows):
            if i == rows:
                if k % 2 == 0:
                    print('*'),
                else:
                    print(' '),
            else:
                print('*'),
        else:
            print(' '),
        k += 1
    print('')
    i += 1

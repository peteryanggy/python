# -*- coding: UTF-8 -*-

rows = int(raw_input('输入行数:'))
#打印菱形
print('打印空心菱形')
for i in range(rows):
        for j in range(rows - i):
            print(' '),
            j += 1
        for k in range(2 * i - 1):
            if (k == 0) or (k == 2 * i - 2):
                print('*'),
            else:
                print(' '),
            k += 1
        print('')
        i += 1
#菱形下半部分
for i in range(rows):
    for j in range(i):
        print(' '),
        j += 1
    for k in range(2 * (rows - i) - 1):
        if (k == 0) or (k == 2 * (rows - i) - 2):
            print('*'),
        else:
            print(' '),
        k += 1
    print('')
    i += 1

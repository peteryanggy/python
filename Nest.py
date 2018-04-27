# -*- coding: UTF-8 -*-

'''
循环嵌套
'''

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not(i % j):
            break
        j += 1
    if (j > i / j):
        print(i),
        print(' 是素数')
    i += 1

#*字塔
print('\n*字塔')
i = 1
while i < 9:
    if i <= 5:
        print('*' * i)
    elif i <= 9:
        j = i - 2 * (i - 5)
        print('*' * j)
    i += 1
else:
    print('')

print('\n')

#冒泡排序
array = [9,2,7,4,5,6,3,8,1,10]
L = len(array)
print('未排序')
for i in range(L):
    print(array[i]),

for i in range(L):
    for j in range(L - i):
        if array[L - j - 1] < array[L - j - 2]:
            array[L - j - 1], array[L - j - 2] = array[L - j - 2], array[L - j - 1]

print('\n排序后')
for i in range(L):
    print(array[i]),


#求区间[a,b]内的质数
a = 1
b = 20

print '\n求区间[',a,b,']内的质数\n'
E = []
for num in range(a, b + 1):
    snum = int(num * 0.5 + 1)
    for i in range(2, snum):
        if num % i == 0:
            break
    else:
        E.append(num)
print a,'到',b,'的质数有',len(E),'个:\n',E




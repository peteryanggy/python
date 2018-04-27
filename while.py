# -*- coding: UTF-8 -*-

'''
wile循环
'''

#筛选列表中的质数
numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []

while len(numbers) > 0:
    num = numbers.pop()
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)

#continue and break

print('continue')
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

print('\nbreak')
i = 1
while 1:
    print(i)
    i += 1
    if i > 10:
        break

#当while执行完成后，执行else
print('\nwhile ... else')
count = 0
while count < 5:
    print(count),
    print(' is less than 5')
    count += 1
else:
    print(count),
    print(' is more than 5 or equal 5')





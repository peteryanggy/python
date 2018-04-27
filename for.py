# -*- coding: UTF-8 -*-

#for 仅用于遍历列表中元素: for in

for letter in 'Python':
    print(letter)

fruits = ['banana', 'apple', 'mango', 'lemon']
for fruit in fruits:
    print(fruit)

#序列索引迭代
print('\n序列索引迭代')
for index in range(len(fruits)):
    print(fruits[index])

#当for循环执行完成后，执行else
print('\nfor...else')
list = [1, 2, 3]
for num in list:
    print(num)
else:
    print('else')

print('\n')
lst = [11, 22, 33, 44, 55, 66, 77]
for j in lst:
    print(j)

print('')

for index in range(0, len(lst)):
    print(index),
    print('->'),
    print(lst[index])

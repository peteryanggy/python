# -*- coding: UTF-8 -*-

lst = []
lst.append('Google')
lst.append(32)
lst.append('Apple')

print(lst)

del lst[1]  #删除列表元素

print(lst)

lst2 = [1, 2, 3, 4]

lst12 = lst + lst2  #组合
print(lst12)

print(lst * 2)  #重复

print('\n迭代')
for x in lst12:
    print(x)

print('\n')
print(lst2[-2]) #读取列表中倒数第二个元素

print('\ncmp')
com1 = [1, 2, 3, 5]
com2 = [1, 2, 3, 4]
'''
如果比较的元素是同类型的,则比较其值,返回结果。

如果两个元素不是同一种类型,则检查它们是否是数字。

如果是数字,执行必要的数字强制类型转换,然后比较。
如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
否则,通过类型名字的字母顺序进行比较。
如果有一个列表首先到达末尾,则另一个长一点的列表"大"。

如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。
'''
print(cmp(com1, com2))  #com1 > com2 => 1，com1 == com2 => 0，com1 < com2 => -1

mlist = [1, 2, 3, 2, 1, 3, 4, 2, 6]
print('\ncount')
print('2 count {}'.format(mlist.count(2)))

print('\nextend')   #在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）,该方法没有返回值，但会在已存在的列表中添加新的列表内容。
mlist.extend(['a', 'b', 100])
print(mlist)

print('\nindex')
print('2 first index {}'.format(mlist.index(2)))

print('\ninsert')
mlist.insert(4, 'google')   #将指定对象插入列表的指定位置。该方法没有返回值，但会在列表指定位置插入对象。
print(mlist)

print('\npop')
p = mlist.pop() #提取出最后一个元素
#p = mlist.pop(mlist[-1])    #pop() 默认为 pop(list[-1])
print(p)
print(mlist)

print('\nwhile-list.pop')   #循环提取出列表最后一个元素
while len(mlist) > 0:
    print(mlist.pop()),

print('\n提取指定元素')
mlist = [1, 2, 3, 4, 3, 2, 1]
rlist = mlist.pop(0)    #移除指定索引的元素
print(rlist)
print(mlist)

print('\nremove')   #移除列表中某个值的第一个匹配项
mlist.remove(2)
print(mlist)

print('\nreverse')
mlist.reverse()
print(mlist)

print('\nsort([func])')
mlist.sort()
print(mlist)

















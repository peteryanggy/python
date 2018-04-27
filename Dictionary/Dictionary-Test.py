# -*- coding: UTF-8 -*-

dic = {'name': 'peter', 'age': 32, 'addr': 'fuzhou', 100: '0x64'}
print(dic)
print(dic['name'])
print(dic['age'])
print(dic[100])

'''
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令
'''
del  dic['name']
print(dic)
dic.clear()
print(dic)
del dic
#print(id(dic))

dic = {'phone': '12580', 'id': 1002548875}
print(str(dic)) #输出字典可打印的字符串表示。

cdic = dic.copy()   #返回一个字典的浅复制
print(cdic)
print('id of dic ={}, id of cdic ={}'.format(id(id), id(cdic)))

print('\nfromkeys')
# fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
ndic = {}.fromkeys(['name', 'sex', 'age'], None)
print(ndic)

print('\nget/has')
print(ndic.get('name'))
print(ndic.has_key('age'))

print('\nitems')    #以列表返回可遍历的(键, 值) 元组数组
print(ndic.items())

print('\nkeys/values')
print(ndic.keys())
ndic['name'] = 'john'
ndic['age'] = 32
ndic['sex'] = 'male'
print(ndic.values())

print('\nsetdefault(key, default=None)')   #和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
print(ndic.setdefault('addr', 'beijing'))
print(ndic)

print('\nupdate')   # update() 函数把字典dict2的键/值对更新到dict里。没有就添加，有则更新
ndic2 = {'name': 'peter', 'sex': 'female', 'age': 39, 'phone': '12580'}
ndic.update(ndic2)
print(ndic)

print('\npop')  #删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
name = ndic.pop('name', None)
print(name)
print(ndic)

print('\npopitem')  #随机返回并删除字典中的一对键和值。
rand = ndic.popitem()
print(rand)
print(ndic)

print(len(ndic))















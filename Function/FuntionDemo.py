# -*- coding: UTF-8 -*-

#定义函数
def myprint(msg):
    text = 'welcome'
    print(type(text))
    print(id(text))
    print('{} {}!'.format(text, msg))

text = 'peter'
myprint(text)
print(id(text))

print('a.id')
a = 5
print(id(a))
a = 10
print(id(a))

print('b.id')
b = [1, 2, 3, 4]
print(id(b))
b[1] = 10
print(id(b))

#不可变对象
def ChangeInt(a):
    a = 10

c = 2
ChangeInt(c)
print('c:{}'.format(c))

#可变对象
def changeme(mylist):
    mylist.append([1, 2, 3, 4, 5]);
    print('函数内取值:{}'.format(mylist))
    return

mylist = [10, 20, 30]
changeme(mylist)
print('函数外取值:{}'.format(mylist))

#缺省参数，即默认参数
def printinfo(name, age, addr = 'fuzhou'):
    print('name:{}, age:{}, addr:{}'.format(name, age, addr))
    return

#关键字参数，即C#中的命名参数
printinfo(age=32, addr='fuzhou', name='peter')

printinfo(age=31, name='John')

#不定长参数
def printinfos(first, *more):
    print('输出: ')
    print(first)
    for item in more:
        print(item)
    return

print('不定长参数')
printinfos(10)
printinfos(10, 20, 30, 40, 50, 60)

#lambda
sum = lambda first, second: first + second;

print('first+second:{}'.format(sum(11, 23)))

def mysumc(first, second):
    return first + second;
print('first+second:{}'.format(mysumc(2, 3)))

_total = 0;
def sum_2(first, second):
    #函数体内定义的与全局变量同名的变量时，函数体内什么使用函数体内定义的局部变量，而非同名的全局变量
    _total = first + second;
    print('内部输出函数内局部变量,first+second:{}'.format(_total))
    return _total;

#函数体内强制使用全局定义的变量
def sum_3(first, second):
    global _total   #声明使用全局定义变量
    _total = first + second;
    return _total


sum_2(1, 89);
print('外部输出函数外全局变量，first+second:{}'.format(_total))

sum_3(22, 1)
print('函数内强制使用全局定义变量, first+second:{}'.format(_total))


def funx(x):
    def funy(y):
        return x * y
    return funy #return funy 返回的是一个对象，可理解为funx是funy的一个对象
xy = funx(2)(4)
print('funx()():{}'.format(xy))
















# -*- coding: UTF-8 -*-

'''
内置函数
'''

print('abs(x) 返回数字x的绝对值')
print('abs(-5): {}'.format(abs(-5)))
print('abs(0.21365): {}'.format(abs(0.21365)))
print('abs(119L): {}'.format(abs(119L)))

print('\r\nall(iterable)')#如果参数中的元素中有包含:0、''、False、或iterable 为空，则返回False，否则返回True
print(all([1, 2, 3, 4, '3', False]))

print('\r\nany(iterable)')#参数中只要有一个不为: 0、''、False，则返回True，否则返回False
print(any([0, False, '', 1]))

print('\r\nisinstance()')#判断一个对象是否是str或unicode的实例
print(isinstance('hello', str))
print(isinstance('1', basestring))

print('\r\nbin()')#返回整数的二进制数据表示
print('bin(10): {}'.format(bin(10)))
print('bin(20L): {}'.format(bin(20L)))

print('\r\nbool()')#将参数转换为布尔类型
print(bool())#False
print(bool(0))#False
print(bool(1))#True
print(bool(0.1))#True
print(bool(-9))#True
print(bool([1, 2, 3]))#True

print('\r\nbytearray()')#创建一个字节数组
'''
如果 source 为整数，则返回一个长度为 source 的初始化数组；
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
如果没有输入任何参数，默认就是初始化数组为0个元素。
'''
bchr = bytearray('0123456789', 'utf-8')
for b in bchr:
    print('0x{:0>2x} '.format(b)),

bis = bytearray([1, 2, 3, 4, 5, 6])
for b in bis:
    print('0x{:0>2x} '.format(b)),  #右对齐，左边补 0

print('\r\ncallable')#检查对象是否可调用
print(callable(0))
print(callable('hello'))

def add(a, b):
    return a + b
print(callable(add))

class A:
    def method(self):
        return 0
print(callable(A))
a = A()
print(callable(a))
print(callable(a.method))#True

class B:
    def __call__(self, *args, **kwargs):
        return 0
b = B()
print(callable(B))
print(callable(b))

print('\r\nchr()')# 1 字节数据转换为ASCII码字符显示
print('chr(0x30):{}'.format(chr(0x30)))

print('\r\nclassmethod')#@classmethod 修饰符用于标识函数是不需要实例化，就能够通过类名称直接调用的
class CM(object):
    bar = 1
    def func1(self):
        print('foo')
    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()
CM.func2()

print('cmp(x, y)')#比较两个对象，x > y => 1, x < y => -1, x == y => 0

def comResult(value):
    if(value == 0):
        return '等于'
    elif(value < 0):
        return '小于'
    else:
        return '大于'

print('1 {} 2'.format(comResult(cmp(1, 2))))
print('100 {} 100'.format(comResult(cmp(100, 100))))
print('10 {} -1'.format(comResult(cmp(10, -1))))
print('a {} A'.format(comResult(cmp('a', 'A'))))#比较字符
print('hello {} helloy'.format(comResult(cmp('hello', 'helloy'))))

print('\r\ncompile(source, filename, mode[, flags[, dont_inherit]])')#动态编译
'''
source -- 字符串或者AST（Abstract Syntax Trees）对象。。
filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
flags和dont_inherit是用来控制编译源码时的标志
'''
src = 'for i in range(0, 10): print(i)'
imp = compile(src, 'mycode', 'exec')
print(imp)
print('exec')
exec(imp)

print('eval')
src2 = '3 * 4 + 5'
imp2 = compile(src2, 'code_2', 'eval')
print(eval(imp2))

print('\r\ncomplex')#创建复数
print(complex(1, 2))#1 + 2j
print(complex(1))
print(complex('1'))
print(complex('1+5j'))

print('\r\ndelattr')#删除对象属性
class Coordinate:
    x = 112.3698
    y = 33.2569874
    z = 10
point1 = Coordinate()
print('x = {}'.format(point1.x))
print('y = {}'.format(point1.y))
print('z = {}'.format(point1.z))

delattr(Coordinate, 'z')

print('--删除 z 属性后')
print('x = {}'.format(point1.x))
print('y = {}'.format(point1.y))
try:
    print('z = {}'.format(point1.z))
except Exception,err:
    print(err)

print('\r\ndict()')#创建一个字典
print(dict(a='a', b='b', c='c'))
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))#以映射函数方式来构造字典
print(dict([(1, 'one'), ('city', 'fuzhou'), ('age', 32)]))#以可迭代对象来构造字典

'''
#不带参数时返回当前范围内的变量、方法、定义的类型列表；带参数时，返回参数的属性、方法列表。
如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
'''
print('\r\ndir()')
print(dir())
print('\r\n')
print(dir(point1))

print('\r\ndivmod()')#返回一个包含商和余数的元组
print(divmod(7, 2))

print('\r\nenumerate')#将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标
seasons = ['Sprint', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))#下标默认从 0 开始
print(list(enumerate(seasons, 1)))#下标从 1 开始
for i, ele in enumerate(seasons):
    print('{} {}'.format(i, ele))

print('\r\nexecfile')#执行一个.py文件
execfile("F:\StudyProjects\PycharmProjects\PythonPrime\InnerFunction\hello.py")

#等价于
with open("F:\StudyProjects\PycharmProjects\PythonPrime\InnerFunction\hello.py", 'r') as f:
    exec(f.read())

print('\r\nfile()')#打开一个文件，open() 是它的别名
f = file("F:\StudyProjects\PycharmProjects\PythonPrime\InnerFunction\hello.py")
print(f.read())
f.close()


print('\r\nfilter()')#过滤序列中，不符合条件的元素，第一个参数为判断函数，第二个参数为参与判断的序列
def is_odd(n):
    return n % 2 == 1

newList = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(newList)

print('\r\nfloat()')#将整数或数字字符串转换为浮点数
print(float('2368.23658'))
print(float(1123))

print('\r\nfrozenset')#冻结一个集合，冻结后的集合不能进行修改
fro = frozenset([1, 2, 3, 4, 5])
print(fro)
for i in fro:
    print('{} '.format(i)),

print('\r\ngetattr')#返回一个对象的指定属性名称的值
print(getattr(point1, 'x'))

print('\r\nglobals()')#返回当前位置的全部全局变量
print(globals())

print('\r\nhasattr')#检查对象是否包含指定名称的属性
print(hasattr(point1, 'x'))
print(hasattr(point1, 'z'))

print('\r\nhash()')#用于获取一个对象的哈希值
print(hash(point1))

print('\r\nhelp()')#用于查询函数或模块的详细说明
#help('sys')

print('\r\nhex()')#将10进制整数转换成16进制，以字符串形式表示
print(hex(255))
print(hex(100))

print('\r\nid()')#获取对象的内存地址
print(id(point1))

'''
注意：input() 和 raw_input() 这两个函数均能接收 字符串 ，但 raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。

除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
注意：python3 里 input() 默认接收到的是 str 类型。
'''
print('\r\ninput()')
'''
print('input:')
i = input()
print(i)

print('raw_input:')
r = raw_input()
print(r)
'''

print('\r\nint()')#将一个整数或数字字符转换为整数
print(int('2366589'))#输入带小数的数字字符时，转换时会报错
print(int(100))
print(int('64', 16))#十六进制字符

'''
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。

如果要判断两个类型是否相同推荐使用 isinstance()。
'''
print('\r\nisinstance()')
print(isinstance(1, int))
print(isinstance('', str))
print(isinstance(point1, Coordinate))

class AA:
    pass

class BB(AA):#继承
    pass

print('isinstance(BB(), AA): {}'.format(isinstance(BB(), AA)))
print('type(BB()) == AA: {}'.format(type(BB()) == AA))

print('\r\nissubclass(class, classinfo)')#用于判断class是否是类型参数classinfo的子类
print(issubclass(BB, AA))

print('\r\niter()')#生成一个迭代器
for i in iter([1, 2, 3, 4, 5]):
    print('{} '.format(i)),

class counter:
    def __init__(self, _start, _end):
        self.start = _start
        self.end = _end

    def get_next(self):
        s = self.start
        if(self.start < self.end):
            self.start += 1
        else:
            raise StopIteration
        return s

print('')

c = counter(1, 5)
iterator = iter(c.get_next, 3)
print(type(iterator))
for i in iterator:
    print('{} '.format(i)),

print('\r\nlen()')#返回对象(字符串、列表、元组等)长度或项目个数
print(len([1, 2, 3, 4, 5, 6]))

print('\r\nlist()')#将元组转换为列表
print(list((123, 'abc', 32)))

print('\r\nlocals()')#以字典类型返回当前位置的全部局部变量
print(locals())

print('\r\nlong()')#将一个数字或字符串转换为一个长整型
print(long('123598'))
print(long('64', 16))

print('\r\nmap()')#根据第一个参数，为函数，将第二个参数序列，映射为一个新序列

def change(x):
    return x * x

mapList = map(change, [1, 2, 3, 4])
for i in mapList:
    print('{} '.format(i)),

print('')
mapList2 = map(lambda x: x ** 3, [1, 2, 3, 4, 5])
for i in mapList2:
    print('{} '.format(i)),
print('')
mapList3 = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 0])
print(mapList3)

print('\r\nmax')
print(max(10, 1, 20, 20.9, 20.12))

print('\r\nmin')
print(min(10, 1, 20, 20.9, 20.12, -2))

print('\r\nmemoryview')#返回给定对象的内存查看对象
#内存查询对象，是指点对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许python代码访问
mv = memoryview('abcdefg')
print(mv[1])
print(mv[-1])
print(mv[1:4])
print(mv[1:4].tobytes())

print('\r\nnext')#返回迭代器的一下个项目
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x),
    except StopIteration:
        break

print('\r\noct')#将一个整数转换成8进制字符串
print(oct(10))

'''
ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
'''
print('\r\nord')
print(ord('^'))
print(chr(0x35))

print('\r\npow')
print(pow(2, 3))    #8
print(pow(2, 3, 3)) #第三个参数表示，对前两个参数的计算结果，按第三个参数进行取模

import math
print(math.pow(2, 3))   #8.0
#print(math.pow(2, 3, 3))    #只提供了支持两个参数的pow函数

print('\r\nprint')
#print('I', 'will', 'try', 'my', 'best', '!', sep=' ')  #python3.x


print('\r\n新式类属性')
class C(object):
    def __init__(self):
        self.x = 0

    def getx(self):
        return self.x

    def setx(self, value):
        self.x = value

    def delx(self):
        del self.x

    x = property(getx, setx, delx, "I'm the 'x' property.")
'''
#下面使用方式会报错，python 2.7x
c = C()
v = c.x
c.x = 100
v2 = c.x
del c.x
'''

print('\r\nrange')#返回一定范围的整数列表
for i in range(0, 10, 2):
    print(i),
print('')
for i in range(-9, 0, 1):
    print(i),

'''
reduce 对参数序列中元素进行累积
函数将一个数据集合中的所有数据进行下列操作：
用传给reduce中的函数function先对集合中的第1、2元素进行操作，
得到的结果再与第三个元素用function函数运算，最后得到一个结果
'''
print('\r\nreduce')
def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)

r2 = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(r2)

print('\r\nreload')#重新载入之前载入的模块
import sys
print(sys.getdefaultencoding())

reload(sys)
sys.setdefaultencoding('utf8')
print(sys.getdefaultencoding())

print('\r\nrepr')#将对象转化为供解释器读取的形式
s = 'Helo'
print(s)
s1 = repr(s)
print(s1)

dict = {'one', 1, 'two', 2, 'three', 3}
print(dict)
dic1 = repr(dict)
print(dic1)

print('\r\nreverse')#反向列表中的元素
aList = [123, 'hello', 0x36, 'John']
print(aList)
aList.reverse()
print(aList)

print('\r\nround')#返回浮点数的四舍五入值，第二个参数为保留小数点后几位
bnum = 80.2365987455
print('round({}, 2): {}'.format(bnum, round(80.2365987455, 2)))
print(round(bnum, 0))
print(round(bnum, 4))

print(round(2.355, 2))#3.35 而非 3.36，受计算机表示精度的影响

print('\r\nset')#创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可计算交集、差集、并集等
x = set('runoob')
y = set('google')
print(x)
print(y)

print(x & y)    #交集
print(x | y)    #并集
print(x - y)    #差集
print(y - x)

print('\r\nsetattr')    #设置属性值，该属性必须存在
print(point1.x)
setattr(point1, 'x', 0x64)
print(point1.x)

print('\r\nslice')#slice函数实现切片对象，主要用在切片操作函数里面的参数传递
myslice = slice(0, 9, 2)#0 起始位置，9 结束位置，2 间距
print(myslice)

arr = range(10)
print(arr)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sliceRet = arr[myslice]
print(sliceRet)#[0, 2, 4, 6, 8]

'''
sorted 对所有可迭代的对象进行排序操作
sort 与 sorted 区别
sort 是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作
list的sort方法返回的是对已存在的列表进行操作，而内建函数sorted方法返回的是一个新的list，而不是在原来的基础上进行操作

sorted(iterable[, cmp[, key[, reverse]]])

参数说明：

iterable -- 可迭代对象。
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

'''
print('\r\nsorted')
a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)

print(a)
print(b)

L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
nLst = sorted(L, cmp = lambda x, y: cmp(x[1], y[1]))

print(L)
print(nLst)

keyList = sorted(L, key = lambda x: x[1])#以第二个值为键进制排序
print(keyList)
keyList_2 = sorted(L, key = lambda x: x[0])#以第一个值为键进行排序
print(keyList_2)
keyList_3 = sorted(L, key = lambda x: x[0], reverse=True)#以第一个值为键进行排序，降序
print(keyList_3)

print('\r\nstaticmethod')#静态方法标签
class S(object):
    @staticmethod
    def smethod(name, age):
        print('{}-{}'.format(name, age))
S.smethod('John', 32)   #直接使用类名.来调用

sobj = S()
sobj.smethod('Peter', 32)#静态方法也可以通过实例来调用

print('\r\nstr')#将对象转化为适于人阅读的形式
print(str('Hello'))
print(str({'one': 1, 'two': 2, 'three': 3, 'four': 4}))

print('\r\nsum')#对序列进行求和计算
print(sum([1, 2, 3, 4, 5]))

print('\r\nsuper')#用于调用父类的方法

class baseA(object):
    def methodFunc(self, msg):
        print('baseA.methodFunc:{}'.format(msg))

class inheritA(baseA):
    def methodFunc(self, msg):
        print('inheritA.methodFunc:{}'.format(msg))
        super(inheritA, self).methodFunc('inherit') #调用父类方法

ih = inheritA()
ih.methodFunc('John')

print('\r\ntuple')#将列表转换为元组
print(tuple([1, 2, 3, 4]))

'''
type() 如果只提供第一个参数，则返回对象的类型，如果三个参数都提供，则返回新的类型对象
ininstance 与 type 区别
type 不会认为子类是一种父类类型，不考虑继承关系
instance 会认为子类是一种父类类型，考虑继承关系

如果要判断两个类型是否相同推荐使用isinstance
'''
print('\r\ntype')
print(type(1))
print(type('hello'))
print(type([]))
print(type((1, 2)))
print(type({'key': 1}))
print(type(point1))
print(type(Coordinate))
print(isinstance(inheritA(), baseA))
print(type(inheritA()) == baseA)

print('\r\nunichr')#将输入数字转换成unicode字符
print(unichr(0x4f60))#你

print('\r\nvars')#返回对象object的属性和属性值的字典对象
print(vars(c))

print('\r\nxrange')#用法与range完全相同，不同的是xrange生成的不是一个数组，而是一个生成器
xr = xrange(0, 9, 1)
xarr = list(xr)#根据生成器生成列表

print(xarr)

print('\r\nzip')
'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
'''
a_1 = [1, 2, 3]
b_1 = [4, 5, 6]
c_1 = [4, 5, 6, 7]
zipped = zip(a_1, b_1)#压缩
print(zipped)
zipped2 = zip(b_1, c_1)
print(zipped2)
unZipped = zip(*zipped)#解压
print(unZipped)

print('\r\n__import__()')#用于动态加载类和函数，如果一个模块经常变化，就可以使用__import__()来动态载入
import sys
__import__('varModule')

print('\r\nexec')#
exec('print("Hello world!")')
exec("""for i in range(5):print("iter item:{}".format(i))""")















































































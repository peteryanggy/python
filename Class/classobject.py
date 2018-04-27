# -*- coding: UTF-8 -*-

import Class.Employee as CE #导入模块，并设置别名

empJhon = CE.Employee(name='Jhon', salary=3000)#实例化类对象
print(type(empJhon))
empJhon.displayEmployee()

empPeter = CE.Employee('Peter', 10000)
empPeter.displayEmployee()

print(CE.Employee.empCount)

empJhon.age = 32#动态增加属性
print(empJhon.age)
#print(empPeter.age)#动态增加的属性，只针对于当前实例，而没有修改类的定义

del empJhon.name
print(empPeter.name)
'''
也可以通过函数方式来操作属性：
getattr(obj, name[, default]) : 访问对象的属性。
hasattr(obj,name) : 检查是否存在一个属性。
setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
delattr(obj, name) : 删除属性。
'''

'''
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''
print('__doc__:{}'.format(CE.Employee.__doc__))
print('__name__:{}'.format(CE.Employee.__name__))
print('__module__:{}'.format(CE.Employee.__module__))
print('__bases__:{}'.format(CE.Employee.__bases__))
print('__dict__:{}'.format(CE.Employee.__dict__))

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):#析构函数， __del__在对象销毁时被调用，当对象不再被使用时，__del__方法运行
        class_name = self.__class__.__name__
        print('{} 销毁!'.format(class_name))

pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1)),
print(id(pt2)),
print(id(pt3))

del pt1
del pt2
del pt3

'''
python中继承中的一些特点：
1、在继承中基类的构造方法__init__()不会被自动调用，它需要在基类派生类中亲自专门调用；
2、在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别在于类中调用普通函数时并不需要带上self参数；
3、python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。(先在本类中查找调用的方法，找不到才去基类中找)

如果在继承元组中列了一个以上的类，那么它就被称作“多重继承”
'''

class Parent(object):
    parentAttr = 100    #该变量相当于C#中类中定义的静态变量
    def __init__(self):
        print('调用父类构造函数!')

    def parentMethod(self):
        print('调用父类方法!')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('父类属性:{}'.format(Parent.parentAttr))

    def myMethod(self):
        print('父类myMethod方法!')

class Child(Parent):
    def __init__(self, x):#子类构造函数
        Parent.__init__(self)#调用父类构造函数
        #super(Parent, self).__init__()
        print('调用子类构造方法!')
        self.x = x

    def childMethod(self):
        print('调用子类方法!')

    def getX(self):
        print('x attr:{}'.format(self.x))

    def myMethod(self):
        print('子类myMethod方法!')

    def superMyMethod(self):
        super(Child, self).myMethod()

print('\r\n类继承：')
c = Child(123)
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.getX()
c.myMethod()
c.superMyMethod()


print('运算符重载')
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector ({}, {})'.format(self.a, self.b)

    def __add__(self, other):# “+”号运算符重载
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print("v1 + v2: {}".format(v1 + v2))

'''
单下划线、双下划线、头尾双下划线说明：

__foo__ ：定义的是特殊方法，一般是系统定义名字，类似 __init__()之类的
_foo：以单下划线开头的表示是 protected 类型的变量，即保护类型只能允许其本身及子类访问，不能用于from module import *
__foo：双下划线表示是私有类型(private)的变量，只能是允许这个类本身进行访问

类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

类的方法
在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数

类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods
'''

class JustCounter:
    __secretCount = 0   #私有变量
    publicCount = 0 #公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)

    def show(self):
        print('show!!!')

    #def show(self, msg): #python 不运行方法重载
    #    print('show: {}'.format(msg))

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)

counter.show()




































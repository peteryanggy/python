# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0
    '''
    empCount 变量是一个类变量，类似于C#中的静态变量，它的值将在这个类的所有实例之间共享，
    可以通过内部类或外部类使用Employee.empCount来访问
    '''

    '''
    __init__() 是类的构造函数或初始化方法，当创建了类的实例时就会被调用
    self 代表类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
    
    类的方法与普通函数只有一个特别的区别--它们必须有一个额外的第一参数名称，通常为self
    '''
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee {}'.format(Employee.empCount))

    def displayEmployee(self):
        print('Name: {}, Salary: {}'.format(self.name, self.salary))

#cmp = Employee('Peter', 8000)
#cmp.displayEmployee()

# -*- coding:UTF-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

#寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
Base.metadata.create_all(engine)
#创建与数据库的会话session class，注意，这里返回的session是个class，不是实例
Session = sessionmaker(bind=engine)
session = Session()

#获取session，然后把对象添加到session
#最后提交并关闭，session对象可以视为当前数据库连接

#增加
'''
add = User(id=2, name='sanya')
session.add(add)
session.add_all([
    User(id=3, name='fuzhou'),
    User(id=10, name='xiamen')
])
session.commit()
'''

#删除
#session.query(User).filter(User.id > 2).delete()
#session.commit()

#修改
'''
session.add_all([
    User(id=31, name='liuyao'),
    User(id=102, name='sbyao'),
    User(id=201, name='mayun')
])
session.commit()
'''


#将users中id等于2信息，修改id为6
#session.query(User).filter(User.id == 2).update({'id': 6})
#session.commit()

#session.query(User).filter(User.id > 2).update({'name': 'unknown'})
#session.commit()

#查询

#查询user表下面name=liuyao的字段
print('查询user表下面name=liuyao的字段')
ret = session.query(User).filter_by(name='liuyao').all()
for i in ret:
    print(i.id, i.name)

#查询user表里字段是name=liuyao的第一条数据
print('查询user表里字段是name=liuyao的第一条数据')
ret = session.query(User).filter_by(name='liuyao').first()
print(ret.id, ret.name)

#查询user表里字段是name是liuyao或者mayun的信息打印出来
print('查询user表里字段是name是liuyao或者mayun的信息打印出来')
ret = session.query(User).filter(User.name.in_(['liuyao', 'mayun'])).all()
for i in ret:
    print(i.id, i.name)

#可以给返回的结果起一个别名，或者叫标签：可有可无
print('可以给返回的结果起一个别名，或者叫标签：可有可无')
ret = session.query(User.name.label('')).all()
print(ret, type(ret))
#其相当于执行以下的SQL语句：SELECT users.name AS name_label FROM users

#查询User表根据id排序
print('查询User表根据id排序')
ret = session.query(User).order_by(User.id).all()
for i in ret:
    print(i.id, i.name)

#查询user表里根据id排序输出0到3的字段
print('查询user表里根据id排序输出0到3的字段')
ret = session.query(User).order_by(User.id)[0:3]
for i in ret:
    print(i.id, i.name)

#创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
print('创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行')
user = session.query(User).filter(User.id == 10).one()
print(user.id, user.name)


























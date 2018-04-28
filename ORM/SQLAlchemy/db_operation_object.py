# -*- coding:UTF-8 -*-

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

import MySQLdb

metadata = MetaData()

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb', max_overflow=5)

conn = engine.connect()#连接数据库
#创建表对象
user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)))

color = Table('color', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(20)))

#执行插入数据操作
#conn.execute(user.insert(), {'id': 13, 'name': 'seven_9'}, {'id': 10, 'name': 'jhon'})
#另一种插入数据方式
#intsql = user.insert().values(id=123, name='peter')
#conn.execute(intsql)

#删除数据
#delsql = user.delete().where(user.c.id > 100)
#conn.execute(delsql)

#修改/更新
#upsql = user.update().where(user.c.name == 'jhon').values(name='jhon_new')
#conn.execute(upsql)

#查询模块
from sqlalchemy import select

#查询表里的内容
sql = select([user, ])
res = conn.execute(sql)
print(res.fetchall())

#查询user表下的id
sql = select([user.c.id, ])
res = conn.execute(sql)
print(res.fetchall())

#查询user表和color表的name，条件是user.id = color.id
sql = select([user.c.name, color.c.name]).where(user.c.id == color.c.id)
res = conn.execute(sql)
print(res.fetchall())

#查询user表的name，并按照条件排序
#按name排序
sql = select([user.c.name]).order_by(user.c.name)
res = conn.execute(sql)
print(res.fetchall())

#按照id排序
sql = select([user.c.name]).order_by(user.c.id)
res = conn.execute(sql)
print(res.fetchall())

#查询user表的name，id，并按照条件分组
#单个分组条件执行会报异常 sql = select([user]).group_by(user.c.name)
sql = select([user]).group_by(user.c.name).group_by(user.c.id)
#print(sql)
res = conn.execute(sql)
print(res.fetchall())




#执行SQL语句查询表信息
#sql = 'select * from user'
#result = conn.execute(sql)
#print(result.fetchall())

conn.close()


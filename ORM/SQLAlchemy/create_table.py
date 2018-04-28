# -*- coding:UTF-8 -*-

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
import MySQLdb

try:
    # mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
    engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb')
    engine.connect()#可省略，也能正常执行
    #获取元数据
    metadata = MetaData()
    #定义表
    user = Table('user_2018', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String(50)))
    color = Table('color_2018', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(20)))

    #创建数据表，如果数据表存在，则忽视
    metadata.create_all(engine)
except Exception:
    print('Error: sqlalchemy create table exception!')
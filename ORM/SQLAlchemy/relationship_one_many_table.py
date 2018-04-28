# -*- coding:UTF-8 -*-

#创建一对多的表关系

from sqlalchemy import create_engine,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb')

class User(Base):
    __tablename__ = 'nuser'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    #一对多，内容不是表名而是定义表的结构名称
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(100))
    #多的一方的book表是通过外键关联到user表的
    #Foreignkey是外键，关联user表的id字段
    user_id = Column(String(20), ForeignKey('nuser.id'))

#创建表
Base.metadata.create_all(engine)

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    liuyao = User(id='1', name='liuyao')
    ali = User(id='2', name='ali')

    session.add_all([liuyao, ali])
    session.commit()

    #创建书，并指定谁是拥有者
    Whitedeer = Book(id='1', name='White_deer', user_id='1')
    Threebody = Book(id='2', name='Three_body', user_id='2')
    session.add_all([Whitedeer, Threebody])
    session.commit()


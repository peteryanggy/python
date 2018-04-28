# -*- coding:UTF-8 -*-

#创建多对多三表关系

from sqlalchemy import create_engine,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

Host2Group = Table('host_2_group', Base.metadata,
                   Column('host_id', ForeignKey('nhosts.id'), primary_key=True),
                   Column('group_id', ForeignKey('group.id'), primary_key=True))

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb')

class Host(Base):
    __tablename__ = 'nhosts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(100), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)
    groups = relationship('Group', secondary=Host2Group, backref='host_list')

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    g1 = Group(id=1, name='g1')
    g2 = Group(id=2, name='g2')
    g3 = Group(id=3, name='g3')
    g4 = Group(id=4, name='g4')

    session.add_all([g1, g2, g3, g4])
    session.commit()


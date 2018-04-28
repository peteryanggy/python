# -*- coding:UTF-8 -*-

#创建多对多的表关系

from sqlalchemy import Column,Sequence,String,Integer,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship,backref

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb')

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    children = relationship('Child', back_populates='parent')

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship('Parent', back_populates='children')

Base.metadata.create_all(bind=engine)

if __name__ ==  '__main__':
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()

    mama = Parent(id=1, name='mamaxx')
    baba = Parent(id=2, name='babaxx')
    session.add_all([mama, baba])

    onesb = Child(id=1, name='onesb', parent_id=2)
    twosb = Child(id=2, name='twosb', parent_id=2)
    session.add_all([onesb, twosb])

    session.commit()


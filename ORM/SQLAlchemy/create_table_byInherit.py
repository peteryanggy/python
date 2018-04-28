# -*- coding:UTF-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

#生成一个SqlORM基类
Base = declarative_base()

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb')

#创建一个类继承Base基类
class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)

#创建所有表结构
Base.metadata.create_all(engine)

if __name__ == '__main__':
    try:
        SessionCls = sessionmaker(bind=engine)
        # 创建与数据库的会话
        # 注意，这里返回的sesion是一个class，不是实例
        session = SessionCls()
        # 插入字段
        h1 = Host(hostname='qd115', ip_addr='115.29.51.8')
        h2 = Host(hostname='ubuntu', ip_addr='139.65.85.66', port=80)
        h3 = Host(hostname='mysql', ip_addr='121.25.185.71', port=3306)

        # 添加多个
        session.add_all([h1, h2, h3])
        #也支持添加单个
        #session.add(h3)

        # 修改字段名称，只要没提交，此时可以修改

        #提交
        session.commit()
    except:
        session.rollback()

# -*- coding:UTF-8 -*-

from sqlalchemy import create_engine
import MySQLdb

try:
    engine = create_engine('mysql+mysqldb://root:root@127.0.0.1:3306/testdb', max_overflow=5)

    engine.execute('INSERT INTO color(id, name) VALUES("1", "peter");')
    result = engine.execute('select * from color')
    print(result.fetchall())
except Exception:
    print('Error: sqlalchemy insert data exception!')
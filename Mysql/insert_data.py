# -*- coding:UTF-8 -*-

import MySQLdb

try:
    db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='TESTDB')

    cursor = db.cursor()

    sql = '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES
    ('Mac_1', 'Mohan', 20, 'M', 3000),
    ('Mac_2', 'Mohan', 30, 'F', 4000),
    ('Mac_3', 'Mohan', 34, 'F', 5000),
    ('Mac_4', 'Mohan', 31, 'M', 3500)'''

    cursor.execute(sql)
    db.commit()
except:
    db.rollback()#回滚
finally:
    db.close()#关闭数据库连接
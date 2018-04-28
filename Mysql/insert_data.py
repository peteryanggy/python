# -*- coding:UTF-8 -*-

import MySQLdb

try:
    db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='TESTDB')

    cursor = db.cursor()

    sql = '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES('Mac', 'Mohan', 20, 'M', 3000)'''

    cursor.execute(sql)
    db.commit()
except:
    db.rollback()#回滚
finally:
    db.close()#关闭数据库连接
# -*- coding:UTF-8 -*-

import MySQLdb

db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='TESTDB')

cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')#删除表
sql = '''CREATE TABLE EMPLOYEE(
    FIRST_NAME VARCHAR(255) NOT NULL,
    LAST_NAME VARCHAR(255),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT
)'''

cursor.execute(sql)#创建表

db.close()


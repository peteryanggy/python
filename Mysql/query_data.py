# -*- coding:UTF-8 -*-

import MySQLdb

try:
    #创建数据库连接
    db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='TESTDB')

    cursor = db.cursor()

    sql = '''SELECT * FROM EMPLOYEE'''

    cursor.execute(sql)#执行SQL语句
    results = cursor.fetchall()#获取查询结果
    for row in results:#循环读取每行结果
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print('fname={},lname={},age={},sex={},income={}'.format(fname, lname, age, sex, income))
except:
    db.rollback()#异常时执行回滚
    print('Error: unable to fetch data')
finally:
    db.close()#关闭数据库连接

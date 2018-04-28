# -*- coding:UTF-8 -*-

import MySQLdb

#db = MySQLdb.connect('127.0.0.1', 'root', 'root', 'TESTDB')
db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='TESTDB')

cursor = db.cursor()

cursor.execute('select version()')
# 获取一条数据
data = cursor.fetchone()

print('Database version: {}'.format(data))

#关闭数据库
db.close()





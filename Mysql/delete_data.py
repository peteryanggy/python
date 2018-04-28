# -*- coding:UTF-8 -*-

import MySQLdb

try:
    db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='TESTDB')

    cursor = db.cursor()

    sql = '''DELETE FROM EMPLOYEE WHERE AGE >= {}'''.format(30)
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
finally:
    db.close()
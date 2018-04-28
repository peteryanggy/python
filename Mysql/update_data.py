# -*- coding:UTF-8 -*-

import MySQLdb

try:
    db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='TESTDB')

    cursor = db.cursor()

    sql = '''UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = "{}"'''.format('M')
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
finally:
    db.close()
# -*- coding: UTF-8 -*-

'''
时区转换
'''

import pytz

#打印出美国的时区
print(pytz.country_timezones('us'))

import time
import datetime

#打印出美东的current time
tz = pytz.timezone('America/New_York')
a = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
print(a)

b = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S')) + int(2) * 60
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(b)))



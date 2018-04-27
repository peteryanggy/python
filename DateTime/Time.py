# -*- coding: UTF-8 -*-

import time;    #引入time模块

#时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。
ticks = time.time() #1970-01-01 00:00:00 经过的总秒数
print(ticks)

print(time.struct_time.tm_year)
print(time.struct_time.tm_mon)
print(time.struct_time.tm_mday)
print(time.struct_time.tm_hour)
print(time.struct_time.tm_min)
print(time.struct_time.tm_sec)

wdic = {0: '周一', 1: '周二', 2: '周三', 3: '周四', 4: '周五', 5: '周六', 6: '周日'}
wday = time.struct_time.tm_wday
print(wday)
print(time.struct_time.tm_yday)
print(time.struct_time.tm_isdst)

print('\nlocaltime')    #获取当前时间
localtime = time.localtime(time.time())
print(localtime)

print('\nasctime')
loctime = time.asctime(time.localtime(time.time()))
print(loctime)

print('\nstrftime') #格式化时间
## 格式化成2016-03-20 11:45:39形式
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))

a = 'Tue Mar 06 15:24:09 2018'
print(time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')))

'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
'''
print(time.strftime('%y,%Y,%I,%H,%a,%A,%b,%B', time.localtime()))
print(time.strftime('%c', time.localtime()))    #本地相应的日期表示和时间表示
'''
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
'''
print(time.strftime('%j,%p,%U,%w,%W', time.localtime()))
#   %x 本地相应的日期表示
#   %X 本地相应的时间表示
print(time.strftime('%x,%X', time.localtime()))
#%Z 当前时区的名称
#print(time.strftime('%Z', time.localtime()))

# print(time.strftime('%%%', time.localtime()))

import calendar

#打印某月的月历
cal = calendar.month(2018, 03)
print(cal)

print('\naltzone')
'''
返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
'''
print(time.altzone)

print(time.asctime(time.localtime()))

print('\nclock')
print(time.clock())

print('\nctime')
'''
把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。 如果参数未给或者为None的时候，
将会默认time.time()为参数。它的作用相当于 asctime(localtime(secs))。
'''
print(time.ctime())
print(time.ctime(1 * 365 * 24 * 60 * 60))

print('\ngmtime')
'''
将一个时间戳转换为UTC时区（0时区）的struct_time，可选的参数sec表示从1970-1-1以来的秒数。
其默认值为time.time()，函数返回time.struct_time类型的对象。（struct_time是在time模块中定义的表示时间的对象）。
'''
print(time.gmtime())
print(time.gmtime(0))

print('\nlocaltime')
'''
接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
'''
print(time.localtime(0))
print(time.localtime(time.time()))

print('\nmktime')
gsec = time.mktime(time.gmtime())
lsec = time.mktime(time.localtime())
print(gsec)
print(lsec)
leftsec = lsec - gsec
print(leftsec)
hur = leftsec / 60 / 60
print(hur)  #8小时，北京时间与UTC时间相差 8 小时

print('\nsleep')    #函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。
print(time.strftime('%H:%M:%S', time.localtime()))
#time.sleep(5)
print(time.strftime('%H:%M:%S', time.localtime()))

print('\ntimezone')
print(time.timezone)

print('\ntzname')
print(time.tzname)



































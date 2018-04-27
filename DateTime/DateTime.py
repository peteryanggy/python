# -*- coding: UTF-8 -*-

import datetime;

print(datetime.date.year),
print(datetime.date.month),
print(datetime.date.day)

print(datetime.time)

print(datetime.datetime)

print(datetime.timedelta)

print(datetime.tzinfo)

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print('\ndate')
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

today = datetime.date(2017, 4, 5)
print(today.year)
print(today.month)
print(today.day)

print('\n__getattribute__')
print(today.__getattribute__('year'))
print(today.__getattribute__('month'))
print(today.__getattribute__('day'))

print('\n日期比较大小')
adate = datetime.date(2017, 3, 1)
bdate = datetime.date(2018, 3, 7)

print('adate: {}, bdate: {}'.format(adate, bdate))
print('adate == bdate: {}'.format(adate.__eq__(bdate)))
print('adate >= bdate: {}'.format(adate.__ge__(bdate)))
print('adate > bdate: {}'.format(adate.__gt__(bdate)))
print('adate <= bdate: {}'.format(adate.__le__(bdate)))
print('adate < bdate: {}'.format(adate.__lt__(bdate)))
print('adate != bdate: {}'.format(adate.__ne__(bdate)))

abdays = adate.__sub__(bdate)
print(type(abdays))
print('adate - bdate: {} days'.format(abdays.days))
print(abdays.seconds)
print(abdays.microseconds)
badays = bdate.__sub__(adate)
print('bdate - adate: {} days'.format(badays.days))

print('\nisocalendar')
'''
返回一个包含三个值的元组，三个值依次为：year年份，week number周数，weekday星期数（周一为1…周日为7)： 
'''
a = datetime.date(2017, 3, 18)
print(a.isocalendar())
print(a.isocalendar()[0])
print(a.isocalendar()[1])
print(a.isocalendar()[2])

print('\nisoformat')    #返回符合ISO 8601标准 (YYYY-MM-DD) 的日期字符串
a = datetime.date(2018, 3, 18)
print(a.isoformat())

print('\nisoweekday')   #返回符合ISO标准的指定日期所在的星期数（周一为1…周日为7)
a = datetime.date(2018, 3, 7)
print(a.isoweekday())

print('\nweekday')  #返回的周一为 0, 周日为 6
print(a.weekday())

print('\ntimetuple')
print(a.timetuple())
print(a.timetuple().tm_year)
print(a.timetuple().tm_mon)
print(a.timetuple().tm_mday)
print(a.timetuple().tm_hour)
print(a.timetuple().tm_min)
print(a.timetuple().tm_sec)

print('\ntoordinal')    #返回公元公历开始到现在的天数。公元1年1月1日为1
print(a.toordinal())

print('\nreplace')
#返回一个替换指定日期字段的新date对象。参数3个可选参数，分别为year,month,day。注意替换是产生新对象，不影响原date对象。
b = a.replace(2015, 1, 26)
print(b)

print('\nresolution')   #date对象表示日期的最小单位。这里是天。
print(datetime.date.resolution.days)
print(datetime.timedelta(1))

print('\nfromordinal')
#将Gregorian日历时间转换为date对象；Gregorian Calendar ：一种日历表示方法，类似于我国的农历，西方国家使用比较多。
a = datetime.date(2017, 1, 14)
b = a.toordinal()
print(datetime.date.fromordinal(b))

import time;

#根据给定的时间戮，返回一个date对象
print('\nfromtimestamp')
dt = datetime.date.fromtimestamp(time.time())
print(dt)

print('\ntoday')    #返回当前日期
print(datetime.date.today())

print('\nmax/min')
#max: date类能表示的最大的年、月、日的数值
#min: date类能表示的最小的年、月、日的数值
print(datetime.date.max)
print(datetime.date.min)

print('\n日期的字符串输出')
print(a.strftime('%Y-%m-%d %H:%M:%S'))
print(a.__str__())
print(a.__format__('%Y-%m-%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%y/%m/%d'))
#print(a.__format__('%D'))

print(a.ctime())

print('\ntime')
# 时、分、秒、微秒
a = datetime.time(12, 20, 59, 899)
print(a)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)
print(a.tzinfo)

print('\n__getattribute__')
print(a.__getattribute__('hour'))
print(a.__getattribute__('minute'))
print(a.__getattribute__('second'))
print(a.__getattribute__('microsecond'))

print('\n时间比较大小')
a = datetime.time(12, 20, 59, 899)
b = datetime.time(11, 20, 59, 899)

print('a == b: {}'.format(a.__eq__(b)))
print('a >= b: {}'.format(a.__ge__(b)))
print('a > b: {}'.format(a.__gt__(b)))
print('a <= b: {}'.format(a.__le__(b)))
print('a < b: {}'.format(a.__lt__(b)))
print('a != b: {}'.format(a.__ne__(b)))

print('\nnonzero')  #判断时间对象是否非零，返回值为True/False
print(a.__nonzero__())

print('\ntime.max/min/resolution')
print(datetime.time.max)
print(datetime.time.min)
print(datetime.time.resolution)

print('\n时间的字符串输出')
print(a.__format__('%H:%M:%S'))
print(a.strftime('%H/%M/%S'))
print(a.isoformat())    #ISO标准输出
print(a.__str__())  #简单的获得时间的字符串


print('\ndatetime类')
print(datetime.datetime.now())
# 年、月、日、时、分、秒、微秒
a = datetime.datetime(2017, 2, 5, 10, 3, 50, 909876)
print(a)

print(a.date()) #返回datetime对象的日期部分
print(a.time()) #返回datetime对象的时间部分

#返回UTC时间元组
print(a.utctimetuple())

print('datetime.combine: 日期与时间合并')
mydate = datetime.date(2000, 7, 5)
mytime = datetime.time(10, 2, 4, 234521)
dtcomb = datetime.datetime.combine(mydate, mytime)
print(dtcomb)

print('\nnow/utcnow')
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

print('\nstrptime: 根据string, format 2个参数，返回一个对应的datetime对象')
newdt = datetime.datetime.strptime('2017-08-15 15:26:59', '%Y-%m-%d %H:%M:%S')
print(newdt)

print('\nutcfromtimestamp')
print(datetime.datetime.utcfromtimestamp(time.time()))

print('\ntimedelta: 用来计算二个datetime对象的差值')
adt = datetime.datetime(2017, 5, 3, 10, 3, 5, 123456)
bdt = datetime.datetime(2017, 5, 3, 10, 3, 4, 123456)
abdelta = adt.__sub__(bdt)
print(abdelta.days)
print(abdelta.seconds)
print(abdelta.microseconds)

print('\n获取当前日期时间')
now = datetime.datetime.now()
print(datetime.datetime.today())
print('date: {}'.format(now.date()))
print('time: {}'.format(now.time()))

print('\n获取上个月第一天和最后一天的日期')
today = datetime.date.today()
mlast_day = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
mfirst_day = datetime.date(mlast_day.year, mlast_day.month, 1)
print('today: {}\nmlast_day: {}, mfirst_day: {}\n'.format(today, mlast_day, mfirst_day))

print('\n获取时间差')
stime = datetime.datetime.now()
etime = datetime.datetime.now()
print((etime - stime).seconds)

print('\n对时间自身进行加加减')

now = datetime.datetime.now()
print('now: {}'.format(now))
print('\n加/减一天')
nowAddDays = now + datetime.timedelta(days=1)
nowSubDays = now - datetime.timedelta(days=1)
print(nowAddDays)
print(nowSubDays)

print('\n加/减一小时')
nowAddHours = now + datetime.timedelta(hours=1)
nowSubHours = now - datetime.timedelta(hours=1)
print(nowAddHours)
print(nowSubHours)
print('\n加/减一分钟')
nowAddMinutes = now + datetime.timedelta(minutes=1)
nowSubMinutes = now - datetime.timedelta(minutes=1)
print(nowAddMinutes)
print(nowSubMinutes)

print('\n计算上周一和周日的日期')
today = datetime.date.today()
today_weekday = today.isoweekday()
last_sunday = today - datetime.timedelta(days=today_weekday)
last_monday = last_sunday - datetime.timedelta(days=6)
print('today_weekday: {}'.format(today_weekday))
print('last_sunday: {}'.format(last_sunday))
print('last_monday: {}'.format(last_monday))

print('\n计算指定日期当月最后一天的日期和本月天数')

def eomonth(date_object):
    if date_object.month == 12:
        next_month_first_date = datetime.date(date_object.year + 1, 1, 1)
    else:
        next_month_first_date = datetime.date(date_object.year, date_object.month + 1, 1)
    return next_month_first_date - datetime.timedelta(1)

datearg = datetime.date(2018, 3, 2)
ret0 = eomonth(datearg)
print(ret0)
print(ret0.day)

print('\n 计算指定日期下个月当天的日期')

def edate(date_object):
    if date_object.month == 12:
        next_month_date = datetime.date(date_object.year + 1, 1, date_object.day)
    else:
        next_month_first_day = datetime.date(date_object.year, date_object.month + 1, 1)
        if date_object.day > eomonth(next_month_first_day).day:
            next_month_date = datetime.date(date_object.year, date_object.month + 1, eomonth(next_month_first_day).day)
        else:
            next_month_date = datetime.date(date_object.year, date_object.month + 1, date_object.day)
    return next_month_date

date = datetime.date(2017,12,20)
print(edate(date))

print('\n获得本周一到今天的时间段并获得上周对应同一时间段')
today = datetime.date.today()
this_monday = today - datetime.timedelta(today.isoweekday() - 1)
last_monday = this_monday - datetime.timedelta(7)
last_weekday = today - datetime.timedelta(7)
print(today)
print(this_monday)
print(last_monday)
print(last_weekday)






























































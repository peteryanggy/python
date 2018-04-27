# -*- coding: UTF-8 -*-

import calendar;

'''
返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
'''
#print(calendar.calendar(2018, 3))

#返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
print('\nfirstweekday')
print(calendar.firstweekday())

print('\nisleap')   #是闰年返回True，否则为false。
print(calendar.isleap(2018))

print('\nleapdays') #返回在Y1，Y2两年之间的闰年总数。
print(calendar.leapdays(2000, 2018))

print('\nmonth')
'''
返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
'''
print(calendar.month(2018, 3))

'''
返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。
Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
'''
print('monthcalendar')
march = calendar.monthcalendar(2018, 3)
print(march)
for m in march:
    print(m)

print('\nmonthrange 不理解结果含义')
#返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
print(calendar.monthrange(2018, 3))

print('\nsetfirstweekday')  #设置每周的起始日期码。0（星期一）到6（星期日）。
calendar.setfirstweekday(1)
print(calendar.month(2018, 3))

print('\nweekday')
wdic = {0: '周一', 1: '周二', 2: '周三', 3: '周四', 4: '周五', 5: '周六', 6: '周日'}
wday = calendar.weekday(2018, 3, 6)
print(wdic[wday])


















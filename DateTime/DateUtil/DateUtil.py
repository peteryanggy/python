# -*- coding: UTF-8 -*-

'''
python-dateutil
parser是根据字符串解析成datetime，而rrule是则是根据定义的规则来生成datetime。
'''

from dateutil.parser import parse

print(parse('Wed, Nov 12'))
print(parse('2017-03-05'))
print(parse('20140509'))

print(parse('09:38:21'))
print(parse('2018-01-05 12:52:24'))

print('\n不理解')
print('parse(\'2013,05,02\'):'),
print(parse('2013,05,02'))

print('parse(\'08,14\'):'),
print(parse('08,14'))
#print(parse(u'This is the wonderful moment 12:00:30, I feel good', fuzzy=True))


from dateutil.rrule import *;

print('\nrrule')
print(list(rrule(DAILY, dtstart=parse('2013-08-01'), until=parse('2013-08-03'))))   ##2013-08-01到2013-08-03每日
print(list(rrule(DAILY,interval=3,dtstart=parse('2013-03-01'),until=parse('2013-03-15'))))   #间隔3天输出一个日期
print(list(rrule(DAILY, count=3, dtstart=parse('2013-03-01'), until=parse('2013-03-15'))))  #只生成3个
print(list(rrule(DAILY, byweekday=(MO, TU), dtstart=parse('2018-03-01'), until=parse('2018-03-18')))) #只匹配周一周二的日期
print(list(rrule(MONTHLY, dtstart=parse('2013-05-19'), until=parse('2013-08-15')))) #按月为单位







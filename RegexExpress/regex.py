# -*- coding: UTF-8 -*-

import re

#span() 匹配的子串索引

ret1 = re.match('www', 'www.baidu.com').span()
print(ret1)#在起始位置匹配
for i in list(ret1):
    print(i),

print('\r\n')
print(re.match('com', 'www.baidu.com'))# 不在起始位置匹配

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"
'''
首先，这是一个字符串，前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，也就是忽略转义字符。但是这个字符串里没有反斜杠，所以这个 r 可有可无。
 (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
 (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
 后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
 
matchObj.group() 等同于 matchObj.group(0)，表示匹配到的完整文本字符
matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的

因为只有匹配结果中只有两组，所以如果填 3 时会报错。   
'''

# re.search 扫描整个字符串并返回第一个成功的匹配
line = 'www.baidu.com'

r1 = re.search('www', line).span()
r2 = re.search('com', line).span()
print(r1)
print(r2)

print(line[r1[0]:r1[1]]) #提取0-3索引号的字符，不包含3
print(line[r2[0]:r2[1]]) #提取10-13索引号的字符，不包含13

#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

line = 'Cats are smarter than dogs';

matchObj = re.match(r'dogs', line, re.M | re.I)
if(matchObj):
    print('match --> matchObj.group(); {}'.format(matchObj.group()))
else:
    print('No match!')

matchObj = re.search(r'dogs', line, re.M | re.I)
if(matchObj):
    print('search --> matchObj.group(): {}'.format(matchObj.group()))
else:
    print('No match!')

#检索和替换
'''
re.sub(pattern, repl, string, count=0, flags=0)
参数：

pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

'''
phone = '2004-959-559 # 这是一个国外电话号码'

#删除注释
num = re.sub(r'#.*', '', phone)
print('phone:{}'.format(num))

#删除非数字字符
num = re.sub(r'\D', '', phone)
print('phone:{}'.format(num))

#匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

#(?P<value>\d+) 将匹配项用 value 来标识，通过 .group('value') 来获取
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

#re.compile 函数
#compile 函数用于编译正则表达式，生成一个正则表达式

pattern = re.compile(r'\d+') #用于匹配至少一个数字
m = pattern.match('one12twothree34four')
print(m)

#从指定的索引号开始匹配
m = pattern.match('one12twothree34four', 3, 10)
print(m.group())
print(m.span())#返回匹配的子串索引

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = pattern.match('Hello World Wide Web')
print(m)

print(m.group(0))
print(m.span(0))
print(m.group(1))
print(m.span(1))
print(m.group(2))
print(m.span(2))
print(m.groups())
#print(m.group(3)) #报错

'''
findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
notice: match 和 search 是匹配一次 findall 匹配所有
'''

pattern = re.compile(r'\d+') #查找数字
ret1 = pattern.findall('runoob 123 google 456')
ret2 = pattern.findall('run88oob123google456', 1, 6)

print(ret1)
print(ret2)

#finditer 与 findall 功能类似，只是返回结果为一个迭代器
it = re.finditer(r'\d+', 'run88oob123google456')
for match in it:
    print(match.group())

#re.split 方法按照能够匹配的子串将字符串分割后返回列表
#使用 '\W+' 表达式作为分隔匹配规则，去分隔字符 'runoob, runoob, runoob.'
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print(re.split('\W+', ' runoob, runoob, runoob.', 1))#只分隔一次
print(re.split('a*', 'hello world'))#对于一个找一到匹配的字符串而言，split 不会对其作出分割

'''
正则表达式对象
re.RegexObject
re.compile() 返回 RegexObject 对象。

re.MatchObject
group() 返回被 RE 匹配的字符串。

start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置
'''






















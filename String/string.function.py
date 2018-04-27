# -*- coding: UTF-8 -*-

'''
string 内建函数
'''

print('abc.EF89ea'.capitalize())    #将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
print('runoob'.center(20))  #返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。
print('runoob'.center(20, '*')) #使用指定字符填充
print('rub7'.center(11, '%')) #当 width 参数小于等于原字符串的长度时，原样返回；
print('h'.center(10, '-'))  #无法使左右字符数相等时候，当原字符串长度为奇数是: 右侧字符会比左侧多 1，当为偶数时，左侧字符会比右侧多 1

letters = 'helloworld'
print(letters.count('l', 0, len(letters)))  #统计字符串里某个字符出现的次数

#编解码
orgstr = 'this is string example....wow!!!'
enstr = orgstr.encode('base64', 'strict')

'''
默认为 'strict',意为编码错误引起一个UnicodeError。 
他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
'''
print('Encoded string:'),
print(enstr)

print('Decoded string:'),
print(enstr.decode('base64', 'strict'))

print('\nendswith/startswith')
print('hello'.endswith('o', 0, len('hello')))   #注意开始索引默认为 0，len 为字符串的实际长度值: True
print('hello'.endswith('o', 0, len('hello') - 1))   #False

#检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
print('hello'.startswith('h', 0, len('hello')))


#把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 4
print('hello\tworld\t!')    #默认tab为 4
print('hello\tworld\t!'.expandtabs(0))  #默认空格数为 0
print('hello\tworld\t!'.expandtabs(16)) #设置用于替代tab的空格数量为 16

print('hello'.find('o', 0, len('hello')))   #检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
print('hello{}{}!'.format('\t', 'world'))
print('hello'.index('l', 0, len('hello')))  #跟find()方法一样，只不过如果str不在 string中会报一个异常

print('12365'.isalnum())   #如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print('hello'.isalpha())    #如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
print('123654'.isdigit())   #如果 string 只包含数字则返回 True 否则返回 False.

#print('12354'.isdecimal()) #如果 string 只包含十进制数字则返回 True 否则返回 False.

print('hello'.islower())    #如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

print('\nisnumeric')    #这种方法是只针对unicode对象。注：定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可，
print(u'1235'.isnumeric())    #如果 string 中只包含数字字符，则返回 True，否则返回 False

print('   '.isspace())  #如果 string 中只包含空格，则返回 True，否则返回 False.

print('\nistitle')  #如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
print('Hello World!'.istitle())
print('hello World!'.istitle())

print('\nisupper')  #如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
print('HELLO WORLD!'.isupper())
print('Hello World!'.isupper())
print('!@#$%^45897'.isupper())

print('\njoin') #以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
print('$%'.join('hello'))
print('#'.join(['1', '2', '3']))

print('\nljust/rjust')
print('run'.ljust(8))
print('run'.rjust(8))

print('\nlower')    #转换 string 中所有大写字符为小写.
print('Hello wORld'.lower())

print('\nmax/min')
print(max('hello'))    #返回字符串 str 中最大的字母。
print(min('hello'))    #返回字符串 str 中最小的字母。

print('\npartition')
'''
根据指定的分隔符将字符串进行分割。
如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
'''
print('http://www.baidu.com'.partition('://'))

print('\nreplace')  #把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
print('hello world!'.replace('o', 'x'))

print('\nrfind')    #类似于 find()函数，不过是从右边开始查找.
print('hello'.rfind('o', 0, len('hello')))

print('\nrindex')
print('hello'.rindex('o', 0, len('hello')))

print('\nrpartition')
print('http://www.baidu.com'.rpartition('://'))

print('\nlstrip/rstrip')    #截掉 string 左边的空格/删除 string 字符串末尾的空格.
print('   hello'.lstrip())
print('hello    '.rstrip())

print('   hello    '.strip())   #在 string 上执行 lstrip()和 rstrip()

print('\nsplit')
print('hello'.split('l'))   #以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串

print('\nsplitlines')   #按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
print('hello \nworld\r\nq!\rwelcome!'.splitlines(True))
print('hello \nworld\r\nq!\rwelcome!'.splitlines(False))

print('\nswapcase') #翻转 string 中的大小写
print('Hello World!'.swapcase())

print('\ntitle')    #返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
print('hello world!'.title())

from string import maketrans    # 必须调用 maketrans 函数。

print('\nmaketrans')
'''
maketrans 用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

注：两个字符串的长度必须相同，为一一对应的关系。
'''
intab = 'aeiou'
outtab = '12345'
trantab = maketrans(intab, outtab)

content = 'this is string example....wow!!!'
# translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。
print(content.translate(trantab, 'e'))

print('\nzfill')    #返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
print('hello'.zfill(10))










































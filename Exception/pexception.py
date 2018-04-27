# -*- coding: UTF-8 -*-

try:
    fh = open('testfile', 'r')
    fh.write('这是一个测试文件，用于测试异常!')
except:# IOError:
    print('Error ：没有找到文件或读取文件失败!')
else:
    print('内容写入成功!')
    fh.close()
finally:
    fh.close()


def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:    #异常参数信息
        print('参数没有包含数据:{}'.format(Argument))

temp_convert('uieo')


def functionName(level):
    if(level < 1):
        raise Exception('Invalid level:{}'.format(level))   #触发异常

#functionName(-2)

class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise NetworkError('Bad hostname')
except NetworkError, e:
    print(e.args)


















# -*- coding: UTF-8 -*-

import Module.support   #相同文件夹下模块导入

Module.support.print_func('peter')

#import Module.NMath.nmath   #不同文件夹下模块导入
#result = Module.NMath.nmath.npow(2, 4) #完整包写法 Module.NMath.nmath.npow

from Module.NMath import nmath  #从包Module.NMath中，导入模块 nmath.py
result = nmath.npow(2, 4)   #简写nmath.npow
print('npow:{}'.format(result))

import ThirdModule.tprint as tp #导入模块并指定别名

tp.tprint_func('ygy')

from Module.NMath import lprint #从模块[Module.NMath]中导入指定部分[lprint]
lprint.lprint_func('Microsoft')

from think.tmath import *   #导入模块中的全部内容
from think.tprint import *
print(tpow(2, 4))   #直接调用模块中定义的函数
tprint_func('Li Yang')

print('dir()函数')    #返回一个排好序的字符串列表，内容是一个模块里面定义的名字
content = dir(lprint)
print(content)

#globals() locals()
def tmethod(msg):
    text = '2018-03-19'
    say = 'welcome {},{}'.format(text, msg)
    print('{}'.format(say))
    gs = globals()  #返回所有在该函数中能访问的全局名字，返回值类型是字典
    ls = locals()   #返回所有在该函数中能访问的命名，返回值类型是字典
    print('globals(): {}'.format(gs.keys()))
    print('locals(): {}'.format(ls.keys()))
tmethod('net influencer')

#reload() 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次
#可以调用 reload() 函数来重新导入之前导入过的模块，reload(module_name)





















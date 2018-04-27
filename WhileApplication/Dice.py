# -*- coding: UTF-8 -*-

#骰子游戏

import random
import sys
import time

result = []
while True:
    result.append(int(random.uniform(1, 7)))
    result.append(int(random.uniform(1, 7)))
    result.append(int(random.uniform(1, 7)))

    print(result)
    count = 0
    index = 2
    pointStr = ''

    while index >= 0:   #统计当前3个骰子投掷点数
        currPoint = result[index]
        count += currPoint
        index -= 1
        pointStr += ' '
        pointStr += str(currPoint)
    if count <= 11:
        sys.stdout.write(pointStr + ' -> 小\n')
        time.sleep(1) #睡眠1秒
    else:
        sys.stdout.write(pointStr + ' -> 大\n')
        time.sleep(1)
    result = []

#END
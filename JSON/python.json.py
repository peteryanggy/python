# -*- coding:UTF-8 -*-

import json

data = [{'a': 1, 'b': 2, 'c': 3}]

jsonStr = json.dumps(data)
print(jsonStr)

#格式化输出JSON字符串
print(
    json.dumps({'a': 'baidu', 'b': 6},
                 sort_keys=True,
                 indent=4,
                 separators=(',', ': '))
)


jsonObj = json.loads(jsonStr)
print(jsonObj)

print('class json')

class location(object):
    def __init__(self):
        self.lon = 0
        self.lat = 0
        self.speed = 0
        self.direction = 0
        self.altitude = 0

loc = location()
loc.lon = 113.0988
loc.lat = 23.090
loc.speed = 100
loc.direction = 56
loc.altitude = 1000

locdic = loc.__dict__
print(type(locdic))
locjson = json.dumps(locdic)
print(locjson)

rloc = json.loads(locjson)
print(rloc)




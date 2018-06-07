# -*- coding:UTF-8 -*-

import demjson

data = [{'a': 1, 'b': 2}]

jsonStr = demjson.encode(data)
print(jsonStr)

jsonObj = demjson.decode(jsonStr)
print(jsonObj)

class myObject(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

me = myObject('peter', 32)
medic = me.__dict__

meJson = demjson.encode(medic)
print(meJson)

meObject = demjson.decode(meJson)
print(meObject)




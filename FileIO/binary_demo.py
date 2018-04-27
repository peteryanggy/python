# -*- coding: UTF-8 -*-

print(b"python")
print(b"1"[0])  #设想输出应该是 0x31

print(b'x24')   #设想输出应该是 $

print(bytes([31, 32, 33]))

#print(bytes.fromhex('31, 32'))

print('$'.encode('ascii'))
print('$'.encode('ascii')[0])

src = bytearray('123456789', 'utf-8')
for e in src:
    print(e)

import struct

a = 12.34
bes = struct.pack('f', a)
print(bes)

b, = struct.unpack('f', bes)
print(b)




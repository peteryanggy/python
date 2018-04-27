# -*- coding: UTF-8 -*-

import struct

filename = "F:\Tmp\\binary2.bin"
with open(filename, 'wb') as fd:
    i = 1
    bi = struct.pack('i', i)
    fd.write(bi)

    f = 2.1
    bf = struct.pack('f', f)
    fd.write(bf)

    d = 3.1
    bd = struct.pack('d', d)
    fd.write(bd)

    l = 4L
    bl = struct.pack('l', l)
    fd.write(bl)

with open(filename, 'rb') as fd:
    byte_len = 4
    bi = fd.read(byte_len)
    print(list(struct.unpack('i', bi)))

    bf = fd.read(byte_len)
    print(struct.unpack('f', bf))

    byte_len = 8
    bd = fd.read(byte_len)
    print(struct.unpack('d', bd))

    bl = fd.read(byte_len)
    print(struct.unpack('l', bl))



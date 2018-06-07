# -*- coding:UTF-8 -*-

import socket

HOST = 'localhost'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    #msg = bytes(input('>>:'), encoding='utf8')
    msg = 'hello peter'
    print(msg)

    s.sendall(msg)

    data = s.recv(1024)

    print('Received:{}'.format(repr(data)))


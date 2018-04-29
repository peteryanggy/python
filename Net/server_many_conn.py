# -*- coding:UTF-8 -*-

import socket
import sys
from thread import *

host = socket.gethostname()
port = 8888

endpoint = (host, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socked created')

try:
    server.bind(endpoint)
except socket.error, msg:
    print('Bind failed. Error code: {}, Message:{}'.format(str(msg[0]), msg[1]))
    sys.exit()

print('Socket bind complete')

server.listen(10)
print('Socket now listening[{}]...'.format(endpoint))

def client_thread(conn):
    conn.send('Welcome to the server. Type something and hit entern')

    while True:
        data = conn.recv(1024)
        reply = 'Ok...{}'.format(data)
        if not data:#not  逻辑运算符 非，即C#中的 !
            break
        conn.sendall(reply)
    conn.close()

while True:
    conn, addr = server.accept()
    print('Connected with {}:{}'.format(addr[0], str(addr[1])))

    start_new_thread(client_thread, (conn, ))

server.close()

# -*- coding:UTF-8 -*-

from socket import *

ip_port = ('127.0.0.1', 9999)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    msg = input('>>:').strip()

    if not msg: continue
    if msg == 'exit': break

    tcp_client.send(msg.encode('utf-8'))

    data = tcp_client.recv(buffer_size)
    print('接收到客户端发来的信息:{}'.format(data.decode('utf-8')))

tcp_client.close()

# -*- coding:UTF-8 -*-

import socket
import datetime
import sys

'''
Address Family：可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）
Type：套接字类型，可以是 SOCKET_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCKET_DGRAM（数据报套接字，主要用于 UDP 协议）
'''
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()  # 获取本地主机名
    port = 5060
    endpoint = (host, port)  # 元组
    server.bind(endpoint)  # 绑定端口
    print(endpoint)

    server.listen(5)  # 开启监听
    print('Server listening......')
    while True:
        client, addr = server.accept()  # 返回一个包含两个元素的元组
        print('Client:{}'.format(addr))
        client.send('{}\tWelcome!\r\n'.format((datetime.datetime.now())))
        client.close()  # 关闭连接
except socket.errno, msg:
    print('Failed to create socket. Error code:{},{}'.format(str(msg[0]), msg[1]))
    sys.exit()

# -*- coding:UTF-8 -*-

from socket import *

ip_port = ('127.0.0.1', 9999)
buffer_size = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    data, addr = udp_server.recvfrom(buffer_size)
    print(data)

    udp_server.sendto(data.upper(), addr)



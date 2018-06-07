# -*- coding:UTF-8 -*-

from socket import *

ip_addr = ('127.0.0.1', 9999)
buffer_size = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = 'hello peter' #input('>>:')

    udp_client.sendto(msg.encode('utf-8'), ip_addr)

    data, addr = udp_client.recvfrom(buffer_size)
    print(data.decode('utf-8'))

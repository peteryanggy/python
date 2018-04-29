# -*- coding:UTF-8 -*-

import socket
import datetime
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
#port = 5060
#endpoint = (host, port)

host = 'www.baidu.com'
port = 80

try:
    #域名解析IP
    remote_ip = socket.gethostbyname(host)
    endpoint = (remote_ip, port)

    message = 'GET / HTTP/1.1\r\n\r\n'
    client.connect(endpoint)
    client.sendall(message)

    print('{} received:\r\n{}'.format(datetime.datetime.now(), client.recv(1024 * 4)))
    client.close()
except socket.error:
    print('Hostname could not be resolved. Exiting!')
    sys.exit()

#print('Ip address of ' + host + ' is ' + remote_ip)


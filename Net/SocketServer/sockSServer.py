# -*- coding:UTF-8 -*-

import SocketServer

'''
SocketServer模块中主要的有以下几个类：

1、BaseServer    包含服务器的核心功能与混合类（mix-in）的钩子功能。这个类主要用于派生，不要直接生成这个类的类对象，可以考虑使用TCPServer和UDPServer类。
2、TCPServer     基本的网络同步TCP服务器
3、UDPServer     基本的网络同步UDP服务器

4、ForkingTCPServer  　　  是ForkingMixIn与TCPServer的组合
5、ForkingUDPServer　　　 是ForkingMixIn与UDPServer的组合

6、ThreadingUDPServer　　是ThreadingMixIn和UDPserver的组合
7、ThreadingTCPServer　　 是ThreadingMixIn和TCPserver的组合

8、BaseRequestHandler　　 必须创建一个请求处理类，它是BaseRequestHandler的子类并重载其handle()方法。
9、StreamRequestHandler　　      实现TCP请求处理类的
10、DatagramRequestHandler　　实现UDP请求处理类的

11、ThreadingMixIn　　实现了核心的线程化功能，用于与服务器类进行混合(mix-in)，以提供一些异步特性。不要直接生成这个类的对象。
12、ForkingMixIn　　   实现了核心的进程化功能，用于与服务器类进行混合(mix-in)，以提供一些异步特性。不要直接生成这个类的对象。
'''

class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        print('conn is: {}'.format(self.request))
        print('addr is: {}'.format(self.client_address))

        while True:
            data = self.request.recv(1024)
            if data:
                print('接收到客户端的信息:{}'.format(data))

                #发送信息
                self.request.sendall(data.upper())
            else:
                break

if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()  #连接循环

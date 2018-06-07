# -*- coding:UTF-8 -*-

import select
import socket
import Queue
import sys

'''
下面程序实现的功能是，使用select实现对多连接的非阻塞监控。
select会将连接进行不同状态管理(可读、可写、出错)，每个连接不同时刻处于其中一个状态，
针对不同状态主程序中，会有相应的处理过程

1、可读连接
    1.1 服务端本身
        接收客户端连接，并为连接创建字典记录
    1.2 连接客户端
        表示客户端有数据待接收，接收数据(将接收到的数据，缓存在客户端对应的数据接收队列中)，
        并将连接放置到可写列表中，触发可写处理流程
        
2、可写连接
    将待发送的数据，发送给客户端
    
3、错误连接
    断开发生错误的连接，及释放相关资源
'''

server = socket.socket()
server.setblocking(False)

port = 9999
server_address = ('localhost', port)

server.bind(server_address)
server.listen(5)

#所有连接进来的对象都放在inputs
inputs = [server, ] #自己也要监控，因为server本身也是个对象
#需要发送数据的对象
outputs = []

#对外发送数据的队列，记录在字典中
message_queue = {}

print(sys.stderr, 'starting up on {} port {}'.format(server_address, port))

while True:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    #如果没有斜体fd就绪，那程序就会一直阻塞在这里

    for s in readable: #每一个s就是一个socket
        if s is server:
            #别忘了了，上面我们server自己也当做一个fd放在了inputs列表里，传给了select
            #如果s是server，代表server这个fd就绪了，就是有活动了，什么情况下它才有活动呢，
            #当前是有新的连接进来的时候
            #新连接进来了，接受这个连接
            conn, client_addr = s.accept()
            print('new connection from{}'.format(client_addr))
            conn.setblocking(0)
            inputs.append(conn)

            '''
            为了不阻塞整个程序，我们不会立刻在这里开始接收客户端发来的数据，把它放到inputs里，
            下一次loop时，这个新连接就会被交给select去监听，如果这个连接的客户端发来了数据，
            那这个连接的fd在server端就会变成就绪的，
            select就会把这个连接返回到readable列表里，然后你就可以loop readable列表,
            取出这个连接，开始接收数据了
            '''
            message_queue[conn] = Queue.Queue()
            #接收到客户端的数据后，不立刻返回，暂存在队列里面，以后发送
        else: #s不是server的话，那就只能是一个与客户端建立的连接的fd
            #客户端的数据发送过来了，在此接收
            data = s.recv(1024)
            if data:
                print('received [{}] from {}'.format(data, s.getpeername()[0]))
                message_queue[s].put(data)  #收到的数据先放到queue里面，一会返回给客户端
                if s not in outputs:
                    outputs.append(s)   #为了不影响处理与其它客户端的连接，这里不立刻返回数据客户端
            else: #如果接收到的data不代表什么，代表客户端断开了
                print('client [{}] closed'.format(s))

                if s in outputs:
                    #既然客户端断开了，我们就不再用给它返回数据了，
                    #所以这时如果这个客户端的连接对象还在outputs列表中，就把它删除掉
                    outputs.remove(s)

                inputs.remove(s) #这个必然在inputs中，也删掉
                s.close()

                #关闭的连接在队列中也删除
                del message_queue[s]

    for s in writable:
        try:
            next_msg = message_queue[s].get_nowait()
        except Queue.Empty:
            #没有数据了，该连接对象队列为空，停止检测
            print('output queue for [{}] is empty'.format(s.getpeername()[0]))
            outputs.remove(s)
        else:
            print('send {} to {}'.format(next_msg, s.getpeername()[0]))
            s.send(next_msg)

    for s in exceptional:
        print('handling exceptional condition for {}'.format(s.getpeername()[0]))
        #从inputs中删除
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        #删除队列
        del message_queue[s]



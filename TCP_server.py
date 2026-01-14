#  =====  TCP服务端程序 server.py =====

#对socket编程的操作系统的调用全部封装到socket库里面了,所以要导入
from socket import *

# 变量名大写通常作为配置项
#主机地址是0.0.0.0,
IP = '0.0.0.0'
PORT = 50000
BUFFER = 512

listen_socket = socket(AF_INET,SOCK_STREAM)
listen_socket.bind((IP,PORT))

# 使socket处于监听状态，等待客户端的连接请求
# 参数五：表示最多接受多少个等待连接的客户端
listen_socket.listen(5)
print(f'服务端启动成功，在{PORT}接口等待客户端连接...')

dataSocket,addr = listen_socket.accept()
print(f'接收到一个客户连接：',addr)

while True:
    recved = dataSocket.recv(BUFFER)
    if not recved:
        break

    info = recved.decode()
    print(f'收到对方信息：{info}')

    dataSocket.send(f'服务端接收到了信息{info}'.encode())

# 服务器调用完关闭socket
dataSocket.close()
listen_socket.close()

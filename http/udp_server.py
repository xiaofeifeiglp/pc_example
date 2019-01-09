# 服务器的作用是为客户端进行服务器，进行服务器必须有固定的地址跟端口
# 初始化套接字
# 绑定地址与端口
# 接收数据
# 关闭

import socket

def main():
    '''这个是udp的服务器'''
    # 初始化套接字
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定地址与端口
    socket_server.bind(('', 8081))
    # 接收数据
    data = socket_server.recvfrom(1024)
    print(data)
    print('解码:', data[0].decode('utf-8'))
    print('地址:', data[1])
    # 关闭
    socket_server.close()

if __name__ == '__main__':
    main()

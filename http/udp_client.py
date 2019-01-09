# 初始化socket(套接字)
# 发送数据
# 关闭

import socket

def main():
    '''创建一个udp客户端'''
    # 初始化socket(套接字)
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送数据
    socket_client.sendto('我是中国人'.encode('utf-8'), ('192.168.47.133', 8080))
    # 接收数据，最大一次接收1024个字节
    data = socket_client.recvfrom(1024)
    print(data)
    print('接收到的数据:', data[0].decode('utf-8'))
    print('接收到的地址:', data[1])
    # 关闭
    socket_client.close()

# 广播
def main1():
    '''创建一个广播'''
    # 初始化
    socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 设置广播及发送
    socket_udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # 发送
    socket_udp.sendto('广播来类，下课了'.encode('utf-8'), ('255.255.255.255',8080))
    # 关闭
    socket_udp.close()

if __name__ == '__main__':
    main1()
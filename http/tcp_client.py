# 初始化套接字
# 连接
# 发送
# 接收数据
# 关闭
import socket

def main():
    '''tcp客户端'''
    # 初始化套接字
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接
    tcp_client.connect(('192.168.47.133', 8080))
    # 发送
    tcp_client.send('我要发了'.encode('utf-8'))
    tcp_client.send('我还发'.encode('utf-8'))

    # 接收数据
    data = tcp_client.recv(1024)
    print(data)
    print('解码:',data.decode('utf-8'))

    # 关闭
    tcp_client.close()

if __name__ == '__main__':
    main()
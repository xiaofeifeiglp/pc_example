# 初始化
# 绑定端口与地址
# 被动模式
# 接收客户端的请求
# 处理客户端的请求
# 关闭
import socket
def client_exec(client):
    '''处理客户端的请求'''
    # 接收数据
    while True:
        # 如果tcp客户端关闭了会自动发送空的字符给我们
        data = client.recv(1024)
        # print(data)
        # print('编码:', data.decode('utf-8'))
        # 判断我们的数据如果接收到的是空的数据，那么推出循环
        if data:
            print('当前有数据:', data.decode('utf-8'))
            # 回复信息
            client.send('我接收到了数据'.encode('utf-8'))
        else:
            break
    print('客户端关闭了')
    client.close()

def main():
    '''tcp服务器'''
    # 初始化
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口与地址
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server.bind(('', 8082))
    # 被动模式
    tcp_server.listen(128)
    # 接收客户端的请求
    while True:
        client, address = tcp_server.accept()
        print(client)
        # 处理客户端的请求
        client_exec(client)
    # 处理客户端的请求
    # 关闭
    tcp_server.close()

if __name__ == '__main__':
    main()
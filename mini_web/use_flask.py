# 1.创建一个tcp服务器端
# 2. 循环接收我们浏览器的请求
# 3. 处理数据 浏览器请求
# 3.1 得到请求的路径
# 3.2 根据不同的路径返回不同的数据
# 4.关闭

# 一个函数一个功能
# 类是相关函数的集合,封装

import re
import socket

import time

import mini_web_01

import gevent
from  gevent import monkey

# 打补丁
monkey.patch_all()


class WebServer(object):
    def client_exec(self, client):
        """处理用户的请求"""
        # 1.得到浏览器的请求头

        request_data = client.recv(1024).decode("utf-8")
        print("请求的数据:", request_data)
        # GET /index.html HTTP/1.1
        # GET / HTTP/1.1
        # 2. 得到路径,通过正则
        result = re.match('[^/]+(/[^ ]*) ', request_data)
        # 判断当前的路径是否可以被解析
        if result:
            # 说明匹配到了
            # 得到路径
            file_path = result.group(1)
        else:
            # 没有匹配到
            client.close()
            return

        # 到这个位置一定有一个地址
        print("地址:", file_path)

        # 根据资源的特性,可或者不变,html是变的,其他一些资源是不变比例 jpg,png,mp4,mp3,avi
        # 可变我们动态的使用代码发送
        # 不可变的,那我们直接打开返回
        # 根据不同的内容返回不同的响应体
        if file_path.endswith(".html"):

            # 通过mini_web中的application方法返回数据
            head_stauts, body = mini_web_01.application(file_path)

            # 发送的格式
            content = head_stauts + "\r\n" + body
            # 发送数据
            client.send(content.encode("utf-8"))

        else:
            # 如果当前的不变的资源找不到我们的处理
            try:
                # 直接 打开返回
                with open("./static%s" % file_path, 'rb')  as f:
                    body = f.read()

                # 发送响应头
                client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf-8"))
                # 发送响应体
                client.send(body)
            except Exception as e:
                head = "HTTP/1.1 404 not found\r\n"
                body = ""
                content = head + "\r\n" + body

                # 发送数据
                client.send(content.encode("utf-8"))

        # 4.关闭
        client.close()

    def run_server(self):
        # 启动服务,循环去接收用户的请求
        while True:
            client, address = self.tcp_server.accept()
            # 处理请求
            # 一个函数一个功能
            # 把函数处理的加入到我们的协程中
            gevent.spawn(self.client_exec, client)
        # self.client_exec(client)

        # 关闭服务器端
        tcp_server.close()

    def __init__(self):
        """这个初始化tcp"""
        # 1.创建套接字
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.绑定端口与复用端口
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_server.bind(("", 8686))
        # 3.被动模式
        self.tcp_server.listen(128)


# 入口函数或者main或者主函数读起来像目录
def main():
    """创建一个http服务器"""
    # 初始化
    server = WebServer()

    # 开启服务
    server.run_server()


if __name__ == '__main__':
    main()

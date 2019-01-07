import threading

# 定义全局变量
g_num = 0

# 循环1000000次每次给全局变量加1
def sum_num1():
    for i in range(1000000):
        global g_num
        g_num += 1

    print("sum1:", g_num)

# 循环1000000次每次给全局变量加1
def sum_num2():
    for i in range(1000000):
        global g_num
        g_num += 1
    print("sum2:", g_num)

if __name__ == '__main__':
    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)

    # 启动线程
    first_thread.start()
    # 主线程等待第一个线程执行完成以后代码再继续执行，让其执行第二个线程
    # 线程同步： 一个任务执行完成以后另外一个任务才能执行，同一个时刻只有一个任务在执行
    first_thread.join()
    # 启动线程
    second_thread.start()
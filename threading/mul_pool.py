# 进程池同步执行任务
import multiprocessing
import time

# 拷贝任务
def work():
    print('复制中...', multiprocessing.current_process().pid)
    time.sleep(0.5)

if __name__ == '__main__':
    # 创建进程池
    # 进程池中进程的最大个数
    pool = multiprocessing.Pool(3)
    # 模拟最大批量的任务,让进程池中去执行
    for i in range(5):
        # 循环让进程池执行对应的work任务
        # 同步执行任务,一个任务执行完成以后另外一个任务才能执行
        pool.apply(work)
# 导入库
# 请猴子打补丁
# 把任务 加入到gevent
# 把任务加入等待列表中
import time
import gevent

from gevent import monkey
monkey.patch_all()

def song():
    while True:
        print('唱歌')
        time.sleep(1)

def dance():
    while True:
        print('跳舞')
        time.sleep(1)

def main():
    '''一边唱歌一边跳舞'''
    # 等待的列表
    gevent_list = list()

    # 执行任务并加入到等待列表中
    gevent_list.append(gevent.spawn(dance))
    gevent_list.append(gevent.spawn(song))
    # 等待
    gevent.joinall(gevent_list)

if __name__ == '__main__':
    main()


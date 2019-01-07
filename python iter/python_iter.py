# 迭代器对象必须实现2个方法 __iter__,__next__
# 迭代器可以使用for循环遍历
import threading
import time

class MyIter(object):
    def __init__(self):
        # 定义一个初始化的值
        print('__init__')
        self.value = 0

    def __iter__(self):
        # 返回迭代器对象
        # 自定义迭代器返回都是固定的
        print('haha')
        return self

    def __next__(self):
        if self.value > 10:
            raise StopIteration
        self.value += 1
        print('lolo')
        return self.value

# 判断是否是可迭代器的对象
class iter_isinstance(object):
    def iter_stance(self):
        from collections import Iterable
        a = [1, 2, 3, 4, 5, 6]
        for temp in a :
            print(temp)
        # isinstance()用来判断 是否是这个类型的
        print(isinstance(a, Iterable))

        b = (1, 2, 3, 4, 5, 56, 6)
        print(isinstance(b, Iterable))

        c = 123
        print(isinstance(c, Iterable)) # int 不是可迭代的对象

# 生成器第一种方式
class iter_generator(object):
    def fun1(self):
        # 生成器一种特殊的迭代器,特殊在于他的创建方式
        a = [x for x in range(10)]
        print(a)

        for temp in a:
            print(temp)
        # 只要把[]改成(那么就是生成器了)
        b = (x for x in range(10))
        print(b)

        for temp in b:
            print(temp)

# 生成器第二种方式
class iter_generator2(object):
    def fun2(self):
        for temp in range(10):
            yield temp
    def fun3(self):
        print(self.fun2())
        test_iter = iter(self.fun2())

        print(next(test_iter))
        print(next(test_iter))
        print(next(test_iter))

# 线程之间的守护问题
# 测试主线程是否会等待子线程执行完成以后程序再退出
def show_info():
    for i in range(5):
        print('test:', i)
        time.sleep(0.5)

if __name__ == '__main__':
    # # 创建迭代器对象
    # my_iter = MyIter()
    #
    # # 使用for循环
    # for temp in my_iter:
    #     print(temp)

    # iter1 = iter_isinstance()
    # iter1.iter_stance()

    # new_generator1 = iter_generator()
    # new_generator1.fun1()

    # new_generator2 = iter_generator2()
    # new_generator2.fun3()

    # sub_thread = threading.Thread(target=show_info)
    # sub_thread.setDaemon(True) # 守护主线程, 主线程结束子线程结束
    # sub_thread.start()
    # # 主线程延时1秒
    # time.sleep(2)
    # print('over')
    pass

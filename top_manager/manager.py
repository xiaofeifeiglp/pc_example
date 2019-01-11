# __exit_和__enter__这2个方法实现这个类就是上下文管理器
# 实现上下文管理器就可以使用with
class MyOpen(object):
    def __init__(self):
        print('初始化')

    # 返回F的值
    def __enter__(self):
        print('__enter')
        return 100

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit')


if __name__ == '__main__':
    with MyOpen() as f:
        print(f)
    print('退出了')
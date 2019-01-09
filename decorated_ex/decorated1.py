def set_fun(fun):
    def call_fun():
        print('添加额外的功能')
        print(fun)
        fun()
    return call_fun


@set_fun  # fun = set_fun(fun)
def fun():
    print('test_python')


# 万能装饰器
def set_fun1(fun1):
    def call_fun1(*args, **kwargs):
        print('添加功能')
        return fun1(*args, **kwargs)
    return call_fun1


@set_fun  # fun1 = set_fun(fun1)
def fun1(*args, **kwargs):
    print('万能装饰器')


if __name__ == '__main__':
    # fun()

    fun1()

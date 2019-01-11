import timeit


def funca():
    '''
    计算多次运行的时间
            tm = timeit.Timer("funca()", "from __main__ import funca")
            （待测语句，前置条件（函数导入））
            print(tm.timeit(10000))
            （总时间）
    :return:
    '''
    print("hello")

tm = timeit.Timer("funca()", "from __main__ import funca")
print(tm.timeit(10000))




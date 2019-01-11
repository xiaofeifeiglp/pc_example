import timeit


def f1():
    l = []
    for i in range(1000):
        l = l + [i]


def f2():
    l = []
    for i in range(1000):
        l.append(i)


def f3():
    l = [i for i in range(1000)]


def f4():
    l = list(range(1000))

tm1 = timeit.Timer('f1()', 'from __main__ import f1')
tm2 = timeit.Timer('f2()', 'from __main__ import f2')
tm3 = timeit.Timer('f3()', 'from __main__ import f3')
tm4 = timeit.Timer('f4()', 'from __main__ import f4')

print('f1 tasks {}s'.format(tm1.timeit(100)))
print('f2 takes {}s'.format(tm2.timeit(100)))
print('f3 takes {}s'.format(tm3.timeit(100)))
print('f4 takes {}s'.format(tm4.timeit(100)))
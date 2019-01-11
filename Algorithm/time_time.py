import time


class main(object):
    def fun1(self):
        strart = time.time()
        for a in range(101):
            for b in range(101):
                for c in range(101):
                    if a+b+c == 1000 and a**2+b**2 == c**2:
                        print('a={} b={} c={}'.format(a, b, c))
        end = time.time()
        print(end-strart)

if __name__ == '__main__':
    time1 = main()
    time1.fun1()

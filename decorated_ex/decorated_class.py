# 用装饰器实现单例
def singleton(MyClass):
    print(MyClass)
    instance = {}

    def getinstance():
        if MyClass not in instance:
            instance[MyClass] = MyClass()
        return instance[MyClass]
    return getinstance


@singleton  # MyClass=singleton(MyClass)
class MyClass():
    a = 1

c1 = MyClass()
c2 = MyClass()
print(c1)
print(c2)
print(c1 == c2)
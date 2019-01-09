class Person(object):
    '''单例模式'''
    instance = None  # 记录创建的对象

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:  # 只有当instance 没有值的时候才创建新对象
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name


class Person1(object):
    '''单例模式的完善'''
    instance = None  # 记录创建的对象
    is_first_run = True  # 如果为True则表示是第一次创建对象

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:  # 只有当instance没有值的时候才创建新对象
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, name=''):
        if Person1.is_first_run:
            self.name = name  # 只有第一次创建对象，才需要初始化属性
            Person1.is_first_run = False

    def set_name(self, new_name):  # 要修改单例模式的属性，可以使用set方法
        self.name = new_name

if __name__ == '__main__':
    # zs = Person('张三')
    # ls = Person('李四')
    # print(zs)
    # print(ls)

    zs = Person1('张三')
    print(zs.name)
    ls = Person1()
    print(ls.name)
    ls.set_name('李四')
    print(zs.name)

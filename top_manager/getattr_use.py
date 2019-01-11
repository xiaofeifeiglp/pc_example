# getattr()函数用于返回一个对象属性值

class A(object):
    bar = 1

a = A()
print(getattr(a, 'bar'))
# print(getattr(a, 'bar2')) 属性2不存在，会报错
print(getattr(a, 'bar2', 3))  # 属性bar2不存在,但设置了默认值
print(getattr(a, 'bar', 3))  # 属性bar2不存在,但设置了默认值
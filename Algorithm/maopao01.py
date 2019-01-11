# 冒泡的时间复杂度o(N^2)
# 每次比较2个相邻的元素，如果他们的顺序错误就把他们交换位置
def bull(a):
    '''从小到大'''
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def bull1(a):
    '''从大到小'''
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return  a
a = [5, 2, 45, 6, 8, 2, 1]
print(bull(a))
print(bull1(a))



# 缺点：冒泡排序解决了桶排序空间的问题，但是冒泡排序的效率特别低
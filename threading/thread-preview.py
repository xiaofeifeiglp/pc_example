#设计实现遍历目录与子目录,抓取.pyc 文件
import os

def getFiles(dir, suffix):

    res = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))

    print(res)

getFiles("./", '.py')


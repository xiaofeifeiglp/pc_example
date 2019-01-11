# 根据不同的路径返回不同的网页
# 让我们的入口函数读起来像目录
# 一个功能一个函数
import re

from pymysql import connect

# 定义一个空的字典
url_dict = dict()


# flask核心功能 就是路由功能
# 路由功能 完成
# 路由功能的功能就是用来控制当前的网页是否展示
def set_url(url):
    def set_fun(func):
        def call_fun(*args, **kwargs):
            print("添加权限")
            return func(*args, **kwargs)

        print(call_fun)  # 函数的引用
        print(url)  # 函数对应的地址

        # 添加到我们的字典中
        url_dict[url] = call_fun

        return call_fun

    return set_fun


# 如果if超过三个以上,我们可以考虑使用字典

def application(file_path):
    # 响应头
    head_stauts = "HTTP/1.1 200 OK\r\n"

    # 定义一个url的字典
    # url_dict = {"/index.html": index, "/center.html": center, "/login.html": login}

    print("自动生成的字典:", url_dict)
    try:
        # 根据不同的地址去字典获取相应的函数引用
        fun = url_dict[file_path]
        # 得到相应体
        body = fun()

    except Exception as e:
        print("异常:", e)
        head_stauts = "HTTP/1.1 404 not found\r\n"
        body = "not page is show"

    return head_stauts, body


################################################################上面全是框架的代码#################################


# 展示首页
@set_url('/index.html')
def index():
    return 'index page is show'

# # 展示一个首页
# # 一个页面定义一个函数
#
# @set_url('/index.html')
# def index():
# 	# 展示 前端的界面
# 	# 1.1 打开前端的代码
# 	# 1.2 读取代码
#
# 	with open("./templates/index.html",'r') as f:
# 		content = f.read()
#
# 	# 一行的字符串
# 	row_str = """
# 	<tr>
#         <td>%s</td>
#         <td>%s</td>
#         <td>%s</td>
#         <td>%s</td>
#         <td>%s</td>
#         <td>%s</td>
#         <td>%s</td>
#         <td>%s</td>
#         <td>
#             <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
#         </td>
#         </tr>
# 	"""
#
# 	# 数据库有多少数据,我们拼接多少条数据
# 	# 1. 从数据库得到数据
# 	# 1.1连接数据库
# 	# 创建Connection连接
# 	conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
# 	# 获得Cursor对象
# 	cs1 = conn.cursor()
#
# 	# 1.2 执行查询的sql语句
# 	cs1.execute("select * from info;")
# 	# 得到数据库的数据
# 	data = cs1.fetchall()
#
# 	# 1.3 关闭
# 	cs1.close()
# 	conn.close()
#
# 	# 有多少数据进行拼接
# 	table_str = "" # 最终的字符串
# 	for temp in data:
# 		table_str += row_str%(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])
#
# 	# 替换前端给的标志
# 	content_new = re.sub(r'\{%content%\}', table_str, content)
#
# 	return content_new

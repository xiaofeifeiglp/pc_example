import base64
import os
from _curses import flash

from flask import Flask, render_template, make_response, session
from flask import redirect
from flask import request
from flask import url_for


app = Flask(__name__)
app.secret_key = "test"


# 登录页面路由
@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        # 获取表单中提交的参数
        username = request.form.get("username")
        password = request.form.get("password")
        # 验证账号密码
        if username == 'laowang' and password == '1234':
            # 状态保持，session中记录用户名
            session['username'] = username
            session.permanent = True
            # 登录成功,跳转到转账页面
            return redirect(url_for('transfer'))
        else:
            print('密码错误')
    return render_template('temp_login.html')


# 转账页面路由
@app.route('/transfer', methods=["POST", "GET"])
def transfer():
    # 从session中取到用户名
    username = session.get('username')
    # 如果没有取到，代表没有登录
    if not username:
        return redirect(url_for('index'))

    if request.method == "POST":
        # 获取表单数据
        to_account = request.form.get("to_account")
        money = request.form.get("money")
        return '转账 %s 元到 %s 成功' % (money, to_account)

    return render_template("temp_transfer.html")


if __name__ == '__main__':
    app.run(debug=True, port=9000)

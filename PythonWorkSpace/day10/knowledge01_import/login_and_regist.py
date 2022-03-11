"""
--------------------------------
@Time    :  2022/1/24 - 10:55 
@Author  :  Lee
@File    :  login_and_regist 
--------------------------------
"""

# 模拟数据库数据,假设数据只有如下数据
user = {"username": "xiaohua", "password": "a123456"}


# 注册功能
def register(username, password, re_password):
    if len(username) == 0:
        return {"code": 1001, "msg": "用户名不能为空"}
    elif username == user.get('username'):
        return {"code": 1002, "msg": "用户名已注册"}
    elif len(password) == 0:
        return {"code": 1003, "msg": "密码不能为空"}
    elif password != re_password:
        return {"code": 1004, "msg": "两次密码输入不一致"}
    elif not (6 <= len(username) <= 18 and 6 <= len(password) <= 18):
        return {"code": 1005, "msg": "用户名和密码必须在6-18位之间"}
    else:
        return {"code": 9999, "msg": "注册成功"}


# 登录功能
def login(username, password):
    if len(username) == 0:
        return {"code": 1001, "msg": "用户名不能为空"}
    elif len(password) == 0:
        return {"code": 1002, "msg": "密码不能为空"}
    elif username == user['username'] and password == user.get('password'):
        return {"code": 9999, "msg": "登录成功"}
    else:
        return {"code": 1003, "msg": "用户名或密码错误"}


if __name__ == '__main__':  # 判断是否在当前模块下运行代码(__name__在当前模块下值:__main__,在其他模块下值:day10.knowledge01_import.login_and_regist)
    print(register('xiaohua', '123456', '123456'))  # {'code': 1002, 'msg': '用户名已注册'}
    print(__name__)  # __main__

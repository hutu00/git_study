"""
-------------------------------------------------
   File Name:python_basic88
   Author:Lee
   date: 2021/9/17-9:37
-------------------------------------------------
"""


# ********************练习1,华丽的分隔符4*****************************************************************

# 将以前的登录注册封装为一个类，并且进行调用
class UserOpt:
    user = {"username": "xiaohua", "password": "a123456"}

    # 注册功能
    def register(self, username, password, re_password):
        if len(username) == 0:
            return {"code": 1001, "msg": "用户名不能为空"}
        elif username == self.user.get('username'):
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
    def login(self, username, password):
        if len(username) == 0:
            return {"code": 1001, "msg": "用户名不能为空"}
        elif len(password) == 0:
            return {"code": 1002, "msg": "密码不能为空"}
        elif username == self.user['username'] and password == self.user.get('password'):
            return {"code": 9999, "msg": "登录成功"}
        else:
            return {"code": 1003, "msg": "用户名或密码错误"}


# 调用
uo = UserOpt()
print(uo.login("xiaohua", "123456"))
print(uo.register("xiaobai", "123456", "123456"))


# ********************练习2,华丽的分隔符4*****************************************************************

# 创建一个类名为Tb_User,并且声明__init__方法,入参为数据库字段名。
# 创建两个对象，将两行内容转为对象保存。
class Tb_User:
    def __init__(self, name, password, phone):
        self.name = name
        self.password = password
        self.phone = phone


user1 = Tb_User('AutoTrue', 'AutoTrue', 15821111149)
user2 = Tb_User("test036", '1234567', 15821111146)

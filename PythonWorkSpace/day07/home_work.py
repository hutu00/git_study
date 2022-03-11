"""
-------------------------------------------------
   File Name:python_basic88
   Author:Lee
   date: 2021/9/17-9:37
-------------------------------------------------
"""
# 1、将title和case1转换成列表，并且进行打包为一个字典，并且获取到 username对应的值。提示要使用到zip和eval
title = "['case_id', 'case_title', 'interface', 'url', 'case_data', 'expect']"
case1 = """['1', '正常流程', 'user_login', 'http://127.0.0.1:5000/user_login',
         '{"username": "xiaoniu", "password": "a123456"}',
         "{'code': 9999, 'msg': '登录成功'}"]"""

a = dict(zip(eval(title), eval(case1)))
print(eval(a["case_data"])["username"])


# ********************练习1,华丽的分隔符*****************************************************************

# 2、如下函数写出打印的内容

def tx1(*args):
    print(type(args))  # 打印出多少,为什么？   tuple
    print(args[2])  # 打印出多少,为什么？   3
    print(sum(args))  # 打印出多少,为什么？  6


tx1(1, 2, 3)


# ********************练习3,华丽的分隔符*****************************************************************

# 3、 写代码调用 tx2方法，并且传入 k1=2, k2=3, k3=3 三对数据，打印出返回的结果

def tx2(**kwargs):
    print(type(kwargs))  # 打印出什么内容,为什么？
    # 添加代码返回所有value值的和
    return sum(kwargs.values())


print(tx2(k1=2, k2=3, k3=3))


# ********************练习4,华丽的分隔符*****************************************************************


# 4、 写代码调用函数

def tx3(args1, args2=None):
    if args2 is None:
        return '调用该方法时只传入了一个值,值为{}'.format(args1)
    else:
        return '调用该方法时只传入了两个值,值为{}和{}'.format(args1, args2)


result1 = tx3(1)
result2 = tx3(1, 2)

print(tx3(10))
print(tx3(10, 20))
# ********************练习5,华丽的分隔符4*****************************************************************


# 5、看懂以下两个功能, 多次调用这两个函数,并且得到每个分支的结果。


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

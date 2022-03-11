"""
--------------------------------
@Time    :  2022/2/23 - 15:30
@Author  :  Lee
@File    :  python_senior014
--------------------------------
"""

"""
不使用框架进行测试,我们也可以测试,但比较麻烦
"""

import requests

# 1.正确流程
response = requests.post(url="http://127.0.0.1:5000/user_login",
                         data={"username": "xiaohua",
                               "password": "a123456"})
res = response.json()
print(res)  # {'code': 9999, 'msg': '登录成功'}

# 2.用户名错误
response = requests.post(url="http://127.0.0.1:5000/user_login",
                         data={"username": "xiaohuahua",
                               "password": "a123456"})
res = response.json()
print(res)  # {'code': 1003, 'msg': '用户名或密码错误'}

# 3.用户名为空
response = requests.post(url="http://127.0.0.1:5000/user_login",
                         data={"username": "",
                               "password": "a123456"})
res = response.json()
print(res)  # {'code': 1001, 'msg': '用户名不能为空'}

# 4.密码错误
response = requests.post(url="http://127.0.0.1:5000/user_login",
                         data={"username": "xiaohua",
                               "password": "a1234567"})
res = response.json()
print(res)  # {'code': 1003, 'msg': '用户名或密码错误'}

# 5.密码为空
response = requests.post(url="http://127.0.0.1:5000/user_login",
                         data={"username": "xiaohua",
                               "password": ""})
res = response.json()
print(res)  # {'code': 1002, 'msg': '密码不能为空'}

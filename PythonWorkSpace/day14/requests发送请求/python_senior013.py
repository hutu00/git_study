"""
--------------------------------
@Time    :  2022/2/23 - 14:50
@Author  :  Lee
@File    :  python_senior013
--------------------------------
"""
import requests

"""
requests 模拟接口之间的关联
"""

# 1.先进行登录
response = requests.post(url="http://127.0.0.1:6666/business/token_login",
                         data={"username": "xiaohua",
                               "password": "a123456",
                               "typeId": "101"})
res = response.json()  # 获取json格式的响应体
print(res)
print(type(res))  # <class 'dict'>
tk = res["token"]
print(tk)

# 2.再调用商品信息查询接口
response = requests.post(url="http://127.0.0.1:6666/business/token_goodsInfo",
                         data={"token": tk,
                               "goodsId": "",
                               "isOnSale": "",
                               "isPromote": ""})
res = response.json()
print(res)

response = requests.get(url="http://127.0.0.1:6666/business/token_goodsInfo?token={}&goodsId=&isOnSale=&isPromote=".format(tk))
res = response.json()
print(res)


"""
--------------------------------
@Time    :  2022/2/23 - 14:42
@Author  :  Lee
@File    :  python_senior012
--------------------------------
"""
import json

import requests

"""
requests模拟json请求(请求体数据为json格式)
"""

# 发送json格式的请求需要三个入参
# 1.url
# 2.json格式的请求体(使用json.dumps(字典)把字典类型转换为json)
# 3.必须添加请求头信息: "Content-Type":"application/json",声明请求体数据的内容是json格式

response = requests.post(url="http://127.0.0.1:6666/business/regist_json",
                         data=json.dumps({"username": "xiaomei",
                                          "password": "a123456",
                                          "re_password": "a123456",
                                          "phone": "18656561234",
                                          "sex": "男",
                                          "birthday": "",
                                          "qq": "",
                                          "email": "456@163.com"
                                          }),
                         headers={"Content-Type": "application/json"})
res = response.content.decode('utf-8')
print(res)

"""
--------------------------------
@Time    :  2022/2/23 - 11:32
@Author  :  Lee
@File    :  python_senior011
--------------------------------
"""

"""
requests 用来模拟http请求
为什么要学习requests库: 因为我们要脱离工具的测试,改成使用代码调用接口测试

使用步骤: 
1.pip install requests
2.导包  import requests
3.使用requests模拟请求
"""
import requests

# 发送get请求
response = requests.get(url='http://www.baidu.com')
# res = response.text  # 获取响应体方式1
res = response.content.decode('utf-8')  # 获取响应体方式2
print(res)

# 案例:通过requests库调用我们自己的接口
response = requests.get(url="http://127.0.0.1:5000/user_login?username=xiaohua&password=a123456")
res = response.content.decode('utf-8')  # 获取响应体方式2
print(res)

# 发送post请求
# 注意:发送post请求,请求数据在请求体中,所以需要传入一个字典,存放请求数据
response = requests.post(url="http://127.0.0.1:5000/user_login",
                         data={"username": "xiaoniu", "password": "a123456"})
res = response.content.decode('utf-8')  # 获取响应体方式2
print(res)  # {"code": 9999, "msg": "登录成功"}

"""
--------------------------------
@Time    :  2022/1/24 - 14:14 
@Author  :  Lee
@File    :  python_basic45 
--------------------------------
"""
from day10.knowledge01_import.login_and_regist import login, register, user

"""
模块导入方式2: 导入某个模块下的部分内容,这种方式用什么,拿什么
格式:from 包名.模块名 import 函数名1,函数名2,变量1...
"""

res = login('xiaohua', 'a123456')
print(res)  # {'code': 9999, 'msg': '登录成功'}
print(user)  # {'username': 'xiaohua', 'password': 'a123456'}



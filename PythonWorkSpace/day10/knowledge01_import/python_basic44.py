"""
--------------------------------
@Time    :  2022/1/24 - 10:58 
@Author  :  Lee
@File    :  python_basic44 
--------------------------------
"""

import day10.knowledge01_import.login_and_regist as lr

"""
模块导入:当前模块导入其他模块的内容,我们就可以使用该模块的变量或函数,类

模块导入方式1:
导入整个模块格式: import 包名.模块名 as 别名 
"""

print(lr.user)  # {'username': 'xiaohua', 'password': 'a123456'}
print(lr.login('xiaohua', '1234'))  # {'code': 1003, 'msg': '用户名或密码错误'}
print(lr.register('xiaomei', '123456', '123456'))  # {'code': 9999, 'msg': '注册成功'}

print(lr.__name__)  # day10.knowledge01_import.login_and_regist
print(__name__)  # __main__

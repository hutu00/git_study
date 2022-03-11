"""
--------------------------------
@Time    :  2022/2/25 - 14:16
@Author  :  Lee
@File    :  excel_test01
--------------------------------
"""


# 复习
# 设计一个类,可以将字典转换为对象
class CaseDate:
    def __init__(self, dict_case):
        for i in dict_case.items():  # {"username":"xiaohua","password":"a123456"}  items[(username,xiaohua),(password,a123456)]
            setattr(self, i[0], i[1])  # 动态的为对象赋值


# 将如下两个列表打包为字典,并且转换为对象
title = ["case_data", "exp"]
case = ["{'username':'xiaohua','password':'a123456'}", "{'code':9999,'msg':'登录成功'}"]

dict1 = dict(zip(title, case))

cd = CaseDate(dict1)

# 打印出转换为对象的case_data的属性值
print(cd.case_data)  # {'username':'xiaohua','password':'a123456'}

# 将多个字典的列表转换为对象,并且存放在一个空列表datas中
cases = [{"case_data": '{"username": "xiaohua", "password": "a123456"}', "exp": "{'code': 9999, 'msg': '登录成功'}"},
         {"case_data": '{"username": "xiaohuahua","password": "a123456"}',
          "exp": "{'code': 1003, 'msg': '用户名或密码错误'}"},
         {"case_data": '{"username": "", "password": "a123456"}', "exp": "{'code': 1001, 'msg': '用户名不能为空'}"},
         {"case_data": '{"username": "xiaohua", "password": "a1234567"}',
          "exp": "{'code': 1003, 'msg': '用户名或密码错误'}"},
         {"case_data": '{"username": "xiaohua", "password": ""}', "exp": "{'code': 1002, 'msg': '密码不能为空'}"}]
datas = []

for i in cases:
    cd = CaseDate(i)
    datas.append(cd)

print(datas[0].case_data)  # {"username": "xiaohua", "password": "a123456"}


# 被@classmethod装饰的方法,可以通过 类名.方法名() 直接调用
class A:
    @classmethod
    def test(cls, a, b):
        print(a + b)


A.test(1, 2)

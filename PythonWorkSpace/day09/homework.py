"""
-------------------------------------------------
   File Name:python_basic75
   Author:Lee
   date: 2021/9/15-17:18
   综合练习：自动化组件
-------------------------------------------------
"""


# 1、设计一个类，可以将字典转换为对象
class Stu(object):
    def __init__(self, dict1):
        for i in dict1.items():
            setattr(self, i[0], i[1])


# 2、将如下两个列表打包为字典,并且转换为对象
title = ['case_data', 'exp']
case = ['{"username": "xiaoniu", "password": "a123456"}', "{'code': 9999, 'msg': '登录成功'}"]

stu = Stu(dict(zip(title, case)))

# 3、打印出转换为对象的 case_data的属性值
print(stu.case_data, stu.exp)

# 4、将多个字典的列表通过转换为对象，并且存放在一个空列表datas中,提示：使用循环
datas = []
cases = [{"case_data": '{"username": "xiaoniu", "password": "a123456"}', "exp": "{'code': 9999, 'msg': '登录成功'}"},
         {"case_data": '{"username": "xiaoniu1", "password": "a123456"}', "exp": "{'code': 1003, 'msg': '用户名或密码错误'}"},
         {"case_data": '{"username": "", "password": "a123456"}', "exp": "{'code': 1001, 'msg': '用户名不能为空'}"},
         {"case_data": '{"username": "xiaoniu", "password": "a1234567"}', "exp": "{'code': 1003, 'msg': '用户名或密码错误'}"},
         {"case_data": '{"username": "xiaoniu", "password": ""}', "exp": "{'code': 1002, 'msg': '密码不能为空'}"},
         'dasnhdkjan']

# for i in cases:
#     stu = Stu(i)
#     datas.append(stu)
#
# for i in datas:
#     print(i.case_data, i.exp)

# 5、对该程序进行 异常处理，如果出异常打印出异常日志和提示 转换失败。
try:
    for i in cases:
        stu = Stu(i)
        datas.append(stu)

    for i in datas:
        print(i.case_data, i.exp)
except Exception as e:
    print("数据异常,请联系管理员处理!", e)

"""
--------------------------------
@Time    :  2022/2/24 - 10:50
@Author  :  Lee
@File    :  test_pytest02
--------------------------------
"""
import pytest
import requests

"""
1. -m 标记,我们为测试用例添加标记,并且指定运行某个标记,可以加在方法和类上
2. 需要在当前目录下创建pytest.ini 文件,并且添加标记到ini文件中
    常用的pytest.ini文件修改pytest的默认行为:
    1.addopts = -vs  : addopts参数可以更改默认命令行选项
    2.marks = test01 : 注册标记选项,注册之后就可以使用装饰器@pytest.mark.xxx装饰类或函数
    3.修改或者添加pytest的用例收集规则
    python_files = test_* *_test : 测试文件以test_ 开头(以_test结尾也可以)
    python_classes = Test* : 测试类以Test开头,并且不能有__init__方法
    python_functions = test_* : 测试用例/测试函数以test_开头

"""


class TestLogin:

    # 1.正确流程
    @pytest.mark.test01
    def test_login01(self):
        print('hello')
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "xiaohua",
                                       "password": "a123456"})
        res = response.json()
        assert {'code': 9999, 'msg': '登录成功'} == res

    # 2.用户名错误
    @pytest.mark.test02
    @pytest.mark.skip(reason='开发bug未修复,下个版本上线')
    def test_login02(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "xiaohuahua",
                                       "password": "a123456"})
        res = response.json()
        assert {'code': 1003, 'msg': '用户名或密码错误'} == res

    # 3.用户名为空
    @pytest.mark.run(order=2)
    @pytest.mark.test02
    def test_login03(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "",
                                       "password": "a123456"})
        res = response.json()
        assert {'code': 1001, 'msg': '用户名不能为空'} == res

    # 4.密码错误
    @pytest.mark.test03
    def test_login04(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "xiaohua",
                                       "password": "a1234567"})
        res = response.json()
        assert {'code': 1003, 'msg': '用户名或密码错误'} == res

    # 5.密码为空
    @pytest.mark.run(order=1)
    @pytest.mark.test03
    def test_login05(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "xiaohua",
                                       "password": ""})
        res = response.json()
        assert {'code': 1002, 'msg': '密码不能为空'} == res


if __name__ == '__main__':
    # pytest.main(['-vs', '-m test03', './test_pytest02.py'])  # 仅运行当前模块下标记test03的case
    # pytest.main(['-vs', '-m test03 or test02', './test_pytest02.py'])  # 仅运行当前模块下标记test03 或 test02
    # pytest.main(['-m not test03', './test_pytest02.py'])  # 仅运行当前模块下非标记test03
    pytest.main(['-vs', './test_pytest02.py'])

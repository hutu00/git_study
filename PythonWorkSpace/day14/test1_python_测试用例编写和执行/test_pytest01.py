"""
--------------------------------
@Time    :  2022/2/23 - 16:43
@Author  :  Lee
@File    :  test_pytest01
--------------------------------
"""
import requests
import pytest

"""
1.pytest作用: 用来管理和运行测试用例
2.pytest安装: pip install pytest
3.查看是否安装成功: pytest --version
4.测试用例编写规则:
    测试文件以test_ 开头(以_test结尾也可以)
    测试类以Test开头,并且不能有__init__方法
    测试用例/测试函数以test_开头
    断言使用基本的assert即可
5.常用的断言:
    assert A == B 
    assert A > B
    assert A in B 
"""


class TestLogin:

    # 1.正确流程
    def test_login01(self):
        print('hello')
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "xiaohua",
                                       "password": "a123456"})
        res = response.json()
        assert {'code': 9999, 'msg': '登录成功'} == res

    # 2.用户名错误
    def test_login02(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "xiaohuahua",
                                       "password": "a123456"})
        res = response.json()
        assert {'code': 1003, 'msg': '用户名或密码错误'} == res

    # 3.用户名为空
    def test_login03(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "",
                                       "password": "a123456"})
        res = response.json()
        assert {'code': 1001, 'msg': '用户名不能为空'} == res

    # 4.密码错误
    def test_login04(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "xiaohua",
                                       "password": "a1234567"})
        res = response.json()
        assert {'code': 1003, 'msg': '用户名或密码错误'} == res

    # 5.密码为空
    def test_login05(self):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data={"username": "xiaohua",
                                       "password": ""})
        res = response.json()
        assert {'code': 1002, 'msg': '密码不能为空'} == res


# 密码区分大小写
def test_login06():
    response = requests.post(url="http://127.0.0.1:5000/user_login",
                             data={"username": "xiaohua",
                                   "password": "A123456"})
    res = response.json()
    assert {'code': 1003, 'msg': '用户名或密码错误'} == res


if __name__ == '__main__':
    # 知识点1: 运行该模块下的所有测试用例
    # pytest.main(['./test_pytest01.py'])  # 运行指定模块

    # 知识点2: -s -v -q 的应用
    # pytest.main(['-v', './test_pytest01.py'])  # 运行指定模块,-v 详细信息模式,输出更详细的执行用例信息
    # pytest.main(['-q', './test_pytest01.py'])  # 运行指定模块,-q 静默模式,只显示运行结果
    # pytest.main(['-s', './test_pytest01.py'])  # 运行指定模块,-s 显示用例中的打印和日志信息

    # 知识点3:运行模块中的某个类
    pytest.main(['./test_pytest01.py::TestLogin'])  # 运行指定模块下的某个类
    # pytest.main(['-vs', './test_pytest01.py::TestLogin'])  # 运行指定模块,-vs 详细显示用例中的打印和日志信息和运行过程

    # 知识点4:运行模块中的某个用例
    # pytest.main(['-vs', './test_pytest01.py::TestLogin::test_login05'])  # 运行指定用例,-vs 详细显示用例中的打印和日志信息和运行过程

    # 知识点5:运行某个目录下的所有测试用例
    # pytest.main(['./'])  # 运行当前目录下的所有(test_*.py和 *_test.py模块下的所有用例)
    # pytest.main([r'D:\PythonWorkSpace\day14\test1_python_测试用例编写和执行'])  # 运行当前目录下的所有(test_*.py和 *_test.py模块下的所有用例)

    # 知识点6:只运行于给定字符串表达式匹配的测试用例,比如:匹配当前目录下包含login的用例(不区分大小写,匹配目录名、模块名、类名、用例名)
    # pytest.main(["-vs", "-k login", './'])  # 运行当前目录下所有包含 login的用例
    # pytest.main(["-vs", "-k login", './test_pytest01.py::TestLogin'])  # 运行指定类中所有包含 login的用例

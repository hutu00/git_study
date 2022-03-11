"""
--------------------------------
@Time    :  2022/2/24 - 16:35
@Author  :  Lee
@File    :  test_pytest01
--------------------------------
"""

"""
测试固件(测试夹具)
使用固件的三种方式:
    1.@pytest.fixture(autouse=True): 声明固件时设置autouse=True会自动使用固件
    2.在需要使用固件的case参数传入固件函数名即可
    3.使用@pytest.mark.usefixtures("固件名") 装饰器装饰需要使用固件的case

# 固件配置文件:
    python会自动加载当前目录下的conftest.py文件里的自定义的测试固件,一般可以在根目录里定义通用的自定义测试固件
    注意: conftest.py和pytest.ini文件一样都是系统规定的名字
"""

import pytest


class TestFixture:
    def test_case01(self):
        print('开始执行case1~~~')

    def test_case02(self):
        print("开始执行case2~~~")


class TestFixture02:
    def test_case03(self):
        print("开始执行case3~~~")

    def test_case04(self):
        print("开始执行case4~~~")


if __name__ == '__main__':
    pytest.main(["-vs", './test_pytest04.py'])

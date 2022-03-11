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
"""

import pytest


class TestFixture:

    @pytest.fixture(scope='class', autouse=True)  # 在当前模块每个测试方法之前自动执行
    def class_scope(self):
        print("----class前执行----")
        yield
        print('----class后执行----')


    def test_case01(self):
        print('开始执行case1~~~')

    def test_case02(self):
        print("开始执行case2~~~")


if __name__ == '__main__':
    pytest.main(["-vs", './test_pytest02.py'])

"""
--------------------------------
@Time    :  2022/2/24 - 16:35
@Author  :  Lee
@File    :  test_pytest01
--------------------------------
"""

"""
测试固件(测试夹具)
使用固件的四种方式:
    1.@pytest.fixture(autouse=True): 声明固件时设置autouse=True会自动使用固件
    2.在需要使用固件的case参数传入固件函数名即可
    3.使用@pytest.mark.usefixtures("固件名") 装饰器装饰需要使用固件的case
    4.conftest.py配置固件
"""

import pytest


class TestFixture:

    @pytest.fixture(scope='function')  # 在当前模块每个测试方法之前自动执行
    def func_scope(self):
        print("----function前执行----")
        yield
        print('----function后执行----')

    @pytest.fixture(scope='function')  # 在当前模块每个测试方法之前自动执行
    def func_scope11(self, func_scope):
        print("****前****")
        yield
        print('****后****')

    def test_case01(self):  # 使用func_scope固件,会在case执行前执行固件和case执行后执行固件
        print('开始执行case1')

    def test_case02(self):
        print("开始执行case2")


if __name__ == '__main__':
    pytest.main(["-vs", './test_pytest01.py'])

"""
--------------------------------
@Time    :  2022/2/24 - 17:32
@Author  :  Lee
@File    :  conftest
--------------------------------
"""
import pytest


@pytest.fixture(scope='function')  # 在每个测试方法执行前和执行后自动执行
def func_scope():
    print("测试方法执行前执行----")
    yield
    print('测试方法执行后执行----')


@pytest.fixture(scope='class')  # 在每个测试类执行前和执行后自动执行
def class_scope():
    print("--class前--")
    yield
    print('--class后--')


@pytest.fixture(scope='module')  # 在每个测试类执行前和执行后自动执行
def module_scope():
    print("***module前***")
    yield
    print('***module后***')

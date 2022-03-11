"""
--------------------------------
@Time    :  2022/2/24 - 14:19
@Author  :  Lee
@File    :  test_pytest_01
--------------------------------
"""

"""
使用pytest参数化数据,让测试数据和测试逻辑分离
"""

import pytest


def add(a, b):
    return a + b


print(add(1, 2))  # 3

cases = [{"param1": 1, "param2": 2, "exp": 3},
         {"param1": 15, "param2": 25, "exp": 40},
         {"param1": 10, "param2": -20, "exp": -10},
         {"param1": 10, "param2": -10, "exp": 0},
         {"param1": 123, "param2": 234, "exp": 357},
         {"param1": 100, "param2": -50, "exp": 50}]


# @pytest.mark.parametrize(变量名:str,数据源:list)  参数化测试用例,数据源中有多少个成员测试用例执行多少次
@pytest.mark.parametrize('case', cases)
def test_add(case):
    res = add(case["param1"], case["param2"])
    assert case["exp"] == res


if __name__ == '__main__':
    pytest.main(["-vs", './test_pytest_01.py'])

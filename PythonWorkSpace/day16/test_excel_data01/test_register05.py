"""
--------------------------------
@Time    :  2022/2/24 - 14:32
@Author  :  Lee
@File    :  test_pytest_02
--------------------------------
"""

"""
使用pytest参数化数据,让测试数据和测试逻辑分离  自己完成注册接口
"""

import pytest
from excel_utils03 import ReadExcel
import requests


class TestRegister:
    cases = ReadExcel.read_data_all(r'./cases.xlsx', 'user_register')

    @pytest.mark.parametrize('case', cases)
    def test_register(self, case):
        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            assert eval(case.expect) == res
        except AssertionError as e:
            ReadExcel.write_data(r'./cases.xlsx', 'user_register', case.case_id, 7, '失败')
            raise e
        else:
            ReadExcel.write_data(r'./cases.xlsx', 'user_register', case.case_id, 7, '成功')


if __name__ == '__main__':
    pytest.main(["-vs", './test_register.py'])


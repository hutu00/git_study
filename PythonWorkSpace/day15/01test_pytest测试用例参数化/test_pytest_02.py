"""
--------------------------------
@Time    :  2022/2/24 - 14:32
@Author  :  Lee
@File    :  test_pytest_02
--------------------------------
"""

"""
使用pytest参数化数据,让测试数据和测试逻辑分离
"""
import pytest
import requests


class TestLogin:
    cases = [{"case_data": '{"username": "xiaohua", "password": "a123456"}', "exp": "{'code': 9999, 'msg': '登录成功'}"},
             {"case_data": '{"username": "xiaohuahua","password": "a123456"}',
              "exp": "{'code': 1003, 'msg': '用户名或密码错误'}"},
             {"case_data": '{"username": "", "password": "a123456"}', "exp": "{'code': 1001, 'msg': '用户名不能为空'}"},
             {"case_data": '{"username": "xiaohua", "password": "a1234567"}',
              "exp": "{'code': 1003, 'msg': '用户名或密码错误'}"},
             {"case_data": '{"username": "xiaohua", "password": ""}', "exp": "{'code': 1002, 'msg': '密码不能为空'}"}]

    @pytest.mark.parametrize("case", cases)
    def test_login(self, case):
        response = requests.post(url="http://127.0.0.1:5000/user_login",
                                 data=eval(case["case_data"]))
        res = response.json()
        assert eval(case["exp"]) == res


if __name__ == '__main__':
    pytest.main(["-vs", '--html=./report.html', "./test_pytest_02.py"])

"""password
--------------------------------
@Time    :  2022/2/24 - 14:40
@Author  :  Lee
@File    :  test_pytest_03
--------------------------------
"""

"""
对注册接口进行参数化,并且运行测试用例成功
"""

import requests
import pytest


class TestRegister:
    cases = [{"case_data": "{'username':'xiaowu','password':'a123456','re_password':'a123456','email':'789@163.com',"
                           "'phone':'18688995566'}", "exp": '{"code": 9999, "msg": "注册成功"}'},
             {"case_data": "{'username':'','password':'a123456','re_password':'a123456','email':'999@163.com',"
                           "'phone':'18855661122'}", "exp": '{"code": 1001, "msg": "用户名不能为空"}'},
             {"case_data": "{'username':'xiaopu','password':'','re_password':'a123456','email':'9991@163.com',"
                           "'phone':'15655661122'}", "exp": '{"code": 1002, "msg": "密码不能为空"}'},
             {"case_data": "{'username':'xiaojing','password':'a123456','re_password':'a1234567','email':'889@163.com',"
                           "'phone':'17788994455'}", "exp": '{"code": 1003, "msg": "两次密码输入不一致"}'},
             {"case_data": "{'username':'niuniu','password':'a123456','re_password':'a123456','email':'',"
                           "'phone':'16622334455'}", "exp": '{"code": 1005, "msg": "邮箱不能为空"}'},
             {"case_data": "{'username':'huahua','password':'a123456','re_password':'a123456','email':'333@163.com',"
                           "'phone':''}", "exp": '{"code": 1006, "msg": "手机号不能为空"}'}
             ]

    @pytest.mark.parametrize('case', cases)
    def test_register(self, case):
        response = requests.post(url="http://127.0.0.1:5000/register",
                                 data=eval(case["case_data"]))
        res = response.json()
        assert eval(case["exp"]) == res


if __name__ == '__main__':
    pytest.main(["-vs", "./test_pytest_03.py"])

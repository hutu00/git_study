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
from excel_utils03 import ReadExcel


class TestLogin:  # 类名要以Test开头
    cases = ReadExcel.read_data_all(r'./cases.xlsx', 'user_login')  # 读取excel的user_login的sheet页的所有测试用例对象返回列表

    @pytest.mark.parametrize("case", cases)  # 把返回的列表中的成员赋值给case,每赋值一次就执行一次case
    def test_login(self, case):  # 接收case测试用例对象参数
        response = requests.post(url=case.url, data=eval(case.case_data))  # 发起post请求,url和请求体是对象的2个实例属性
        res = response.json()  # 把响应体转换为json格式

        try:
            assert eval(case.expect) == res  # 断言测试用例的预期结果和实际结果是否一致
        except AssertionError as e:
            ReadExcel.write_data(r'./cases.xlsx', 'user_login', case.case_id, 7, '失败')  # 如果断言失败把结果写入excel
            raise e  # 捕捉到断言异常写完excel结果后,要手动抛出断言异常,否则pytest会认为case成功
        else:
            ReadExcel.write_data(r'./cases.xlsx', 'user_login', case.case_id, 7, '成功')  # 如果实际结果符合预期把成功写入excel


if __name__ == '__main__':
    pytest.main(["-vs", "./test_login.py"])

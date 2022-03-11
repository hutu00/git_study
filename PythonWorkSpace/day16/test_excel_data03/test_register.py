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
from excel_utils import ReadExcel
import requests
import allure
from log_utils import logger


@allure.feature("注册模块")  # allure报告的模块分层
class TestRegister:
    cases = ReadExcel.read_data_all(r'./cases.xlsx', 'user_register')

    @allure.severity("critical")  # 为allure报告修改case优先级
    @allure.description("京东小程序入口注册接口")  # 为allure报告添加case描述
    @pytest.mark.parametrize('case', cases)
    def test_register(self, case):
        allure.dynamic.title(case.case_title)  # 动态获取allure报告的case标题
        allure.attach(body=case.url, name='接口路径')  # allure报告显示接口路径
        allure.attach(body=case.case_data, name='接口参数')  # allure报告显示接口参数

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        allure.attach(body=str(res), name='响应结果')  # allure报告显示响应结果

        try:
            assert eval(case.expect) == res
        except AssertionError as e:
            ReadExcel.write_data(r'./cases.xlsx', 'user_register', case.case_id, 7, '失败')
            logger.error("测试编号{},测试用例标题{},执行失败!实际结果是:{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(r'./cases.xlsx', 'user_register', case.case_id, 7, '成功')
            logger.info("测试编号{},测试用例标题{},执行成功!".format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(["-vs", './test_register.py'])

"""
--------------------------------
@Time    :  2022/2/24 - 14:32
@Author  :  Lee
@File    :  test_pytest_02
--------------------------------
"""

import pytest
from comms.excel_utils import ReadExcel
import requests
import allure
from comms.log_utils import logger
from comms.constants import DATA_FILE
from comms.db_utils import DBUtils


@allure.feature("注册模块")
class TestRegister:
    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'user_register')

    @allure.severity("critical")
    @allure.description("京东小程序入口注册接口")
    @pytest.mark.parametrize('case', cases)
    def test_register(self, case):
        allure.dynamic.title(case.case_title)
        allure.attach(body=case.url, name='接口路径')
        allure.attach(body=case.case_data, name='接口参数')

        uname = eval(case.case_data)["username"]
        phone = eval(case.case_data)["phone"]
        # 正确流程
        if case.case_id == 1:
            self.db.cud("delete from tb_user where name = %s or phone = %s;", (uname, phone))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        allure.attach(body=str(res), name='响应结果')

        try:
            assert eval(case.expect) == res
            # 数据验证
            if case.case_id == 1:
                count = self.db.find_count('select * from tb_user where name = %s;', (uname,))
                assert count == 1
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'user_register', case.case_id, 7, '失败')
            logger.error("测试编号{},测试用例标题{},执行失败!实际结果是:{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'user_register', case.case_id, 7, '成功')
            logger.info("测试编号{},测试用例标题{},执行成功!".format(case.case_id, case.case_title))

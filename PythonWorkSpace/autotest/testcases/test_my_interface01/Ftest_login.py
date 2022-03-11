"""
--------------------------------
@Time    :  2022/2/24 - 14:32
@Author  :  Lee
@File    :  test_pytest_02
--------------------------------
"""

import pytest
import requests
from comms.excel_utils import ReadExcel
import allure
from comms.log_utils import logger
from comms.constants import DATA_FILE
from comms.db_utils import DBUtils


@allure.feature("登录模块")
class TestLogin:
    cases = ReadExcel.read_data_all(DATA_FILE, 'user_login')

    @allure.severity("critical")
    @allure.description("京东小程序入口登录接口")
    @pytest.mark.parametrize("case", cases)
    def test_login(self, case):
        allure.dynamic.title(case.case_title)
        allure.attach(body=case.url, name='接口路径')
        allure.attach(body=case.case_data, name='接口参数')

        # 正确流程
        if case.case_id == 1:
            uname = eval(case.case_data)["username"]
            pwd = eval(case.case_data)["password"]
            db = DBUtils()
            db.cud("delete from tb_user where name = %s;", (uname,))
            db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);",
                   (uname, pwd, 'test@163.com', '18656034444'))
            db.close()

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        allure.attach(body=str(res), name='响应结果')

        try:
            assert eval(case.expect) == res
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'user_login', case.case_id, 7, '失败')
            logger.error("测试编号{},测试用例标题{},执行失败!实际结果是:{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            logger.info("测试编号{},测试用例标题{},执行成功!".format(case.case_id, case.case_title))
            ReadExcel.write_data(DATA_FILE, 'user_login', case.case_id, 7, '成功')

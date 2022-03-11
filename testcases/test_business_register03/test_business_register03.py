"""
--------------------------------
@Time    :  2022/3/3 - 11:16
@Author  :  Lee
@File    :  test_business_register01
--------------------------------
"""

import pytest
import requests
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger
from comms.db_utils import DBUtils
import allure

"""
1.主流程
2.数据回滚和数据验证
3.追加其他case和allure报告
"""


@allure.feature("商品注册模块")
class TestRegister:

    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'business_register')

    @allure.severity("critical")
    @allure.description("商品注册模块接口测试用例")
    @pytest.mark.parametrize("case", cases)
    def test_register(self, case):
        allure.dynamic.title(case.case_title)
        allure.attach(body=case.url, name='接口路径')
        allure.attach(body=case.case_data, name='接口参数')

        uname = eval(case.case_data)["username"]
        email = eval(case.case_data)["email"]
        phone = eval(case.case_data)["phone"]
        # 正确流程
        if case.case_id in (1, 3, 13, 28, 31, 36, 38):
            self.db.cud('delete from tb_user where name = %s or email = %s or phone = %s;', (uname, email, phone))
        if case.case_id == 6:  # 用户名已存在的场景
            self.db.cud('delete from tb_user where email = %s or phone = %s;', (email, phone))
        if case.case_id == 27:  # 手机号已存在的场景
            self.db.cud('delete from tb_user where email = %s or name = %s;', (email, uname))
        if case.case_id == 40:
            self.db.cud('delete from tb_user where name = %s or phone = %s;', (uname, phone))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        allure.attach(body=str(res), name='响应结果')

        try:
            assert eval(case.expect) == res
            # 数据验证
            if case.case_id in (1, 3, 13, 28, 31, 36, 38):
                count = self.db.find_count('select * from tb_user where name = %s;', (uname,))
                assert count == 1
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_register', case.case_id, 7, '失败')
            logger.error('测试编号{},测试标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_register', case.case_id, 7, '成功')
            logger.info('测试编号{},测试标题{},执行成功'.format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(['-vs', '--tb=line', './test_business_register03.py'])

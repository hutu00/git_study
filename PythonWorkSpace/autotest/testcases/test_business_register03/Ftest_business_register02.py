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

"""
1.主流程
2.数据回滚和数据验证
"""


class TestRegister:

    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    cases = ReadExcel.read_data_pl(DATA_FILE, 'business_register', 1, 1)

    @pytest.mark.parametrize("case", cases)
    def test_register(self, case):
        uname = eval(case.case_data)["username"]
        email = eval(case.case_data)["email"]
        phone = eval(case.case_data)["phone"]

        # 正确流程
        if case.case_id == 1:
            self.db.cud('delete from tb_user where name = %s or email = %s or phone = %s;', (uname, email, phone))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            assert eval(case.expect) == res
            # 数据验证
            if case.case_id == 1:
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
    pytest.main(['-vs', './Ftest_business_register02.py'])

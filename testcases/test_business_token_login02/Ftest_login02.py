"""
--------------------------------
@Time    :  2022/3/2 - 16:42
@Author  :  Lee
@File    :  test_login01
--------------------------------
"""
import pytest
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
import requests
from comms.log_utils import logger
from comms.db_utils import DBUtils

"""
1.主流程
2.数据回滚和数据验证
"""


class TestLogin:

    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    cases = ReadExcel.read_data_pl(DATA_FILE, 'business_token_login', 1, 1)

    @pytest.mark.parametrize('case', cases)
    def test_login(self, case):

        # 正确流程
        if case.case_id == 1:
            uname = eval(case.case_data)["username"]
            pwd = eval(case.case_data)["password"]
            self.db.cud("delete from tb_user where name = %s;", (uname,))
            self.db.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);",
                        (uname, pwd, 'tester24@163.com', '17788995566'))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            if case.case_id == 1:
                assert case.expect in str(res)
            else:
                assert eval(case.expect) == res
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_login', case.case_id, 7, '失败')
            logger.error("测试编号{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_login', case.case_id, 7, '成功')
            logger.info("测试编号{},测试标题{},执行成功!".format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(['-vs', './test_login02.py'])

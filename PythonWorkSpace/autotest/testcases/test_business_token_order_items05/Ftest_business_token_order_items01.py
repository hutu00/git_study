"""
--------------------------------
@Time    :  2022/3/5 - 14:15
@Author  :  Lee
@File    :  test_business_token_order_items01
--------------------------------
"""

import pytest
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
import requests
from comms.db_utils import DBUtils
from comms.public_api import replace_data, get_token
from comms.log_utils import logger

"""
1.主流程
"""


class TestOrderItems:

    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        one = self.db.find_one("select * from tb_order order by rand();")
        self.orderId = one[0]
        yield
        self.db.close()

    cases = ReadExcel.read_data_pl(DATA_FILE, 'business_token_order_items', 1, 1)

    @pytest.mark.parametrize("case", cases)
    def test_order_items(self, case):
        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        if "#orderId#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'orderId', self.orderId)

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            # 四表连接查询orderId数据,如果查询多条和goods_tiems作比较,如果查询到数据断言响应报文包含查询成功,如果没查询到数据,断言包含查询无结果
            if case.case_id == 1:
                sql = 'select * from tb_user u,tb_order o,tb_order_goods og,tb_goods g where u.userId = o.userId and ' \
                      'o.orderId = og.orderId and og.goodsId = g.goodsId and o.orderId = %s;'
                count = self.db.find_count(sql, (self.orderId,))
                if count > 0:
                    assert '查询成功' in str(res)
                    assert count == len(res["goods_tiems"])
                elif count == 0:
                    assert '查询无结果' in str(res)
            else:
                assert eval(case.expect) == res
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_order_items', case.case_id, 7, '失败')
            logger.error("测试编号{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_order_items', case.case_id, 7, '成功')
            logger.info("测试编号{},测试标题{},执行成功!".format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(['-vs', './Ftest_business_token_order_items01.py'])

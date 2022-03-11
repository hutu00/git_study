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
import allure

"""
1.主流程
2.数据回滚和追加其他case、allure报告
"""


@allure.feature("商品订单查询模块")
class TestOrderItems:

    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        one = self.db.find_one("select * from tb_order order by rand();")
        self.orderId = one[0]
        yield
        self.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'business_token_order_items')

    @allure.severity("normal")
    @allure.description("商品订单查询模块接口测试用例")
    @pytest.mark.parametrize("case", cases)
    def test_order_items(self, case):
        allure.dynamic.title(case.case_title)

        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
            if case.case_id == 3:  # token区分大小写
                case.case_data = replace_data(case.case_data, 'token', get_token().upper())
            if case.case_id == 4:  # token值过期的场景
                token = get_token()
                get_token()
                case.case_data = replace_data(case.case_data, 'token', token)
        if "#orderId#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'orderId', self.orderId)
        if case.case_id == 7:  # orderId不存在的场景
            self.db.cud("delete from tb_order where orderId = %s;", (eval(case.case_data)["orderId"],))

        allure.attach(body=case.url, name='接口路径')
        allure.attach(body=case.case_data, name='请求参数')

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        allure.attach(body=str(res), name='响应参数')

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
    pytest.main(['-vs', './test_business_token_order_items02.py'])

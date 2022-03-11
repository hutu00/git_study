"""
--------------------------------
@Time    :  2022/3/8 - 10:56
@Author  :  Lee
@File    :  test_business_goods_inputs01
--------------------------------
"""
import requests
import pytest
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import get_token, replace_data
from comms.log_utils import logger
from comms.db_utils import DBUtils
import allure

"""
1.主流程
2.数据回滚和数据验证
3.追加其它case和allure报告
"""


@allure.feature("商品模块商品信息录入接口")
class TestGoodsInput(object):
    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'business_token_goods_input')

    @allure.severity("critical")
    @allure.description("商品模块商品信息录入接口测试用例")
    @pytest.mark.parametrize('case', cases)
    def test_goods_input(self, case):
        allure.dynamic.title(case.case_title)
        allure.attach(body=case.url, name="接口路径")

        if case.case_id == 1:
            self.db.cud("delete from tb_goods where goodsName = %s;", (eval(case.case_data)["goodsName"],))
        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        allure.attach(body=case.case_data, name='请求参数')

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        allure.attach(body=str(res), name='响应结果')

        try:
            assert eval(case.expect) == res
            if case.case_id == 1:
                count = self.db.find_count('select * from tb_goods where goodsName = %s;',
                                           (eval(case.case_data)["goodsName"],))
                assert count == 1
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_input', case.case_id, 7, '失败')
            logger.error("测试编号{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_input', case.case_id, 7, '成功')
            logger.info("测试编号{},测试标题{},执行成功!".format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(["-vs", '--tb=line', 'test_business_goods_input03.py'])

"""
--------------------------------
@Time    :  2022/3/8 - 16:35
@Author  :  Lee
@File    :  test_business_goods_promote01
--------------------------------
"""
import pytest
import requests
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token, get_ini_data
from comms.db_utils import DBUtils
from comms.log_utils import logger
import allure

"""
1.主流程
"""


@allure.feature("商品模块促销开启接口")
class TestGoodsPromote:

    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'business_token_goods_promote')

    @allure.severity("normal")
    @allure.description("商品模块促销开启接口测试用例")
    @pytest.mark.parametrize('case', cases)
    def test_goods_promote(self, case):
        allure.dynamic.title(case.case_title)
        allure.attach(body=case.url, name='接口路径')

        one = self.db.find_one(
            'select * from tb_goods where isPromote = 1 and isOnSale = 0 and goodsId != %s order by rand();',
            (get_ini_data('goodsId1', 'goodsId'),))

        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        if "#goodsId#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'goodsId', one[0])
            if case.case_id == 12:  # 商品已开启促销的场景
                one = self.db.find_one(
                    'select * from tb_goods where isPromote = 0 and isOnSale = 0 and goodsId != %s order by rand();',
                    (get_ini_data('goodsId1', 'goodsId'),))
                case.case_data = replace_data(case.case_data, 'goodsId', one[0])
        allure.attach(body=case.case_data, name='请求参数')

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        allure.attach(body=str(res), name='响应结果')

        try:
            assert eval(case.expect) == res
            if case.case_id in (1, 13):  # 验证数据库,断言响应结果已更改完成
                count = self.db.find_count('select * from tb_goods where isPromote = 0 and goodsId = %s;', (one[0],))
                assert count == 1
                # 数据回滚,将数据还原
                self.db.cud("update tb_goods set isPromote = 1 where goodsId = %s;", (one[0],))
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_promote', case.case_id, 7, '失败')
            logger.error("测试编号{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_promote', case.case_id, 7, '成功')
            logger.info("测试编号{},测试标题{},执行成功!".format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(["-vs", "--tb=line", "./test_business_goods_promote03.py"])

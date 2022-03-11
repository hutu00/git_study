"""
--------------------------------
@Time    :  2022/3/9 - 14:15
@Author  :  Lee
@File    :  test_business_goods_delete01
--------------------------------
"""

import requests
import pytest
from comms.excel_utils import ReadExcel
from comms.log_utils import logger
from comms.constants import DATA_FILE
from comms.public_api import get_token, replace_data, get_ini_data
from comms.db_utils import DBUtils
import allure

"""
1.主流程
2.数据回滚和数据验证
3.追加其它case和allure报告
"""


@allure.feature("商品信息删除模块")
class TestGoodsDelete:
    @pytest.fixture(autouse=True)
    def connect_db(self):
        self.db = DBUtils()
        yield
        self.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, 'business_token_goods_delete')

    @allure.severity("critical")
    @allure.description("商品信息删除模块接口测试用例")
    @pytest.mark.parametrize("case", cases)
    def test_goods_delete(self, case):
        allure.dynamic.title(case.case_title)
        allure.attach(body=case.url, name='接口路径')

        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        if "#goodsId#" in case.case_data:
            if case.case_id == 7:
                case.case_data = replace_data(case.case_data, 'goodsId', get_ini_data('goodsId1', 'goodsId'))
            else:
                case.case_data = replace_data(case.case_data, 'goodsId', get_ini_data('goodsId2', 'goodsId'))
        if case.case_id == 1:
            self.db.cud("INSERT INTO `businessdb`.`tb_goods` (`goodsId`, `goodsName`, `goodsTypeId`, `descp`, "
                        "`num`, `onTime`, `offTime`, `shopPrice`, `promotePrice`, `promoteStartTime`, `promoteEndTime`,"
                        " `isOnSale`, `isPromote`, `givePoints`) VALUES (%s, '新冠疫苗', '10004', '一针就见效', "
                        "'99999', '2022-03-09 14:08:30', '2099-12-31', '0.00', '0.00', NULL, NULL, '1', '1', '10');",
                        (get_ini_data('goodsId2', 'goodsId'),))
        allure.attach(body=case.case_data, name='请求参数')

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        allure.attach(body=str(res), name='响应结果')

        try:
            assert eval(case.expect) == res
            if case.case_id == 1:
                count = self.db.find_count('select * from tb_goods where goodsId = %s;',
                                           (get_ini_data('goodsId2', 'goodsId'),))
                assert count == 0
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, "business_token_goods_delete", case.case_id, 7, '失败')
            logger.error('测试编号{},测试标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, "business_token_goods_delete", case.case_id, 7, '成功')
            logger.info('测试编号{},测试标题{},执行成功!'.format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(["-vs", "./test_business_goods_delete03.py"])

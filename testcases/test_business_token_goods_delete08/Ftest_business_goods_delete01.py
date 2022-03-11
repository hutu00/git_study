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

"""
1.主流程
"""


class TestGoodsDelete:
    cases = ReadExcel.read_data_pl(DATA_FILE, 'business_token_goods_delete', 1, 1)

    @pytest.mark.parametrize("case", cases)
    def test_goods_delete(self, case):
        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        if "#goodsId#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'goodsId', get_ini_data('goodsId2', 'goodsId'))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            assert eval(case.expect) == res
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, "business_token_goods_delete", case.case_id, 7, '失败')
            logger.error('测试编号{},测试标题{},执行失败!实际结果{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, "business_token_goods_delete", case.case_id, 7, '成功')
            logger.info('测试编号{},测试标题{},执行成功!'.format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(["-vs", "./Ftest_business_goods_delete01.py"])

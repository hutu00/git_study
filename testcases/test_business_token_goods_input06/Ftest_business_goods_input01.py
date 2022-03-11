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

"""
1.主流程
"""


class TestGoodsInput(object):
    cases = ReadExcel.read_data_pl(DATA_FILE, 'business_token_goods_input', 1, 1)

    @pytest.mark.parametrize('case', cases)
    def test_goods_input(self, case):
        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            assert eval(case.expect) == res
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_input', case.case_id, 7, '失败')
            logger.error("测试编号{},测试标题{},执行失败!实际结果{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_input', case.case_id, 7, '成功')
            logger.info("测试编号{},测试标题{},执行成功!".format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(["-vs", '--tb=line', 'Ftest_business_goods_input01.py'])

"""
--------------------------------
@Time    :  2022/2/24 - 17:55
@Author  :  Lee
@File    :  test_runner
--------------------------------
"""

import pytest, os
from comms.constants import REPORT_JSON, REPORT_HTML, CASE_DIR

if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir', REPORT_JSON, CASE_DIR])
    os.system('allure generate %s -o %s --clean' % (REPORT_JSON, REPORT_HTML))

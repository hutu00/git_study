"""
--------------------------------
@Time    :  2022/2/24 - 17:55
@Author  :  Lee
@File    :  test_runner
--------------------------------
"""

"""
使用allure生成测试报告
    1.https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/  官网下载allure的.zip压缩包
    2.解压到tools目录下 如: D:\Tools\allure-2.17.0 
    3.添加allure的bin目录到环境变量path中
    4.在cmd命令行输入 allure 回车,验证是否安装成功
    5.在cmd命令行输入 pip install allure-pytest 安装pytest框架的allure插件
"""

import pytest, os

if __name__ == '__main__':
    pytest.main(['--alluredir', './report/allure_json', 'test_case.py'])
    os.system('allure generate report/allure_json -o report/allure_report --clean')

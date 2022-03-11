"""
--------------------------------
@Time    :  2022/1/24 - 17:37 
@Author  :  Lee
@File    :  constants 
--------------------------------
"""
import os

"""
使用常量对路径进行管理
好处: 代码使用非绝对路径,可移植性高
"""

path = os.path.dirname(__file__)  # 获取当前文件的目录
# print(path)  # D:/PythonWorkSpace/day10/文件路径管理

# 获取当前文件的父级目录
path = os.path.dirname(os.path.dirname(__file__))
# print(path)  # D:/PythonWorkSpace/day10

# 地址拼接  join
IMPORT_DIR = os.path.join(path, 'knowledge01_import')
# print(IMPORT_DIR)  # D:/PythonWorkSpace/day10\knowledge01_import

CONF_DIR = os.path.join(path, '读取配置文件')
# print(CONF_DIR)
CONF_FILE = os.path.join(CONF_DIR, 'config.ini')

"""
--------------------------------
@Time    :  2022/2/28 - 15:52
@Author  :  Lee
@File    :  logger02
--------------------------------
"""
from log_utils import logger

# 实际意义上的应用

try:
    num = input("请输入除数:")
    res = 20 / int(num)
except Exception as e:
    logger.error("该方法报异常!")  # 记录错误信息到文件
    logger.exception(e)  # 记录报错的堆栈回溯到文件
else:
    logger.info("该方法正常!")  # 记录重要方法运行信息到文件

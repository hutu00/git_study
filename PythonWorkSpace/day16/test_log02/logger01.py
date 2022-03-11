"""
--------------------------------
@Time    :  2022/2/28 - 14:20
@Author  :  Lee
@File    :  logger01
--------------------------------
"""

"""
log/日志:用来记录软件运行的轨迹。我们可以把需要记录的内容记录在文件中,方便以后查看

日志的级别:
debug: 记录详细的信息,主要用来调试
info: 记录正确情况下,重要的日志
warning: 记录告警信息
error: 记录错误信息

"""

# 第一步: 导入logging
import logging

# 第二步:创建日志对象
logger = logging.getLogger()
logger.setLevel("DEBUG")  # 代表获取DEBUG及DEBUG级别以上的内容

# 第三步:设置输出方向
# 日志输出到控制台,级别是INFO及INFO级别以上的内容
sh1 = logging.StreamHandler()
sh1.setLevel("DEBUG")  # 级别是DEBUG及DEBUG级别以上的内容

# 输出 ./info.log文件,并且内容为追加写入,级别是INFO及INFO级别以上的内容
sh2 = logging.FileHandler(filename='./info.log', mode='a', encoding='utf-8')
sh2.setLevel("INFO")  # 级别是INFO及INFO级别以上的内容

# 输出 ./error.log文件,并且内容为追加写入,级别是ERROR及ERROR级别以上的内容
sh3 = logging.FileHandler(filename='./error.log', mode='a', encoding='utf-8')
sh3.setLevel("ERROR")  # 级别是ERROR及ERROR级别以上的内容

# 第四步: 添加输出方向到logger对象
logger.addHandler(sh1)
logger.addHandler(sh2)
logger.addHandler(sh3)

# 第五步: 指定日志输出格式
fmt_str = '%(asctime)s - [%(filename)s - %(lineno)d] - %(levelname)s:%(message)s'
my_fmt = logging.Formatter(fmt_str)  # 设置样式
sh1.setFormatter(my_fmt)
sh2.setFormatter(my_fmt)
sh3.setFormatter(my_fmt)

# 第六步: 如何使用
logger.debug("这是DEBUG级别的日志！")
logger.info("这是INFO级别的日志！")
logger.warning("这是WARNING级别的日志！")
logger.error("这是ERROR级别的日志！")

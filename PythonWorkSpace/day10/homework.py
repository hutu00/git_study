# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2022/1/14-14:31
=============================
"""
import os
from configparser import ConfigParser

# 通过 os模块提供的API,使用常量表达出 config.ini文件的地址
pt = os.path.dirname(__file__)  # 获取当文件的目录
print(pt)
CONF_FILE = os.path.join(pt, '读取配置文件')  #
print(CONF_FILE)


# 封装一个方法，该方法传入ini文件中的 section和option，比如传入 (mysql,user) 得到 root
def get_ini_data(section, option):
    try:
        cnp = ConfigParser()  # 填写核心代码
        cnp.read(r'./读取配置文件/config.ini', encoding='utf-8')
        return cnp.get(section, option)
    except Exception as e:
        print('从ini文件读取测试数据失败!', e)


# 调用该方法

print(get_ini_data('mysql1', 'host'))


# 封装一个方法,传入一个字符串类型的字典，返回替换后的字符串
# 入参为：字符串类型的字典，需要替换的key，value是新的值
# 举例现有字符串：'{"token": "#token#", "goodsId": "100001"}' 我们需要将 token对应的值 #token# 替换为 QEFRJLDFJALSFALCAELK

def replace_data(my_dict, key, value):
    try:
        dict1 = eval(my_dict)  # 先转换字符串为字典类型
        dict1[key] = value
        return str(dict1)
    except Exception as e:  # 如果出现异常，就执行except下的代码
        print('替换数据失败！！')
        print(e)


# 调用该方法

str1 = '{"username":"xiaohua","pwd":"a123456","token":"123456"}'

print(replace_data(str1, "token", "aaaaaa"))

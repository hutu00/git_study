"""
--------------------------------
@Time    :  2022/1/24 - 16:47 
@Author  :  Lee
@File    :  read_properties 
--------------------------------
"""

from configparser import ConfigParser

# 创建一个解析类的对象
cnp = ConfigParser()

# 读取文件
cnp.read(r'config.ini', encoding='utf-8')
# 要传2个参数,第一个参数是文件位置(绝对路径(从根目录开始的路径,比如: D:\Tools)和相对路径(相对于当前文件的目录路径,比如: ./config.ini)),第二个参数是编码格式
host = cnp.get('mysql', 'host')
print(host)  # 127.0.0.1

pwd = cnp.get('mysql', 'password')
print(pwd)  # 123456
print(type(pwd))  # <class 'str'>

# 注意 get读取的默认数据都是字符串格式,我们也可以读取其它类型
port = cnp.getint('mysql', 'port')
print(port)  # 3306
print(type(port))  # <class 'int'>

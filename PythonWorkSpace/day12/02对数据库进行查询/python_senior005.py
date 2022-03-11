"""
--------------------------------
@Time    :  2022/2/21 - 13:56
@Author  :  Lee
@File    :  python_senior001
--------------------------------
"""

"""
知识点:python操作mysql,查询(查询单条、查询多条、查询所有)
"""

# 第一步:导入第三方模块,pymysql是一个第三方的模块,我们需要先进行安装,再导包,然后通过pymysql操作mysql数据库
import pymysql

# 第二步: 获取连接对象(我们需要指定mysql服务器的ip地址,端口号,用户名,密码,指定的库名)
# 127.0.0.1和localhost都是闭环地址,都指向本机的ip地址
# mysql默认的端口号3306 oracle默认的端口号1521 http默认的端口号80 https默认的端口号443
# db是database数据库的缩写
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
print(conn)

# 第三步: 获取一个游标对象
cursor = conn.cursor()  # 游标能够存储结果集

# 第四步: 通过游标执行sql语句,把结果存在cursor里,并且返回条目数
count = cursor.execute('select * from account;')
print(count)  # 5 获取结果集中的条目数

# 第五步: 获取结果集中的数据
# 第一种:获取结果集中的一行数据
# data = cursor.fetchone()  # 返回一条数据,并且包装成元组
# print(data)

# 第二种:获取结果集中的多行数据
data = cursor.fetchmany(2)  # 获取结果集中的2条数据,并且包装成元组
print(data)  # 返回多条数据,格式: ((元组1),(元组2)....)

# 第三种:获取结果集中的所有数据
# data = cursor.fetchall()  # 获取结果集中的所有数据,并且包装成元组
# print(data)  # 返回多条数据,格式: ((元组1),(元组2)....)

# 第六步:关闭游标
cursor.close()

# 第七步:关闭连接对象
conn.close()

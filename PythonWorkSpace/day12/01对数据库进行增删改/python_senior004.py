"""
--------------------------------
@Time    :  2022/2/21 - 13:56
@Author  :  Lee
@File    :  python_senior001
--------------------------------
"""

"""
知识点:python操作mysql数据库,进行增删改
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

# 第四步: 批量增删改  executemany(sql,列表)
# count = cursor.executemany("insert into account(name,age,nickName) values(%s,%s,%s);",
#                    [('xiaolan', 20, 'lanlan'), ('xiaohong', 18, 'honghong'), ('xiaobai', 20, 'dabai')])
# count = cursor.executemany("delete from account where name = %s;", [('xiaolan',), ('xiaohong',)])
count = cursor.executemany("update account set age = %s where name = %s;", [(50, 'xiaohua'), (60, 'xiaobai')])
print(count)

# 第五步:增删改都需要提交,不能忘记,否则数据库数据不变
conn.commit()

# 第六步:关闭游标
cursor.close()

# 第七步:关闭连接对象
conn.close()

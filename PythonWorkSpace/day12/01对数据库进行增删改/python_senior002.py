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

# 第四步: 通过游标对象执行sql语句,调用execute()方法
"""
通过execute方法提供的另外一个方式操作数据库  execute(sql,params)
把活得数据通过%s进行占位,再通过元组进行赋值,好处:
    1.增加SQL代码可读性
    2.占位符可以预先编译，提高执行效率
    3.防止SQL注入
    4用占位符的目的是绑定变量，这样可以减少数据SQL的硬解析，所以执行效率会提高不少
"""
# count = cursor.execute("insert into account(name,age,nickName) values(%s,%s,%s);", ('小美', 18, '美美'))
# count = cursor.execute("delete from account where name = %s;", ('小美',))
count = cursor.execute("update account set name = %s where name = %s;", ('dahuahua', "Dahua"))
print(count)

# 第五步:增删改都需要提交,不能忘记,否则数据库数据不变
conn.commit()

# 第六步:关闭游标
cursor.close()

# 第七步:关闭连接对象
conn.close()

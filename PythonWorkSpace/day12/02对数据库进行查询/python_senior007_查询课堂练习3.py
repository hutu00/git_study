"""
-------------------------------------------------
   date      :2021/11/3-11:33
   Author    :Lee
   File Name :python_senior02
-------------------------------------------------
"""

'''
知识点:python操作mysql,通过占位符查询
pytest_01: execute(sql,params)方式查询出SMITH的工资,并且打印在控制台
'''
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')
cursor = conn.cursor()
count = cursor.execute("select sal from emp where lower(ename) = %s;", ("smith",))  # 执行sql语句
data = cursor.fetchone()  # 从游标中获取内容
print(data[0])  # 拿到具体的工资
cursor.close()
conn.close()

"""
-------------------------------------------------
   date      :2021/11/3-11:33
   Author    :Lee
   File Name :python_senior02
-------------------------------------------------
"""

"""
知识点:python操作mysql
pytest_01: 填写代码获取emp表中的所有数据。通过excute(sql)
"""

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
print(conn)
cursor = conn.cursor()
count = cursor.execute('select * from emp;')
data = cursor.fetchall()
print(data)
cursor.close()
conn.close()

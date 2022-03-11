# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/15-10:21
=============================
"""

'''
1、克隆 dept 为 dept_xxx。 create table dept_xxx as select * from dept
2、使用 execute(sql) 为dept_xxx表增加部门编号为 50 部门名称为 Tester， Loc为‘BeiJing’
'''

import pymysql  # 第一步导库

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')  # 第二步: 连库
print(conn)
cursor = conn.cursor()  # 第三步: 获取游标
count = cursor.execute('create table dept_lee as select * from dept;')  # 第四步: 执行sql语句
print(count)
count1 = cursor.execute("insert into dept_lee values(%s,%s,%s);", (50, 'tester', 'BeiJing'))
print(count1)

conn.commit()  # 第五步：提交
cursor.close()  # 第六步：关闭游标
conn.close()  # 第七步：关闭连接

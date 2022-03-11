# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/15-10:21
=============================
"""

# pytest_01: 使用 CV大法模仿以最快的速度完成如下作业,该文件直接下发。
'''
通过两种方式实现如下功能:
1、为dept_xxx表增加部门编号为 60 部门名称为 Test， Loc为 'ShangHai'
2、删除部门编号为 60的部门
'''

'''
使用 execute(sql,params) 为dept_xxx表增加部门编号为 60 部门名称为 DEV， Loc为‘BeiJing’
'''

import pymysql  # 第一步导库

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='test')  # 第二步: 连库
print(conn)
cursor = conn.cursor()  # 第三步: 获取游标
count = cursor.execute("insert into dept_lee values(%s,%s,%s);", (60, 'Test', 'ShangHai'))  # 第四步: 执行sql语句
print(count)
count1 = cursor.execute("delete from dept_lee where deptno = %s;", (60,))
print(count1)

conn.commit()  # 第五步：提交
cursor.close()  # 第六步：关闭游标
conn.close()  # 第七步: 关闭连接

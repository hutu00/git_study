# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2022/1/17-14:37
=============================
"""

'''
# 使用pymysql完成这些题目
1、使用python语言操作(查询) test库中的emp表
2、通过占位符方式查询出smith所在的部门名称,并且打印在控制台
3、通过占位符的方式查询出20部门的所有员工的信息。
4、通过占位符的方式查询出job为 SALESMAN的工资总和
5、查询出部门编号20有多少人？
6、为dept表增加部门编号为 50 部门名称为 Test， Loc为‘ShangHai’
7、批量更新dept表中编号为50的部门名称为TestSoftW,30部门的部门名称为SLS
8、删除部门编号为 50的部门
'''

# 1、使用python语言操作(查询) test库中的emp表
from db_utils03 import DBUtils

db = DBUtils()
data = db.find_all('select * from emp;')
print(data)

# 2、通过占位符方式查询出smith所在的部门名称,并且打印在控制台
data = db.find_one("select d.DNAME from dept d,emp e where d.deptno = e.deptno and lower(e.ename) = %s;", ('smith',))
print(data[0])

# 3、通过占位符的方式查询出20部门的所有员工的信息。
data = db.find_all("select * from emp where deptno = %s;", (20,))
print(data)

# 4、通过占位符的方式查询出job为 SALESMAN的工资总和
data = db.find_one("select sum(sal) from emp where lower(job) = %s;", ('salesman',))
print(data[0])

# 5、查询出部门编号20有多少人？
count = db.find_count("select * from emp where deptno = %s;", (20,))
print(count)

# 6、为dept表增加部门编号为 50 部门名称为 Test， Loc为‘ShangHai’
count = db.cud("insert into dept values(%s,%s,%s);", (50, 'Test', 'ShangHai'))
print(count)

# 7、批量更新dept表中编号为50的部门名称为TestSoftW,30部门的部门名称为SLS
count = db.cud("update dept set dname = %s where deptno = %s;", [("TestSoftW", 50), ("SLS", 30)])
print(count)

# 8、删除部门编号为 50的部门
count = db.cud("delete from dept where deptno = %s;", (50,))
print(count)

db.close()

"""
--------------------------------
@Time    :  2022/2/21 - 17:37
@Author  :  Lee
@File    :  python_senior008
--------------------------------
"""

"""
使用数据库工具类,为dept_xxx表增加部门编号为70,部门名称为 DBA,Loc为'ShenZhen'
"""

from db_utils01 import DBUtils

db = DBUtils()

count = db.cursor.execute("insert into dept_lee values(%s,%s,%s);", (70, 'DBA', 'ShenZhen'))
print(count)  # 1
db.conn.commit()

count = db.cursor.execute("select * from emp;")
data = db.cursor.fetchall()
print(data)

db.close()

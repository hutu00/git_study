# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2022/1/15-11:56
=============================
"""
# 练习1
# 在自己的mysql下, businessdb 库中创建tsd24_xxx表,建表语句如下，直接改表名后使用。
'''
create table tsd24_xxxxx(
t_name varchar(20),
t_age varchar(3),
t_sex varchar(6)
)
'''
# 1、通过pymysql为数据库添加两条数据 如下内容: xiaohua,18,女|xiaoming,19,女
from db_utils01 import DBUtils

db = DBUtils()
count = db.cursor.executemany("insert into tsd24_lee values(%s,%s,%s);", [('xiaohua', 18, '女'), ('xiaoming', 19, '女')])
db.conn.commit()
print(count)

# 2、通过pymysql修改小明的sex为男  (通过占位符方式)
count = db.cursor.execute("update tsd24_lee set t_sex = %s where t_name = %s;", ('男', 'xiaoming'))
print(count)
db.conn.commit()

# 3、查询小花的年龄和性别  (通过占位符方式)
count = db.cursor.execute("select t_age,t_sex from tsd24_lee where t_name = %s;", ('xiaohua',))
print(db.cursor.fetchone())

# 4、删除 表中的所有内容
db.cursor.execute("delete from tsd24_lee;")
db.conn.commit()

db.close()

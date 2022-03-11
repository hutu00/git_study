"""
--------------------------------
@Time    :  2022/2/21 - 17:28
@Author  :  Lee
@File    :  db_utils01
--------------------------------
"""
"""
我们每次操作数据库都要进行连接和关闭,所以我们可以封装连接和关闭,封装后我们每次调用就行
"""

import pymysql


class DBUtils(object):
    # 封装连接对象和游标对象
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("数据库工具类连接出现异常,请检查DButils中的__init__方法!")
            print(e)

    # 封装关闭游标对象和连接对象
    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':  # 在当前模块下运行代码
    db = DBUtils()
    print(db.conn, db.cursor)
    db.close()

"""
--------------------------------
@Time    :  2022/1/20 - 15:44 
@Author  :  Lee
@File    :  python_basic32 
--------------------------------
"""

"""
self 代表当前对象,谁调用就代表谁
"""


class Student:
    stu_id = ''
    stu_name = ''
    stu_sex = ''

    def study(self):
        print("{}正在学python".format(self.stu_name))  # 打印当前对象的stu_name属性值,拼接'正在学python'

    def sleep(self):
        print('11点前在', self.stu_sex, '宿舍就寝,别跑错了.早睡早起身体棒棒!')


stu01 = Student()  # 创建了Student类的实例对象stu01
stu01.stu_name = '小花'  # 为对象属性赋值
stu01.stu_sex = '女'
stu01.stu_id = '1001'
stu01.stu_age = 20
stu01.study()  # 通过对象调用所属类中的属性和方法
stu01.sleep()  # 11点前在 女 宿舍就寝,别跑错了.早睡早起身体棒棒!

stu02 = Student()  # 创建了Student类的实例对象stu02
stu02.stu_name = 'xiaomei'
stu02.stu_sex = '男'
stu02.stu_id = '1002'
stu02.study()  # xiaomei正在学python
stu02.sleep()  # 11点前在 男 宿舍就寝,别跑错了.早睡早起身体棒棒!

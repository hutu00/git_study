"""
--------------------------------
@Time    :  2022/1/21 - 11:21 
@Author  :  Lee
@File    :  python_basic38 
--------------------------------
"""

"""
封装:
第一层面的封装:就是把某一类操作写在一个类中,供以后调用.就是封装
第二层面的封装:类中把某些属性和方法隐藏起来(或者说定义为私有),只能在类的内部使用、外部无法访问,或者留下少量的函数供外部访问
"""

name = 'xiaohua'
sex = '女'
age = 20


# 声明三个变量去形容小花这个同学,这有什么弊端?
# 弊端:太零散,如果学生太多,需要不断的新建变量去描述

class Student:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


one = Student("老刘", '男', 38)
two = Student("老王", '男', 32)
three = Student("老徐", '男', 28)

print("姓名:{},性别:{},年龄:{}".format(two.name, two.sex, two.age))  # 姓名:老王,性别:男,年龄:32


# 第二层面的封装: 控制访问权限
# 我们可以把所有的属性私有,不在允许对象访问

class Stu:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age


four = Stu("小花", '女', 20)


# print(four.name)  # 该行代码报错 AttributeError: 'Stu' object has no attribute 'name'

# 问题来了: 现在我们把name,age,sex设置为私有属性,但是我又想他们通过我指定的接口去访问或修改我的属性,该怎么办?
class Stu1:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age1):
        self.__age = age1

    def get_sex(self):
        return self.__sex


# 这样有效的控制了访问、修改的权限只有age允许修改,name、age、sex只允许访问
five = Stu1('小李mini', '男', 26)
print(five.get_name(), five.get_age(), five.get_sex())  # 小李mini 26 男
five.set_age(30)
print(five.get_name(), five.get_age())  # 小李mini 30

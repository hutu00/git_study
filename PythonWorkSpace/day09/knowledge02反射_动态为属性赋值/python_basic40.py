"""
--------------------------------
@Time    :  2022/1/21 - 14:36 
@Author  :  Lee
@File    :  python_basic40 
--------------------------------
"""


# 反射,我们可以在代码运行过程中,为属性赋值
class Student:
    pass


t = Student()
# setattr(对象名,属性名,属性值) 动态的为实例对象的实例属性赋值
setattr(t, "name", "xiaohua")  # 程序运行时,会为t对象创建属性name,值为xiaohua
setattr(t, "age", 18)
print(t.name, t.age)  # 通过对象获取值 xiaohua 18

# getattr(对象名,属性名) 程序运行时获取值
age = getattr(t, 'age')
name = getattr(t, 'name')
print(age, name)  # 18 xiaohua


# 使用场景,动态为属性赋值的时候使用

# 封装一个工具类,实现字典转换为对象
class Student2:
    def __init__(self, dict1):
        for i in dict1.items():  # (("name","xiaohua"),("age",20))
            setattr(self, i[0], i[1])


stu1 = Student2({"name": "xiaohua", "age": 20})
print(stu1.name, stu1.age)  # xiaohua 20

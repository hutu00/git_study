"""
--------------------------------
@Time    :  2022/1/21 - 14:23 
@Author  :  Lee
@File    :  python_basic39 
--------------------------------
"""

"""
方法重写/方法覆盖:子类继承父类,子类和父类具有相同的方法
"""


class Animal:
    country = ''
    name = ''
    age = 0

    def walk(self):
        print("父类的walk方法")


class Dog(Animal):  # Dog类继承了Animal类
    def walk(self):
        print('子类的walk方法')


am1 = Animal()
am1.walk()  # 调用父类的walk方法

dd = Dog()
dd.walk()  # 子类的walk方法

# 多态  子类对象调用父类的方法
super(Dog, dd).walk()  # 父类的walk方法

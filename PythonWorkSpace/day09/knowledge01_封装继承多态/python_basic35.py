"""
--------------------------------
@Time    :  2022/1/21 - 10:23 
@Author  :  Lee
@File    :  python_basic35 
--------------------------------
"""

"""
继承:子类继承父类(超类,基类),子类就能使用父类的属性和方法.子类又叫派生类
继承的好处:减少代码的冗余、提高代码的重用性(子类一旦继承一个父类就可以使用父类的所有的属性和方法)
Java是单继承,Python是多继承
继承的语法:在声明类的时候在类名之后使用(父类1,父类2,父类3....)
"""


class Class1:
    pass


class Class2:
    pass


class Class3(Class1):  # Class3继承了Class1
    pass


class Class4(Class1, Class2):  # Class4 继承了Class1、Class2
    pass

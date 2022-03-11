"""
--------------------------------
@Time    :  2022/1/20 - 17:29 
@Author  :  Lee
@File    :  python_basic34 
--------------------------------
"""

"""
魔法方法: 在某些情况下自动调用的方法.由python自己提供,比如:
__new__():创建对象的时候自动调用
__init__():初始化实例对象时调用
__del__():会在删除对象的时候调用
魔法方法中的__init__会在初始化对象是自动执行,利用该特性我们可以在创建实例对象时做一些操作

一般写一个类,如果不声明__init__时会自动使用默认的,默认的构造方法一般不显示,如果声明了__init__方法,会覆盖默认的
注意: 不能同时有两个__init__方法
"""


class Emp:
    emp_no = ''  # 类属性
    emp_name = ''
    emp_sal = 2480

    # def __init__(self):  # 在初始化Emp类的实例对象时,python会自动调用Emp类中的__init__函数,当我们重写了以后,会自动完成我们的预期操作
    #     print('构造函数,在创建对象时触发自动调用!')

    def __init__(self, no, name, sal):  # 重写了__init__方法,要求在创建实例对象时传入3个参数,并且给绑定的实例对象的3个实例属性赋值
        self.emp_no = no
        self.emp_name = name
        self.emp_sal = sal


# emp01 = Emp()  # 创建了一个Emp类的实例对象,没有重写__init__方法时,使用默认的__init__方法

emp02 = Emp('1001', 'scott', 5000)  # 当__init__方法被重写时,必须要按照重写后的要求传参数才能创建实例对象
print(emp02.emp_no, emp02.emp_name, emp02.emp_sal)  # 1001 scott 5000

print(dir(Emp))  # 查看Emp类中的所有的属性和方法

print(dir(str))

print(isinstance('abc', str))  # True
print(isinstance(123, int))  # True

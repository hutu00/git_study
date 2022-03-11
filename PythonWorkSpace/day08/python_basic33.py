"""
--------------------------------
@Time    :  2022/1/20 - 15:56 
@Author  :  Lee
@File    :  python_basic33 
--------------------------------
"""

"""
实例方法:最少需要包含一个self参数,用来绑定调用此方法的实例对象
类方法:用装饰器@classmethod 来标识其为类方法,对于类方法,第一个参数必须是类对象,一般以cls作为第一个参数,可以通过类本身和实例对象去访问
静态方法:用装饰器@staticmethod 来标识其为静态方法,静态方法没有self/cls这样特殊的参数,静态方法无法调用任何类属性和类方法
"""
import time


class Emp:
    emp_no = ''  # 类属性
    emp_name = ''
    emp_sal = 2480
    __emp_age = 0  # 如果属性前有__,代表私有属性,只能在该类中使用

    # 计算年薪
    def year_sal(self):
        return self.emp_sal * 12

    print(__emp_age)  # 0

    # 计算请假天数的扣款
    @classmethod
    def fine(cls, day):  # 类方法,第一个参数代表类本身
        return cls.emp_sal / 22 * day

    @staticmethod
    def showtime():  # 静态方法,没有self/cls这样的特殊参数,无法使用类属性和类方法
        # print(emp_no)  # 会报错,静态方法无法使用类属性和类方法
        return time.strftime("%H:%M:%S", time.localtime())


Emp.emp_sal = 2600
# print(Emp.__emp_age)  # 会报错,私有属性 类外无法使用

# 实例方法:使用对象进行调用
emp01 = Emp()
emp01.emp_sal = 5000
print(emp01.year_sal())  # 60000

# 类方法: 推荐使用 类名.方法名() 直接调用
print(Emp.fine(2))  # 236.36

# 静态方法: 推荐使用 类名.方法名() 直接调用
print(Emp.showtime())  # 17:03:11

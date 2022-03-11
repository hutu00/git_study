"""
--------------------------------
@Time    :  2022/1/21 - 10:32 
@Author  :  Lee
@File    :  python_basic36 
--------------------------------
"""

"""
继承:子类继承父类(超类,基类),子类就能使用父类的属性和方法.子类又叫派生类
继承的好处:减少代码的冗余、提高代码的重用性(子类一旦继承一个父类就可以使用父类的所有的属性和方法)
Java是单继承,Python是多继承
继承的语法:在声明类的时候在类名之后使用(父类1,父类2,父类3....)
"""


class Animal:
    country = ''
    name = ''
    age = 0

    def walk(self):
        print("%s正在狂奔" % self.name)

    def say(self):
        print("%s正在咆哮" % self.name)


class Dog(Animal):  # Dog类继承了Animal类
    def look_door(self):
        print("警告你不要过来,小心我咬你!")


d1 = Dog()  # 创建了字类的实例对象
d1.name = '大黄'  # 调用父类的属性
d1.age = 10  # 调用父类的属性
d1.country = '中国'

d1.walk()  # 大黄正在狂奔
d1.say()  # 大黄正在咆哮
d1.look_door()  # 警告你不要过来,小心我咬你!

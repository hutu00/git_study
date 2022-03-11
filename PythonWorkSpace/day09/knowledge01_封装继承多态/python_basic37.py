"""
--------------------------------
@Time    :  2022/1/21 - 10:41 
@Author  :  Lee
@File    :  python_basic37 
--------------------------------
"""

"""
1.多继承:一个子类可以继承多个父类
2.多继承的情况下,字类会现在自己类中去寻找需要的内容,找不到再去父类中找
    该顺序按照 __mro__提供的顺序去找
"""


class Father:
    def f1(self):
        print("这是父类01")


class Mother:
    def f1(self):
        print("这是父类02")


class Baby(Father, Mother):
    pass


by = Baby()
by.f1()  # 这是父类01
print(Baby.__mro__)  # 查看方法解析顺序


# 菱形继承
class A:
    def test(self):
        print("from A ")


class B(A):
    # def test(self):
    #     print("from B ")
    pass


class C(A):
    # def test(self):
    #     print("from C ")
    pass


class D(B, C):
    # def test(self):
    #     print("from D ")
    pass


dd = D()
dd.test()  # 查找顺序 D B C A O
print(D.__mro__)

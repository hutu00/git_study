"""
--------------------------------
@Time    :  2022/1/19 - 10:44 
@Author  :  Lee
@File    :  python_basic27 
--------------------------------
"""

"""
函数:函数是可以重复使用的一段代码  比如:print() / id() / input() / type() / len() ....
函数的定义规则:
def 函数名([参数1,参数2,参数3....]):
    函数体(用来实现具体的功能)
    [return] 代表结束该函数并且返回数据
"""


def add():  # 声明了一个函数,名字是add,没有入参,没有返回
    print('该函数被调用')


add()  # 根据函数名调用add函数


def add1(a, b):  # 声明了一个函数,名字是add1,需要2个参数,调用该函数时必须传入2个参数,没有返回
    print(a + b)


add1(10, 20)  # 30 调用add1函数并且传入了2个参数
add1(14, 786)  # 800  函数可以多次使用


def add2(a, b, c):  # 声明了一个函数,名字是add2,需要3个参数,调用该函数时必须传入3个参数,有返回值
    return a + b + c


res = add2(10, 25, 35)
print(res)  # 70
print(add2(11, 22, 99))  # 132
print(add2('a', 'b', 'c'))  # abc


# 练习: 设计一个函数,有2个入参,该函数可以返回矩形面积,并且调用该函数三次
def area(length, width):
    """
    :param length: 长度
    :param width: 宽度
    :return: 矩形面积
    """
    return length * width


res = area(5, 4.5)
print(res)  # 22.5
print(area(10, 20))  # 200
print(area(15, 30))  # 450


# 声明一个函数,判断是奇数还是偶数,并返回判断结果
def judge(num):
    if num % 2:
        return '%d是奇数' % num
    else:
        return "{}是偶数".format(num)


print(judge(15))  # 15是奇数


# 声明一个函数,需要传入一个保存多个人的成绩的元组,该函数返回元组中所有成绩的和
def sum_score(tup1):
    sm = 0
    for i in tup1:
        sm += i
    return sm


tup1 = (50, 60, 70, 80, 90, 100)
print(sum_score(tup1))  # 450


# 函数返回多个值
def math(a, b):
    c = a + b
    d = a - b
    e = a / b
    f = a * b
    return c, d, e, f  # 如果返回多个值,会自动把多个值打包成一个元组返回


res = math(10, 20)
print(res)  # (30, -10, 0.5, 200)
print(*res)  # 30 -10 0.5 200

add3, min1, mul1, div1 = math(100, 50)
print(add3, min1, mul1, div1)  # 150 50 2.0 5000

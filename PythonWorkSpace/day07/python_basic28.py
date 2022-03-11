"""
--------------------------------
@Time    :  2022/1/19 - 14:32 
@Author  :  Lee
@File    :  python_basic28 
--------------------------------
"""
"""
函数参数的定义:
1.必须参数(位置参数)  2.默认参数  3.不定长参数(可变参数)  4.关键字参数
"""


# 1.必须参数(位置参数): 入参按照位置传递,在调用时入参的元素个数必须相同
def fun1(a, b, c):
    return a + b + c


res = fun1(10, 20, 30)
print(res)  # 60
res1 = fun1(c=100, b=300, a=500)  # 把100赋值给fun1函数中的c,把300赋值给fun1函数中的b,把500赋值给fun1函数中的a
print(res1)  # 900


# 2.默认参数:我们可以在声明方法的时候给入参设置默认值.  # 如果只传一个参数,那么b使用默认值,如果传入2个参数,b使用参数值
def fun2(a, b=10):  # 这里a是必须参数，b是默认参数,默认值是10
    return a + b


res = fun2(10)  # 把10赋值给a,b使用默认值
print(res)  # 20
res1 = fun2(10, 20)  # 把10赋值给a,把20赋值给b,b不使用默认值
print(res1)  # 30


# 3.不定长参数(可变参数):可以保存0-N个入参,一般使用*args,调用该方法时如果传入多个入参,会自动组包成一个元组
def fun3(*args):
    print("入参为:", args)


fun3()  # 入参为: ()
fun3(3)  # 入参为: (3,)
fun3(1, 2, 3)  # 入参为: (1, 2, 3)
fun3(1, 2, 3, 4, 5, 78, 8, 9, 9, 9, 10)  # 入参为: (1, 2, 3, 4, 5, 78, 8, 9, 9, 9, 10)


# 声明一个函数,需要传入多个人的成绩,该函数返回所有成绩的和
def fun4(*args):  # 接收多个参数并且打包成元组
    return sum(args)  # 求元组的和


print(fun4())  # 0
print(fun4(50, 80, 90, 100, 55))  # 375


# 4.关键字参数: 用来接收 key-value格式的入参,保存成一个字典
def fun5(**kwargs):  # 两个星号表示把传入的多个键值对打包成一个字典
    print("入参是:", kwargs)


fun5(a=1, b=2, c=3)  # 入参是: {'a': 1, 'b': 2, 'c': 3}
fun5(name='xiaohua', age=18, sex='女')  # 入参是: {'name': 'xiaohua', 'age': 18, 'sex': '女'}


# 使用关键字参数声明一个函数,并且调用该函数:传入多个值,求出这些值的和
def fun6(**kwargs):
    return sum(kwargs.values())


res = fun6(a=100, b=200, c=300)
print(res)  # 600


# 多种参数混合使用1
def test(x, y=5, z=6, *args, **kwargs):
    print('x的值是{},y的值是{},z的值是{},args的值是{},kwargs的值是{}'.format(x, y, z, args, kwargs))


test(1)  # x的值是1,y的值是5,z的值是6,args的值是(),kwargs的值是{}
test(1, 2)  # x的值是1,y的值是2,z的值是6,args的值是(),kwargs的值是{}
test((1, 2))  # x的值是(1, 2),y的值是5,z的值是6,args的值是(),kwargs的值是{}
test(1, 2, 3, 4, 5)  # x的值是1,y的值是2,z的值是3,args的值是(4, 5),kwargs的值是{}
test(1, 2, 3, 4, a=5, b=6)  # x的值是1,y的值是2,z的值是3,args的值是(4,),kwargs的值是{'a': 5, 'b': 6}
test(1, z=5)  # x的值是1,y的值是5,z的值是5,args的值是(),kwargs的值是{}


# 多种参数混合使用2
def test2(*args, **kwargs):
    print("args的值是{},kwargs的值是{}".format(args, kwargs))


test2()  # args的值是(),kwargs的值是{}
test2(1)  # args的值是(1,),kwargs的值是{}
test2(a=1, b=2)  # args的值是(),kwargs的值是{'a': 1, 'b': 2}
test2(1, 2, 3, a=3, b=4)  # args的值是(1, 2, 3),kwargs的值是{'a': 3, 'b': 4}

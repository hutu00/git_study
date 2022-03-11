"""
--------------------------------
@Time    :  2022/1/21 - 15:29 
@Author  :  Lee
@File    :  python_basic42 
--------------------------------
"""

"""
异常的处理:

try:
    语句块1
except 异常类型1:
    语句块2
except 异常类型2:
    语句块3
....
[else]: else可选内容,如果没有异常,则执行else中的内容
[finally]: finally为可选内容,不管有没有异常,都必须执行

执行try中的语句块1,如果语句块1出现了异常类型1则执行语句块2
"""

try:
    num = int(input("请输入一个整数:"))

    if num % 2:
        print('{}是奇数'.format(num))
    else:
        print("%d是偶数" % num)
except ValueError:  # 如果try中的代码出现了ValueError,则执行except下的代码
    print("请输入正确的整数!")
else:
    print("没有出现异常!")  # 如果try中的语句块没有出现异常,则执行else的内容
finally:
    print("执行完成!")  # 不管有没有异常最后都执行finally中的内容

"""分别处理多种异常"""
try:
    num = int(input("请输入一个数字:"))
    print(10 / num)
except ValueError:
    print("请输入正确的数据!")  # 处理非整数类型异常
except ZeroDivisionError:
    print("除数不能为0！")  # 处理除数为0异常

"""万能处理异常的方式"""
try:
    num = int(input("请输入一个数字:"))
    print(10 / num)
except Exception as e:  # 如果出现异常,就执行except下的代码
    print("请输入正确的数据!", e)  # e代表报错信息

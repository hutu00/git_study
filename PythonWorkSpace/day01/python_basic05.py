"""
--------------------------------
@Time    :  2022/1/12 - 14:06 
@Author  :  Lee
@File    :  python_basic05 
--------------------------------
"""

# input()函数

# input()这个函数用来读取控制台的输入,可以从控制台输入内容,并且保存到变量里
name = input("请输入您的姓名:\n")  # 变量name接收input()函数输入数据
print('您输入的姓名是:', name)  # 您输入的姓名是: 李老师
print(type(name))  # <class 'str'>

age = input("请输入您的年龄:")  # input()函数读取的所有从控制台的输入内容都是字符串类型
print("姓名是:", name, "年龄是:", age)
print(type(age))  # <class 'str'>

# 设计一个简单的两位整数加法运算器
num1 = int(input("请输入第一位整数:"))
num2 = int(input("请输入第二位整数:"))
sm = num1 + num2
print("两个整数之和是:", sm)

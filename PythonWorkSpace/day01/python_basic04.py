"""
--------------------------------
@Time    :  2022/1/12 - 10:50 
@Author  :  Lee
@File    :  python_basic04 
--------------------------------
"""

"""
本章讲解: 数字类型、布尔类型、字符串类型
"""

# 数字类型 分为 int / float / complex
a = 10
b = 10 / 3

print(a)  # 10
print(b)  # 3.3333333333333335

# 查看类型的函数  type()
print('a的变量类型为:', type(a))  # a的变量类型为: <class 'int'>
print('b的变量类型为:', type(b))  # b的变量类型为: <class 'float'>

# 布尔类型(bool): 只有2个值   True(真、成立)   False(假、不成立)
bo1 = 10 < 3
print(bo1)  # False

bo2 = 10 > 3
print(bo2)  # True
print('bo2的变量类型为:', type(bo2))  # bo2的变量类型为: <class 'bool'>

bo3 = 5 >= 5
print(bo3)  # True

# 字符串类型:用来保存一串字符 str
str1 = 'xiaohua'
str2 = "xiaomei"
str3 = '''xiaolan'''
str4 = """xiaohong"""

print(str1, str2, str3, str4)  # xiaohua xiaomei xiaolan xiaohong

# 字符串使用过程中的一些注意事项
# 1.单引号和双引号可以配合使用,但是需要符合书写规范
print("仇璐是个'优秀'的测试工程师")  # 仇璐是个'优秀'的测试工程师  单引号变成了字符串的成员
print("my name's China!")  # my name's China!

# 类型强制转换,使用 类型() 进行类型转换
# 1.数字类型和字符串类型强制转换
num = 10
str1 = str(10)
print(str1)  # 10
print(type(str1))  # <class 'str'>

str1 = '20'
num1 = int(str1)
print(num1)  # 20
print(type(num1))  # <class 'int'>

num2 = 3.5
str1 = str(num2)
print(str1)  # 3.5
print(type(str1))  # <class 'str'>

str1 = '5.5'
num3 = float(str1)
print(num3)  # 5.5
print(type(num3))  # <class 'float'>

str1 = '5a'
# num4 = int(str1)  # 该行代码报错,字符串转整数类型字符串所有成员只能是纯数字

num5 = 5.7
num6 = int(num5)
print(num6)  # 5  float类型转换为int类型会造成精度丢失
print(type(num6))  # <class 'int'>

# 2.数字类型、字符串类型转布尔类型
# 2.1 数字转布尔类型
num7 = 1
bo3 = bool(num7)
print(bo3)  # True

num8 = 0
bo4 = bool(num8)
print(bo4)  # False

num9 = 5.5
bo5 = bool(num9)
print(bo5)  # True

num10 = 0.0
bo6 = bool(num10)
print(bo6)  # False

# 2.2 布尔类型转数字
num11 = int(True)
print(num11)  # 1

num12 = int(False)
print(num12)  # 0   布尔类型的底层就是数字类型,就是0和1

num13 = float(True)
print(num13)  # 1.0

num14 = float(False)
print(num14)  # 0.0

# 2.3 字符串类型转布尔类型
str5 = '小花'
bo7 = bool(str5)
print(bo7)  # True

str6 = ''
bo8 = bool(str6)
print(bo8)  # False

''' 总结:非零即真，非空即真 '''

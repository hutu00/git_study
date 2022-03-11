"""
--------------------------------
@Time    :  2022/1/12 - 16:48 
@Author  :  Lee
@File    :  python_basic08 
--------------------------------
"""

"""
if语句
if 条件:
    语句块
    
如果条件满足则执行语句块,否则不执行语句块
"""

a, b = 10, 20
if a > b:  # False
    print('a>b成立')

num = 10
if num % 2 == 0:  # True
    print(num)  # 10

num1 = 21
if num1 % 2:  # 一个整数取余2只有2个结果,奇数取余2是1,偶数取余2是0   非0即真,非空即真   1  True
    print(num1)  # 21

# if...else
"""
if 条件:
    语句块1
else:
    语句块2

如果条件成立则执行语句块1,否则执行语句块2
"""
a, b = 10, 20
if a > b:  # False
    print('a>b成立')
else:
    print("a>b不成立")

num = 10
if num % 2:  # 一个整数取余2只有2个结果,奇数取余2是1,偶数取余2是0   非0即真,非空即真   1  True
    print("是奇数")
else:
    print("是偶数")

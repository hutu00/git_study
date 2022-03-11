"""
--------------------------------
@Time  :  2022/1/11 - 17:23 
@Author:  Lee
@File  :  python_basic02 
--------------------------------
"""
"""
本章讲解:变量
"""

print("侬好")

a = "今天天气很好,和你一样"  # a是一个变量,把后面的这句话存储在a里面
print(a)  # 今天天气很好,和你一样

# Ctrl+Alt+L  自动调整格式的快捷键
# 声明变量,变量是用来存储值的

# 知识点1: 变量的声明
a = 1  # 该行代码声明了一个变量a,并且赋值1,变量a是整数类型 int
b = 2  # 该行代码声明了一个变量b,并且赋值2,变量b是整数类型 int
print(a + b)  # 3

c = 3.5  # 该行代码声明了一个变量c,并且赋值3.5,变量c是浮点数类型 float
print(b + c)  # 5.5

# 保存字符串可以使用四种方式,一般使用前两种
name = 'xiaohua'  # 该行代码声明了一个变量name,并且赋值xiaohua,变量name是字符串类型 str
name1 = "xiaohong"
name2 = '''xiaomei'''
name3 = """xiaolan"""

# 知识点2: 变量的覆盖,变量可以一次声明,多次赋值,后面的值会覆盖前面的值
sal = 2480  # 声明sal变量,赋值为2480
sal = 5000  # 声明sal变量,赋值为5000
print(sal)  # 5000
sal = sal + 500
print(sal)  # 先运行sal+500,在赋值给sal  5500

name4 = 'xiaohua'
print(name4)  # xiaohua
name4 = 'xiaoliu'
print(name4)  # xiaoliu

# 知识点3: 同时为多个变量赋值
# 1.为多个变量赋值相同的值
a = b = c = 1  # 代表声明了a,b,c三个变量,且赋值为1
print(a, b, c)  # 1 1 1

# 2.为多个变量赋值不同的值
A, B, C = 1, 'xiaohua', 5.5  # 代表声明了A,B,C三个变量,并且赋值不同的值
print(A, B, C)  # 1 xiaohua 5.5

# 知识点4: python是一门大小写和缩进敏感的编程语言
sno = 1001
Sno = 1005
print('sno的值是:', sno)  # sno的值是: 1001
print("Sno的值是:", Sno)  # Sno的值是: 1005

print('tester24班')  # tester24班
# print('tester24班')  # 该行代码会报错,注意print前面有个空格,注意缩进问题,一般都是顶格写

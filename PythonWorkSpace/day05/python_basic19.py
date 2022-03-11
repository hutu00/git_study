"""
--------------------------------
@Time    :  2022/1/17 - 11:18 
@Author  :  Lee
@File    :  python_basic19 
--------------------------------
"""

"""
for 循环
for 变量 in 可迭代数据(str/list/tuple/range()):
    循环体
"""

# 知识点1: range()函数
for i in range(5):
    print(i)  # 打印了: 0,1,2,3,4
for i in range(0, 5):  # 每循环一次,把0-4数字赋值给i
    print(i)  # 打印了 [0,5)

for i in range(2, 10):
    print(i)  # 2,3,4,5,6,7,8,9

# 使用for循环,打印1-100的奇数和
sm = 0
for i in range(1, 101, 2):
    sm += i
print("1-100的奇数和为:", sm)  # 1-100的奇数和为: 2500

sm = 0
for i in range(1, 101):
    if i % 2 == 1:
        sm += i
print("1-100的奇数和为:", sm)  # 1-100的奇数和为: 2500

"""
--------------------------------
@Time    :  2022/1/17 - 15:29 
@Author  :  Lee
@File    :  python_basic22 
--------------------------------
"""

"""
冒泡排序
"""

# 数据交换,将a和b的值进行交换
a = 10
b = 20

# t = a
# a = b
# b = t

a, b = b, a

print('a的值:', a)  # a的值: 20
print('b的值:', b)  # b的值: 10

# 有一个元素类型为int类型的列表,[20,16,88,60,14],互换下标0和1位置的值
list1 = [20, 16, 88, 60, 14]

# temp = list1[0]
# list1[0] = list1[1]
# list1[1] = temp

list1[0], list1[1] = list1[1], list1[0]

print(list1)  # [16, 20, 88, 60, 14]

for i in range(len(list1) - 1):  # i = 0,1,2,3
    if list1[i] > list1[i + 1]:
        list1[i], list1[i + 1] = list1[i + 1], list1[i]
        # temp = list1[i]
        # list1[i] = list1[i + 1]
        # list1[i + 1] = temp

print(list1)  # [16, 20, 60, 14, 88]

# [16, 20, 60, 14, 88]
# 第一次循环两个相邻的值进行比较,一共比较4次,如果前面的值比后面的值大,交换位置
# [16, 20, 60, 14, 88] [16, 20, 60, 14, 88] [16, 20, 14, 60, 88] [16, 20, 14, 60, 88]
# 第二次循环两个相邻的值进行比较,一共比较4次,如果前面的值比后面的值大,交换位置
# [16, 20, 14, 60, 88] [16, 14, 20, 60, 88] [16, 14, 20, 60, 88] [16, 14, 20, 60, 88]
# 第三次循环两个相邻的值进行比较,一共比较4次,如果前面的值比后面的值大,交换位置
# [14, 16, 20, 60, 88] [14, 16, 20, 60, 88] [14, 16, 20, 60, 88] [14, 16, 20, 60, 88]
# 第四次循环两个相邻的值进行比较,一共比较4次,如果前面的值比后面的值大,交换位置
# [14, 16, 20, 60, 88] [14, 16, 20, 60, 88] [14, 16, 20, 60, 88] [14, 16, 20, 60, 88]

list1 = [20, 16, 88, 60, 14]

for j in range(len(list1) - 1):  # 外循环控制有几个数需要确定位置 j = 0,1,2,3
    for i in range(len(list1) - 1 - j):  # 内循环循环一次确定一个元素的位置  i = 0,1,2,3
        if list1[i] > list1[i + 1]:  # 如果前面比后面值大,则交换位置
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
print(list1)  # [14, 16, 20, 60, 88]
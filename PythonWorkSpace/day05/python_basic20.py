"""
--------------------------------
@Time    :  2022/1/17 - 11:28 
@Author  :  Lee
@File    :  python_basic20 
--------------------------------
"""

"""
for循环
for 变量 in 可迭代数据(str/list/tuple/range()):
    循环体
"""

# 遍历:就是把对象中的每一个元素都过一遍
# 用两种方式遍历下面的字符串
str1 = '生命诚可贵,爱情价更高,若为python故,二者皆可抛'

# 通过值遍历方式遍历字符串
for i in str1:
    print(i, end='')
print()

# 通过下标遍历字符串
for i in range(len(str1)):
    print(str1[i], end='')
print()

# 字符串、列表、元组、集合的遍历
# 值遍历
students = ['xiaoliu', 'xiaoxu', 'xiaowang']
for i in students:
    print(i)

# 下标遍历
for i in range(len(students)):
    print(students[i])

# 循环遍历字典,打印出所有key和value的值
dict1 = {"name": "xiaohua", "age": 20, "sex": "女", "nickName": "huahua"}

# 方式1
for i in dict1:
    print(i, dict1.get(i))

# 方式2
for i, j in dict1.items():
    print(i, j)

# 字典的遍历
dict2 = {"name": "xiaohua", "age": 20, "sex": "女", "nickName": "xiaohua"}
# 找出字典dict2的value值xiaohua出现的次数
count = 0
for i in dict2.values():
    if i == 'xiaohua':
        count += 1
print("xiaohua出现的次数是:", count)

# 统计下面这个元组中5出现的次数
tup1 = (1, 2, 3, 5, 6, 7, 78, 5, 7, 8, 19, 10, 5, 35, 96)
count = 0
for i in tup1:
    if i == 5:
        count += 1
print("5出现了{}次!".format(count))

count = 0
for i in range(len(tup1)):
    if tup1[i] == 5:
        count += 1
print("5出现了{}次!".format(count))

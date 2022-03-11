"""
--------------------------------
@Time    :  2022/1/14 - 10:55 
@Author  :  Lee
@File    :  python_basic14 
--------------------------------
"""

"""
我们发现,列表、元组、集合、字典都能够保存一组数据,不过他们有不同的特征
1.从保存值的方式来看,列表、元组、字典都可以保存一组值
2.列表和元组是可以通过下标去访问的,而集合和字典没有下标,字典通过key获取value
3.增删改方式不同
4.可变类型: 列表、集合、字典(值可以被修改);不可变类型: 数字、字符串、元组(值不能被改变)
"""

# 1.列表、元组、集合都是保存单个值,而字典已键值对来保存数据
# 比如保存红球:
list_redball = [5, 10, 15, 18, 22, 28]
tuple_redball = (7, 13, 16, 19, 25, 32)
set_redball = {3, 8, 17, 24, 29, 33}
dict_redball = {"第一个球": 1, "第二个球": 8, "第三个球": 13, "第四个球": 18}

# 2.列表和元组是可以通过下标去访问的,而集合没有下标,字典保存值的方式为key
print('list列表通过下标访问,比如获取下标为0的元素的值为:', list_redball[0])
print('tuple元组通过下标访问,比如获取下标为0的元素的值为:', tuple_redball[0])
print('set集合没有办法通过下标访问')
print('字典通过key获取value,比如方式1:', dict_redball["第二个球"])
print('字典通过key获取value,比如方式2:', dict_redball.get("第三个球"))

# 3.增加元素
list_redball.append(21)  # 列表增加元素用append()
print(list_redball)  # [5, 10, 15, 18, 22, 28, 21]
print('元组为不可变类型,所以不能对元组进行增删改')
set_redball.add(21)  # 集合增加元素用add()
print(set_redball)  # {33, 3, 8, 17, 21, 24, 29}
dict_redball["第五个球"] = 21  # 字典增加数据
print(dict_redball)  # {'第一个球': 1, '第二个球': 8, '第三个球': 13, '第四个球': 18, '第五个球': 21}

# 4.删除元素
list_redball.pop(1)  # 列表删除方式1:通过下标删除,删除下标为1的位置的值
list_redball.remove(21)  # 列表删除方式2:通过值删除,删除值为21的元素
print(list_redball)  # [5, 15, 18, 22, 28]
print('元组为不可变类型,所以不能对元组进行增删改')
set_redball.remove(21)  # 集合通过值删除,删除值为21的元素
print(set_redball)  # {33, 3, 8, 17, 24, 29}
dict_redball.pop("第五个球")  # 字典通过key删除
print(dict_redball)  # {'第一个球': 1, '第二个球': 8, '第三个球': 13, '第四个球': 18}

# 5.修改元素 比如:把第一个球改为 11
list_redball[0] = 11  # 列表修改操作可以直接通过下标赋值
print(list_redball)  # [11, 15, 18, 22, 28]
print('元组为不可变类型,所以不能对元组进行增删改')
print('set集合没有下标,所以不能直接修改值')
dict_redball["第一个球"] = 11  # 字典通过key获取元素和修改
print(dict_redball)  # {'第一个球': 11, '第二个球': 8, '第三个球': 13, '第四个球': 18}

# 以上是对列表、元组、集合、字典的总结,还有一些公共的API,我们需要学习

list_redball = [5, 10, 15, 18, 22, 28]
tuple_redball = (7, 13, 16, 19, 25, 32)
set_redball = {3, 8, 17, 24, 29, 33}
dict_redball = {"第一个球": 1, "第二个球": 8, "第三个球": 13, "第四个球": 18}

# 1.字符串、列表、元组切片,获取一部分值
number = '15821598071'
print(number[0:5])  # 15821 字符串切片
print(list_redball[1:4])
print(tuple_redball[2:5])

# 2.求长度用 len()
print(len(number), len(list_redball), len(tuple_redball), len(set_redball), len(dict_redball))

# 3.判断某个值是否在列表、元组、集合、字符串、字典中使用 in / not in
print('1' in number)
print(10 in list_redball)
print(7 in tuple_redball)
print(7 in set_redball)
print('第一个球' in dict_redball)  # 字典默认判定的是 键
# 判定值是否存在字典的value中
print(7 in dict_redball.values())  # 需要先获取字典的所有的值在进行判断

# 4. 求列表、元组、集合、字典中: 最大值 max() 、最小值 min()、 求和 sum()
print("列表的最大值是:{},最小值是:{},和为:{}".format(max(list_redball), min(list_redball), sum(list_redball)))
print("元组的最大值是:{},最小值是:{},和为:{}".format(max(tuple_redball), min(tuple_redball), sum(tuple_redball)))
print("集合的最大值是:{},最小值是:{},和为:{}".format(max(set_redball), min(set_redball), sum(set_redball)))
value = dict_redball.values()
print("字典的值的最大值是:{},最小值是:{},和为:{}".format(max(value), min(value), sum(value)))

# 5.字符串、列表、元组统计元素出现的次数 count()
str1 = 'xiaohuahua'
print(str1.count('a'))  # 3
print(list_redball.count(10))  # 1
print(tuple_redball.count(8))  # 0

# 6.字符串、列表、元组合并用 + 重复用 *
str1, str2, str3 = 'i ', 'am ', 'teacher'
str4 = str1 + str2 + str3
print(str4 * 2)
list1, list2 = [1, 2, 3], [4, 5, 6]
list3 = list1 + list2
print(list3 * 2)
tup1, tup2 = ('a', 'b', 'c'), (1, 2, 3)
tup3 = tup1 + tup2
print(tup3 * 2)

# 7.列表、元组、字符串、集合的相互转换

# 字符串转列表
phone_number = '15821598071'
list_number = list(phone_number)
print(list_number)  # ['1', '5', '8', '2', '1', '5', '9', '8', '0', '7', '1']

# 字符串转元组
phone_number = '15821598071'
tuple_number = tuple(phone_number)
print(tuple_number)  # ('1', '5', '8', '2', '1', '5', '9', '8', '0', '7', '1')

# 列表转元组
list1 = [5, 10, 15, 18, 22, 28]
tup1 = tuple(list1)
print("列表转换为元组:", tup1, "转换后的类型:", type(tup1))  # 列表转换为元组: (5, 10, 15, 18, 22, 28) 转换后的类型: <class 'tuple'>

# 字符串转集合,因为集合不能重复,所以相同的元素会被过滤掉
phone_number = '15821598071'
set_number = set(phone_number)
print(set_number)  # {'2', '8', '7', '0', '9', '5', '1'}

# del 删除,可以删除任何数据
nick_name = '迟迟'
print(nick_name)
del nick_name
# print(nick_name)  # 报错

list1 = [1, 2, 3]
print(list1)
del list1
# print(list1)  # 报错

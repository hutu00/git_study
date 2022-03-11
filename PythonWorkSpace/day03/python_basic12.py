"""
--------------------------------
@Time    :  2022/1/13 - 16:24 
@Author  :  Lee
@File    :  python_basic12 
--------------------------------
"""

"""
本章讲解:集合  set
集合的定义:{value1,value2,value3....}
集合的特征:无序、没有索引、不能重复
注意:集合只能存放不可变类型(数字、字符串、元组)
"""

# 1.集合的定义
redball1 = set()  # 定义了一个空集合
redball2 = {7, 10, 16, 23, 30, 32, 10}  # 存放一组双色球的红球
# 特征
print(redball2)  # {32, 7, 10, 16, 23, 30}  打印出来是无序的,没有下标
# set1 = {1, 2, 3, 4, [1, 2]}  # 不能存放可变类型的数据

# 2.删除元素用remove: 删除redball集合中的 30
redball2.remove(30)
print(redball2)  # {32, 7, 10, 16, 23}

# 3.集合添加元素用add(): 为redball2集合添加 6
redball2.add(6)
print(redball2)  # {32, 6, 7, 10, 16, 23}

# 4. 集合的交集intersection() 和 并集union()
redball2 = {7, 10, 16, 23, 30, 32}
redball3 = {1, 2, 3, 4, 5, 6, 7}
print(redball2.union(redball3))  # {32, 1, 2, 3, 4, 5, 6, 7, 10, 16, 23, 30}
print(redball2.intersection(redball3))  # {7}

# 5.清空集合元素
redball2.clear()
print(redball2)  # set()

# 6.del删除
del redball2
# print(redball2)  # 会报错,因为redball2已经被删除了

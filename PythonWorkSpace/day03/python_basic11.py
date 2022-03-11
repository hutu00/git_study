"""
--------------------------------
@Time    :  2022/1/13 - 15:25 
@Author  :  Lee
@File    :  python_basic11 
--------------------------------
"""

"""
本章讲解:元组 tuple
元组的定义: 元组和列表一样存储一组任意类型的数据,但是元组为不可变类型,创建后不能修改数据
        (三大序列: str字符串/list列表/tuple元组)
"""

# 1.元组的声明:
redball1 = ()  # 创建了一个空元组
print(type(redball1))  # <class 'tuple'>
redball2 = (7, 9, 15, 18, 24, 33)

# 特殊情况
redball3 = (11,)  # 如果元组保存一个数据,需要加 , 号
print(type(redball3))  # <class 'tuple'>
redball4 = (11)  # 如果不加 , 号,这是一个int类型
print(type(redball4))
redball5 = 11,
print(redball5)  # (11,)  任意无符号类型对象,以逗号隔开会自动组包成元组
print(type(redball5))  # <class 'tuple'>

# 2.查看元组中的数据,通过下标访问
redball6 = (7, 9, 15, 18, 24, 33)
print(redball6[5])  # 33
print(redball6[-1])  # 33
print(redball6[2:-1])  # (15, 18, 24)
print(redball6[1:-1:2])  # (9, 18)

# 3.元组为不可变类型,所以不能修改和删除
# redball6[2] = 10  # 该行代码报错,不支持修改

# 4. 序列通用的API   in / not in / len() / max() / min() / sum() / + / * .....
print(max(redball6))  # 33
print(redball6 + (1, 2, 3))  # (7, 9, 15, 18, 24, 33, 1, 2, 3)

"""
列表和元组的区别:
1.列表和元组都是序列
2.列表和元组都可以存放任意类型的数据
3.列表是[],元组是()
4.列表是可变类型,元组是不可变类型
"""

# id()查看内存地址
redball6 = (7, 9, 15, 18, 24, 33)
print('redball6的物理地址是:', id(redball6))  # redball6的物理地址是: 1996634119528
redball7 = redball6 + (1, 2, 3)
print('redball7的物理地址是:', id(redball7))  # redball7的物理地址是: 1996634134232

# 元组内存放可变类型成员是可以被修改的,同时元组物理地址不变
tup1 = (1, 2, [1, 2, 3])
print("改变前的地址:", id(tup1))
tup1[2][2] = 999
print(tup1)
print("改变后的地址:", id(tup1))

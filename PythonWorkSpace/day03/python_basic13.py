"""
--------------------------------
@Time    :  2022/1/13 - 16:47 
@Author  :  Lee
@File    :  python_basic13 
--------------------------------
"""

"""
字典:以key(键) - value(值) 形式来保存数据 {key1:value1,key2:value2,key3:value3......}
"""

"""
part01:字典的常见操作
"""

# 1.字典的定义
redball1 = {}  # 定义了一个空字典
print(type(redball1))  # <class 'dict'>
# 注意字典的key不能重复
redball2 = {"第一个球": 2, "第二个球": 12, "第三个球": 20, "第四个球": 25}  # 存放一组双色球的红球

# 2.通过key获取value 方式1:
print("第一个球的值为:", redball2["第一个球"])  # 第一个球的值为: 2

# 3.通过key获取value 方式2:
print("第三个球的值为:", redball2.get("第三个球"))  # 第三个球的值为: 20

# 4.修改value值  把第三个球的值修改为 18
redball2["第三个球"] = 18
print(redball2)  # {'第一个球': 2, '第二个球': 12, '第三个球': 18, '第四个球': 25}

# 5.增加单个键值对
redball2["第五个球"] = 28
print(redball2)  # {'第一个球': 2, '第二个球': 12, '第三个球': 18, '第四个球': 25, '第五个球': 28}

# 6.根据key删除value 删除第五个球
redball2.pop("第五个球")
print(redball2)  # {'第一个球': 2, '第二个球': 12, '第三个球': 18, '第四个球': 25}

"""
part02:字典的其他知识
"""

dict1 = {1: [1, 2, 3], 2: (1, 2, 3), 3: "xiaohua"}

# 获取所有的key
info = {"name": "xiaohua", "age": 18, "sex": "女"}
print(list(info.keys()))  # ['name', 'age', 'sex'] 获取字典所有的key,并且转换为列表

# 获取所有的value
print(list(info.values()))  # ['xiaohua', 18, '女']

# 获取字典所有的键值对,重点
print(list(info.items()))  # 把字典的每一个键值对打包成元组返回
# [('name', 'xiaohua'), ('age', 18), ('sex', '女')]

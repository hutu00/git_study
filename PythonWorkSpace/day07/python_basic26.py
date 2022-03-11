"""
--------------------------------
@Time    :  2022/1/19 - 10:24 
@Author  :  Lee
@File    :  python_basic26 
--------------------------------
"""

"""
组包/装包:通俗的说,组包就是把多个数据装在一个元组中
拆包/解包:把一组数据进行拆分,比如 列表/字典/元组 等拆分成单个数据
"""

# 自动组包  任意无符号对象以逗号隔开,会自动组包成元组类型
red_balls = 1, 10, 16, 19, 20, 30
print(red_balls)  # (1, 10, 16, 19, 20, 30)
print(type(red_balls))  # <class 'tuple'>  将多个元素组装成一个元组

teachers = "老刘", "老徐", "老王", "彦祖"
print(teachers)  # ('老刘', '老徐', '老王', '彦祖')

# 自动拆包
red_balls = (1, 2, 3)
first_ball, sed_ball, third_ball = red_balls
print(first_ball, sed_ball, third_ball)  # 1 2 3

teachers = ('老刘', '老徐', '老王', '彦祖')
F1, F2, F3, F4 = teachers
print(F1, F2, F3, F4)  # 老刘 老徐 老王 彦祖

# 手动拆包/组包
print(*teachers)  # 老刘 老徐 老王 彦祖
F1, *F = teachers
print('F1是:', F1)  # F1是: 老刘
print("F的值是:", F)  # F的值是: ['老徐', '老王', '彦祖']  把其余的放到一个列表里赋值给F

*F, F4 = teachers
print('F4是:', F4)  # F4是: 彦祖
print("F的值是:", F)  # F的值是: ['老刘', '老徐', '老王']

F1, *F, F4 = teachers
print('F1是:', F1)  # F1是: 老刘
print('F4是:', F4)  # F4是: 彦祖
print("F的值是:", F)  # F的值是: ['老徐', '老王']

dict1 = {"name": "xiaohua", "sex": "女", "age": 20}

# 字典默认拆包的是键
a, b, c = dict1
print(a, b, c)  # name sex age

a, b, c = dict1.values()
print(a, b, c)  # xiaohua 女 20

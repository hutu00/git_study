"""
--------------------------------
@Time    :  2022/1/13 - 11:39 
@Author  :  Lee
@File    :  python_basic10 
--------------------------------
"""

"""
本章讲解:列表  

列表的定义:[]
列表的作用:可以存储任意类型一组数据,比如我们的双色球
列表也是属于序列之一、列表是可变类型
"""

# 1.列表的声明
redball1 = []  # 定义了一个空列表
print(type(redball1))  # <class 'list'>
redball2 = [1, 2, 3, 4, 5, 6]  # 存放一组双色球的红球
print(redball2)

# 2.1为列表增加单个元素: append()
redball1.append(11)
print(redball1)  # [11]
redball1.append([22, 11])
print(redball1)  # [11, [22, 11]]

# 2.2在列表尾部追加多个元素: extend()
redball1.extend([1, 2, 3])
print('增加多个元素后的列表:', redball1)

# 3.通过下标(和字符串一样,从0开始)获取元素的值，比如redball2获取第一个元素和第三个元素
first_ball = redball2[0]
third_ball = redball2[2]
print('第一个球为:', first_ball, '第三个球为:', third_ball)

print(redball2[0:3])  # 查看第一个到第三个球

# 4.通过下标修改值,比如我想把第一个红球改为6,第三个红球改为9
redball2[0] = 6
redball2[2] = 9
print('修改后的列表为:', redball2)  # 修改后的列表为: [6, 2, 9, 4, 5, 6]

# 5.删除元素方式1: pop(index) 通过下标进行删除。比如：删除第一个球
redball2.pop(0)
redball2.pop(2)
print('删除后的列表为:', redball2)  # 删除后的列表为: [2, 9, 5, 6]

# 6.删除元素方式2: remove() 根据元素值进行删除,把 redball2中4进行删除
redball2 = [1, 2, 3, 4, 5, 6, 4]
redball2.remove(4)
print(redball2)  # [1, 2, 3, 5, 6, 4]

# 7.列表指定下标位置插入数据: insert(index,value)
redball2.insert(3, 4)
print(redball2)  # [1, 2, 3, 4, 5, 6, 4]

# 列表可以嵌套
students = [['张飞', '关羽', '刘备'], ['许褚', '郭嘉', '夏侯惇'], '曹操', '张大仙']  # 列表信息可以嵌套
#           [0][0]  [0][1]  [0][2]   [1][0]  [1][1]  [1][2]    [2]     [3]
print(students[0])  # ['张飞', '关羽', '刘备']
print(students[0][0])  # 张飞
print(students[0][1])  # 关羽
# 练习
# 1.删除下标为2的数据,根据'张大仙'这个名字进行删除数据
students.pop(2)
students.remove('张大仙')
print(students)  # [['张飞', '关羽', '刘备'], ['许褚', '郭嘉', '夏侯惇']]

# 2.为列表增加元素 ["周瑜","吕蒙",'太史慈']，注意把列表当成一个元素进行添加
students.append(["周瑜", "吕蒙", '太史慈'])
print(students)  # [['张飞', '关羽', '刘备'], ['许褚', '郭嘉', '夏侯惇'], ['周瑜', '吕蒙', '太史慈']]

# 3.获取[1][0]位置的数据
print(students[1][0])  # 许褚

# 4.修改夏侯惇为夏侯渊
students[1][2] = '夏侯渊'
print(students)  # [['张飞', '关羽', '刘备'], ['许褚', '郭嘉', '夏侯渊'], ['周瑜', '吕蒙', '太史慈']]

# 5.列表的反转和排序,reverse()翻转/sort()排序
redball2 = [1, 7, 13, 17, 19, 28]
redball2.reverse()  # 翻转
print('翻转后的结果为:', redball2)  # [28, 19, 17, 13, 7, 1]
redball2.sort()  # 排序 默认是升序 从小到大
print('从小到大排序结果:', redball2)  # 从小到大排序结果: [1, 7, 13, 17, 19, 28]
redball2.sort(reverse=True)  # 从大到小 降序排序
print("更改reverse排序方式开关的结果为:", redball2)

# 6.因为列表是序列所以可用 max()/min()/sum()/in/not in/+拼接/*重复....
print(max(redball2))  # 28
print(min(redball2))  # 1
print(sum(redball2))  # 85

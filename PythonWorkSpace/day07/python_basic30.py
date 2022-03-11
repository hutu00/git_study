"""
--------------------------------
@Time    :  2022/1/19 - 16:27 
@Author  :  Lee
@File    :  python_basic30 
--------------------------------
"""

"""
内置函数:python自带的函数
"""

# 常用的内置函数: print() / id() / len() / type() / input().....
# 高级内置函数

# 1.eval(): 能够识别字符串中的python表达式,并且进行运算
print('1+1')  # 1+1
print(eval('1+1'))  # 2  eval()将字符串中的表达式识别为1+1,并且进行运算
eval('print("hello world")')  # hello world
# 案例1:
num1 = input("请输入第一个整数:")
num2 = input("请输入第二个整数:")
print(eval(num1) + eval(num2))  # 识别字符串中的数字
# 案例2:
# 求出如下字符串中元素的和:"[1,2,3,4,5]"
print(sum(eval("[1,2,3,4,5]")))
# 打印出如下字符串的测试编号: "{'case_id':5,'case_title':'登录接口冒烟测试','case_data':'......'}"
print(eval("{'case_id':5,'case_title':'登录接口冒烟测试','case_data':'......'}")["case_id"])  # 5

# 2. zip():聚合打包
list1 = ['name', 'age', 'sex', 'class']
list2 = ['xiaohua', '20', '女', '24']

print(list(zip(list1, list2)))  # [('name', 'xiaohua'), ('age', '20'), ('sex', '女'), ('class', '24')]
print(dict(zip(list1, list2)))  # {'name': 'xiaohua', 'age': '20', 'sex': '女', 'class': '24'}

# 当多个序列打包时按最少元素的长度来打包
list3 = [1, 2, 3]
list4 = ['a', 'b', 'c', 'd']
list5 = ['aa', 'bb', 'cc', 'dd', 'ee']
print(list(zip(list3, list4, list5)))  # [(1, 'a', 'aa'), (2, 'b', 'bb'), (3, 'c', 'cc')]

# 3.isinstance(A,B)  判断A变量的数据类型是否属于B类型
num = 1000
print(isinstance(num, int))  # True

str1 = 'abc'
print(isinstance(str1, int))  # False
print(isinstance(str1, str))  # True

"""
--------------------------------
@Time    :  2022/1/12 - 17:29 
@Author  :  Lee
@File    :  python_basic09 
--------------------------------
"""

# 知识点:字符串的常用方法,常用的API

# 1.len() 求字符串的长度  length
str1 = 'abcdef'
res = len(str1)
print(res)  # 6

# 2.replace(a,b) 查找字符串中的元素,将字符串中的a 替换成 b
str2 = '我们爱学python'
str3 = str2.replace('爱', '热爱')
print(str3)  # 我们热爱学python

str4 = str2.replace('python', '数据库')
print(str4)  # 我们爱学数据库

# 3.find() 查找括号中的元素在字符串中第一次出现的位置,返回int类型
str5 = 'pythonic_python'
res = str5.find('o')
print(res)  # 4

res1 = str5.find('oni')
print(res1)  # 4

res2 = str5.find('z')
print(res2)  # -1 如果字符串中找不到对应的元素,那么返回-1

# 4.join() 拼接()中的每一个元素,但是括号中的内容必须为字符串
a = '*'
b = a.join('12345')
print(b)  # 1*2*3*4*5

a = '--'
b = a.join('123')
print(b)  # 1--2--3
print('@'.join('123'))  # 1@2@3

# 如下字符串,如何去除字符串里的空格
str6 = "dahs klahdh aldh auildh ai;dashjdk;''daskld akl"
str7 = str6.replace(' ', '')
print(str7)

# 5.count()  统计元素在字符串中出现的次数
str8 = 'qwerqwerqwer'
res3 = str8.count('A')
print(res3)  # 0

res4 = str8.count('qw')
print(res4)  # 3

# 6.upper() / lower() 大小写转换
str9 = 'abcdefghijklmnopqrstuvwxyz123'
str10 = str9.upper()
print(str10)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ123

print(str10.lower())  # abcdefghijklmnopqrstuvwxyz123

# 7.isnumeric() 判断字符串是否为纯数字,如果是返回True,否则返回False
str11 = '1234'
print(str11.isnumeric())  # True

str12 = 'a1234'
print(str12.isnumeric())  # False

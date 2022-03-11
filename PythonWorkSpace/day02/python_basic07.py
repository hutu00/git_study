"""
--------------------------------
@Time    :  2022/1/12 - 15:42 
@Author  :  Lee
@File    :  python_basic07 
--------------------------------
"""

"""
本章讲解: str字符串类型
"""

# 知识点1: 字符串的定义、声明的方式
name = 'xiaohua'  # 该行代码声明了一个变量name,并且赋值xiaohua,变量name是字符串类型 str
name1 = "xiaohong"
name2 = '''xiaomei'''
name3 = """xiaolan"""

# 知识点2: 字符串之间可以使用 + 号拼接,结果还是一个字符串
str1 = '今天'
str2 = '天气'
str3 = '很好'
str4 = '很适合学python'
str5 = str1 + str2 + str3 + str4
print(str5)  # 今天天气很好很适合学python  通过拼接四个字符串成为了一个新的字符串

name4 = 'xiaowang'
age = 18
# print(name4 + age)  # 数字不能和字符串拼接
print(name4 + str(age))  # xiaowang18

# 知识点3: 字符串的索引,字符串对每个字符都做了编号,从前往后从0开始,从后往前从-1开始
str6 = '我是个机智的小天才'
print(str6[0])  # 我  []这个代表位置
print(str6[8])  # 才
print(str6[-2])  # 天
# print(str6[9])  # IndexError 下标越界异常

# 知识点4: 字符串的切片(截取)  str[开始下标:结束下标]  前包含,后不包含
print(str6[0:5])  # 我是个机智
print(str6[5:-1])  # 的小天
print(str6[5:-6])  # 没有截取到数据,什么都没打印
print(str6[5:])  # 的小天才  截取了下标从5开始到结束
print(str6[:6])  # 我是个机智的  从下标0开始截取到下标6,但是不包含下标6的元素

# 知识点5: 填充
# 1. format()
str7 = '小花来自{}，年龄{}，{}来上海工作'  # {}用来占位
str8 = str7.format('安徽', 25, '2022年')  # 填充的值要和{}数量对应
print(str8)  # 小花来自安徽，年龄25，2022年来上海工作

# 2. 传统填充方式
# %s 代表填充字符串类型   %d 代表填充整数类型   %f 代表填充浮点数类型
str9 = '小花来自%s,年龄%d,%d年来上海工作,目前年薪%f万' % ('河南', 18, 2022, 19.5)
print(str9)  # 小花来自河南,年龄18,2022年来上海工作,目前年薪19.500000万

# 知识点6:字符串的转义:在python里 \n 代表换行  \t 代表制表符,相当于一个tab
str10 = 'sagjk\ndgsajkdgs\tajlkgdajklsgda'
print(str10)  # 输出的结果就加上了 换行 和 制表符

# 关闭转义:在字符串前面加 r/R
str11 = r'sagjk\ndgsajkdgs\tajlkgdajklsgda'
print(str11)  # sagjk\ndgsajkdgs\tajlkgdajklsgda

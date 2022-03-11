# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2022/1/12-16:06
=============================
"""

# 练习1： 看懂并自己写一遍：统计一串字符串中各元素的数量 比如:"abc129adb12",打印出一个字典 {a:2,b:2,c:1....}
# 要求使用debug调试模式看
"""
# 大概思路就是循环统计每一个元素的数量，但是如果循环的话重复的数据就会被统计多次
# 所以先去重,再循环,这时候我们想到set能够自动去重。
# 循环拿到每一个元素后，求出元素的数量，并且添加到字典中(key为 元素,value为 元素出现的次数)
"""
str1 = "abc129adb12"
set1 = set(str1)
dict1 = {}
print(set1)
for i in set1:
    dict1[i] = str1.count(i)
print(dict1)  # {'c': 1, '9': 1, 'd': 1, 'b': 2, 'a': 2, '1': 2, '2': 2}

# *****************************************************************************

# 练习2： 看懂并自己写一遍 ,求出一串字符串中重复次数最多的元素,要求使用debug调试模式看
# 1、在上边题目的基础上统计出每个元素出现的次数
str1 = "abc129adb12"
set1 = set(str1)
dict1 = {}
for i in set1:
    dict1[i] = str1.count(i)

# 2.再把字典的所有的value值中最大的值拿出来,判断那个key等于该最大值
max_val = max(dict1.values())
print(max_val)

for i, j in dict1.items():
    if j == max_val:
        print('出现次数最多的键是:', i)

"""
--------------------------------
@Time    :  2022/1/12 - 10:24 
@Author  :  Lee
@File    :  python_basic03 
--------------------------------
"""

"""
本章讲解: 注释、命名规则、保留字
"""

# 注释1: 单行注释

'''
注释多行
第二个注释
第三个注释
第四个注释
'''

"""
注释多行
第五个注释
第六个注释
print('hello world')
"""

# 江南逢李龟年
# 作者：杜甫
#
# 岐王宅里寻常见，崔九堂前几度闻。
# 正是江南好风景，落花时节又逢君。

# 多行注释快捷键,选中需要注释的文本,然后Ctrl + /

# 命名规则
# 666 = 'a'  # 不能以数字开头
# and = '123'  # and是保留字，不能当作变量名
# money$aa = 10  # 除了下划线,不推荐使用其它符号作为变量名


# 查看python的保留字
import keyword

print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
 '''

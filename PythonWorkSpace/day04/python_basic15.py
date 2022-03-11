"""
--------------------------------
@Time    :  2022/1/14 - 14:07 
@Author  :  Lee
@File    :  python_basic15 
--------------------------------
"""

"""
本章讲解:条件判断
"""

"""
条件判断分为单分支语句、双分支和多分支语句

单分支语句语法:
if 条件:
    语句块

如果条件成立则执行语句块,反之则不执行语句块
"""

# case1:如果今天天气好,我就晒被子
weather = input("请输入今天的天气:")

if weather == '好':
    print('可以晒被子了')
    print("好开心~")

# case2: 如果今天是周五,明天就不用上课了
date = input("请输入今天是星期几:")

if date == '周五' or date == '星期五' or date == '礼拜五' or date == 'Friday' or date == 'friday' or date == '5':
    print('明天就不用上课了!')

# case2优化
date = input("请输入今天是星期几:")

if date in ['周五', '星期五', '礼拜五', 'Friday', 'friday', '5']:
    print('明天就不用上课了!')

# 模拟Oracle登录
name = input("请输入用户名:")
password = input("请输入密码:")

if name == 'scott' and password == '1234':
    print("恭喜您登录成功")
else:
    print("用户名或密码输入错误,请检查您的输入是否正确")

"""
双分支语句语法:
if 条件:
    语句块1
else:
    语句块2
    
如果条件成立则执行语句块1,其它情况执行语句块2
"""

# case1:如果今天天气好,我就晒被子.天气不好,睡觉
weather = input("请输入今天的天气:")

if weather == '好':
    print('可以晒被子了')
    print("好开心~")
else:
    print('睡觉')

# case2:如果今天是周五或周六,明天不用上课,其他时间正常上课
date = input("请输入今天是星期几:")

if date in ['周五', '周六']:
    print('明天就不用上课了!')
else:
    print('正常上课!')

# 练习:用户从控制台输入一个整数,判断他是奇数还是偶数并且输出
num = int(input("请输入一个整数:"))

# 第一种写法
if num % 2 == 0:
    print('{}是偶数'.format(num))
else:
    print("%d是奇数" % num)

# # 第二种写法
if num % 2:  # 整数取余2只有2个结果,要么是1,要么是0,所以余1时为True,打印是奇数.反之打印偶数
    print("%d是奇数!" % num)
else:
    print("{}是偶数!".format(num))

# 练习:用户输入一个年份,判断是否为闰年(能被4整数但不能被100整除,或者能被400整除)
year = int(input('请输入年份:'))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("{}是闰年!".format(year))
else:
    print("%d是平年!" % year)

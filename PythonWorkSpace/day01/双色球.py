# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/11/21-12:07
=============================
"""
# 规则：**
# 1、双色球是由两种颜色的球（号码）组成,红色球：从1-33号球中，先择6个不重复的号码。
# 2、蓝色球：从1-16号球中，选择1个号码,从而组成的一个七位数的号码组合。
# 3、在显示的时候，红色球按照从小到到的顺序依次显示,用户从控制台输入一注双色球号码。
# 4、与计算机随机生成的双色球号码进行比对,判断用户中了几等奖。

# 一等奖：6+1
# 二等奖：6
# 三等奖：5+1
# 四等奖：5、4+1
# 五等奖：4、3+1
# 六等奖：2+1、1+1、0+1
# 系统随机生成一注双色球号码

import random

# 模拟 用户购买一注双色球号码
user_redballs = []
user_blueball = 0
count = 1
while True:
    if len(user_redballs) == 6:
        break
    user_number = input("请输入第{}个红色号码：".format(count))
    if not user_number.isnumeric():
        print("你输入的不是数字，请重新输入！")
        continue
    user_number = int(user_number)
    if user_number < 1 or user_number > 33:
        print("你输入的数字超出范围，请重新输入！")
        continue
    if user_number in user_redballs:
        print("该数字已经存在，请重新输入！")
        continue
    user_redballs.append(user_number)
    count += 1
user_redballs.sort()

while True:
    if user_blueball != 0:
        break
    user_number = input("请输入蓝色球号码：")
    if not user_number.isnumeric():
        print("你输入的不是数字，请重新输入！")
        continue
    user_number = int(user_number)
    if user_number < 1 or user_number > 16:
        print("你输入的数字超出范围，请重新输入！")
        continue
    user_blueball = user_number
    print("您购买的双色球号码是：{}[{}]".format(user_redballs, user_blueball))

# ***********************模拟彩票中奖号码：生成6个不重复的红色球号码和蓝色号码***********************
# 第一步：制作一个号码池，里面有33个数
number = 1
numbers = []
while number < 34:
    numbers.append(number)
    number += 1

# 第二步：从号码池中取出6个不重复的数字
computer_redballs = []
count = 1
while count <= 6:
    index = random.randint(0, len(numbers) - 1)
    number = numbers[index]
    computer_redballs.append(number)
    del numbers[index]
    count += 1

# 第三步：在显示的时候，按照升序进行显示
computer_redballs.sort()
print("本期中奖号码红色球为：{}".format(computer_redballs))

# 第四步：生成1个蓝色球号码
computer_blueball = random.randint(1, 16)
print("本期中奖号码蓝色球为：{}".format(computer_blueball))

# 第五步：显示计算机生成的双色球号码
print("本期中奖号码为：{}".format(computer_redballs), end="")
print("[{}]".format(computer_blueball))


# ***********************# 中奖判定 ***********************

count = 0
for number in user_redballs:
    if number in computer_redballs:
        count += 1

if count == 6 and user_blueball == computer_blueball:
    print("一等奖")
elif count == 6:
    print("二等奖")
elif count == 5 and user_blueball == computer_blueball:
    print("三等奖")
elif count == 5 or (count == 4 and user_blueball) == computer_blueball:
    print("四等奖")
elif count == 4 or (count == 3 and user_blueball) == computer_blueball:
    print("五等奖")
elif user_blueball == computer_blueball:
    print("六等奖")
else:
    print("没中奖，欢迎下次光临！")

print("程序结束")

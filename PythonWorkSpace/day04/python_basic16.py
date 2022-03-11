"""
--------------------------------
@Time    :  2022/1/14 - 15:34 
@Author  :  Lee
@File    :  python_basic16 
--------------------------------
"""

"""
本章讲解:多分支条件判断
语法:
if 条件1:
    语句块1
elif 条件2:
    语句块2
elif 条件3:
    语句块3
....
[else:
    语句块4]
"""
# 0（初生）-6岁为婴幼儿；7-12岁为少儿；13-17岁为青少年；18-45岁为青年；46-69岁为中年；>69岁为老年
age = int(input("请输入年龄:"))

if 0 < age <= 6:
    print('婴幼儿阶段,好好玩耍')
elif 6 < age <= 12:
    print('少儿阶段,好好学习,天天向上')
elif 12 < age <= 17:
    print('青少年阶段,学习')
elif 17 < age <= 45:
    print('青年阶段,努力拼搏,争取老板明年换车')
elif 45 < age <= 69:
    print('中年阶段,带娃,享受生活')
else:  # 如果以上条件都不满足,执行else的语句块
    print('年华一去不复返,是非成败转头空')

# 自己想个多分支逻辑(至少4个分支)
sal = int(input("请输入年收入:"))

if 0 < sal <= 30000:
    print("贫困家庭")
elif 30000 < sal <= 100000:
    print("低收入家庭")
elif 100000 < sal <= 300000:
    print("小康家庭")
elif 300000 < sal <= 1000000:
    print("中高收入家庭")
elif sal > 1000000:
    print("高收入家庭")
else:
    print("乞丐")

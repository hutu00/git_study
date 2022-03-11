"""
--------------------------------
@Time    :  2022/1/17 - 10:22 
@Author  :  Lee
@File    :  python_basic18 
--------------------------------
"""

"""
1.while循环使用else语句: 在while...else,当循环判断条件为False的时候执行else语句块
2.终止循环使用break
3.跳过本轮循环使用continue
4.死循环
"""

'''
案例1:
i = 1
while i <= 100:
    print(i)

案例2:
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
        i += 1
'''

i = 1
while i <= 10:
    print(i)
    i += 1
else:  # 循环结束后,执行else语句块
    print("循环结束")

print('===' * 50)

i = 0
while i <= 10:
    i += 1
    if i == 5:
        # break  # 打印结果: 1,2,3,4 Hello 当i==5的时候整个循环终止
        continue  # 打印结果: 1,2,3,4,6,7,8,9,10,11 Hello 当i==5时候,跳过本轮循环，不执行下面的代码,执行下轮循环
    print(i)

print("Hello")

count = 0
while True:
    name = input("请输入用户名:")
    password = input("请输入密码:")
    count += 1

    if name == "scott" and password == "1234":
        print("登录成功")
        break
    if count < 3:
        print("您输入的用户名或密码错误!")
        print("您还有{}次机会!".format(3 - count))
        continue
    if count == 3:
        print("您输入的错误次数过多,请稍后重试!")
        break

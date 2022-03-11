"""
--------------------------------
@Time    :  2022/1/24 - 14:44 
@Author  :  Lee
@File    :  thread01 
--------------------------------
"""

"""
进程: 一个应用是由一个或者多个进程来实现的
线程: 一个进程包含多个线程

多线程并发: 多个线程同时执行任务
"""

import time


def a():
    print('我要吃饭了!')
    time.sleep(1)  # 让当前等待1s
    print('饭吃完了~')


def b():
    print("找对象聊聊天~")
    time.sleep(1)  # 让当前等待1s
    print("聊完了~")


def c():
    print("我要追星,我要上微博给爱豆点赞!")
    time.sleep(1)  # 让当前等待1s
    print("追星成功了~")


start_time = time.time()  # 获取当前时间戳
a(), b(), c()  # 调用三个函数
end_time = time.time()
print("总耗时:{}".format(end_time - start_time))

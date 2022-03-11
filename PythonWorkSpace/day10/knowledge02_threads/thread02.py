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
import threading
import time


def a1():
    print('我不吃饭了!')
    time.sleep(1)  # 让当前等待1s
    print('以后都不吃了~')


def b1():
    print("找不到对象~")
    time.sleep(1)  # 让当前等待1s
    print("再努努力!")


def c1():
    print("再也不追星了!")
    time.sleep(1)  # 让当前等待1s
    print("爱豆跑早操去了~")


start_time = time.time()  # 获取当前时间戳

t1 = threading.Thread(target=a1)
t2 = threading.Thread(target=b1)
t3 = threading.Thread(target=c1)

t1.start()  # 启动线程
t2.start()
t3.start()

end_time = time.time()
print("总耗时:{}".format(end_time - start_time))

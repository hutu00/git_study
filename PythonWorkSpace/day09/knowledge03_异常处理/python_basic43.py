"""
--------------------------------
@Time    :  2022/1/21 - 15:45 
@Author  :  Lee
@File    :  python_basic43 
--------------------------------
"""

"""
1.我们可以使用raise 自己触发异常   raise [Exception[,args,[traceback]]]
2.自定义异常:
    实际的工程项目中,我们有时候需要定义一个区别于系统的异常类,还好python为我们提供了一个可以自己定义异常类的方法，来看下面的代码
"""

num = int(input("请输入0-100的整数:"))
if not 0 <= num <= 100:
    raise Exception('输入了无效的分数!')  # 主动抛异常
elif 0 <= num < 60:
    print('不及格')
else:
    print("及格")


# 自定义异常
class NotValidNumber(Exception):  # 异常类必须继承Exception类
    pass


num = int(input("请输入0-100的整数:"))
if not 0 <= num <= 100:
    raise NotValidNumber('输入了无效的分数!')  # 主动抛异常
elif 0 <= num < 60:
    print('不及格')
else:
    print("及格")

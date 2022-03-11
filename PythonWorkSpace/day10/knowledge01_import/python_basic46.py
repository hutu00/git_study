"""
--------------------------------
@Time    :  2022/1/24 - 14:22 
@Author  :  Lee
@File    :  python_basic46 
--------------------------------
"""

# 使用两种方法 引入python_basic27模块下的judge方法并调用
import day07.python_basic27 as pb

print(pb.judge(10))  # 10是偶数

from day07.python_basic27 import judge

print(judge(15))  # 15是奇数

# 使用两种方法 引入python_basic33模块下的Emp类并新建实例对象调用方法
import day08.python_basic33 as pb3

emp01 = pb3.Emp()
print(emp01.year_sal())  # 31200

from day08.python_basic33 import Emp

emp02 = Emp()
print(emp02.fine(10))  # 1181.818181818182

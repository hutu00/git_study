"""
--------------------------------
@Time    :  2022/1/12 - 14:38 
@Author  :  Lee
@File    :  python_basic06 
--------------------------------
"""

"""
本章讲解:运算符
"""

# 知识点1: 算术运算符 + - * /  %(取余)  //(取整)  **(幂等)
print(10 + 20)  # 30
print(10 - 20)  # -10
print(10 * 20)  # 200
print(20 / 10)  # 2.0  除法运算总是会返回一个浮点数

print(1 % 2)  # 1
print(2 % 3)  # 2
print(10 % 20)  # 10
print(6 % 3)  # 0
print(10 % 3)  # 1
print(20 % 6)  # 2
print(156453 % 2)  # 1
# 小数对大数取余,余小的
# 所有奇数对2取余都是1,所有偶数对2取余都是0

print(2 ** 3)  # 2的3次方  2*2*2  8

print(10 // 20)  # 0
print(25 // 2)  # 12
print(-25 // 2)  # -13  取整的规则是向下取整

# 知识点2: 赋值运算符  =  +=  -=  *=  /=  **=  %=  //=
a = 10
a += 1  # 相当于 a = a+1
print(a)  # 11

a -= 1  # 相当于 a = a-1
print(a)  # 10

a *= 2  # 相当于 a = a*2
print(a)  # 20

a /= 2  # 相当于 a = a/2
print(a)  # 10.0

a = 5
a //= 2  # 相当于 a = a//2
print(a)  # 2

a %= 2  # 相当于 a = a%2
print(a)  # 0

a = 5
a **= 3  # 相当于 a = a ** 3
print(a)  # 125

# 知识点3: 比较运算符  >  <  >=  <=  !=(不等于)  ==(相等)  结果只能是 True 或 False
a = 20
b = 10
print(a == b)  # False
print(a < b)  # False
print(a >= b)  # True

# 知识点4: 逻辑运算符   and(全真为真)   or(全假为假)   not(取反)
# and(全真为真): (条件A　and 条件B)两个条件同时成立,结果是成立
# or(全假为假): (条件A　or 条件B)两个条件同时不成立,结果是不成立
print(a > 0 and b > 0)  # True
print(a < 0 and b > 0)  # False
print(a < 0 or b < 0)  # False
print(a > 0 or b < 0)  # True
print(a < 0 or (a < 0 or b > 0))  # True
print(not (1 > 0))  # False

# 知识点5: 成员运算符   in(在指定序列寻找指定值,找到返回True,否则返回False)
# not in(在指定序列寻找指定值,找不到返回True,否则返回False)
str1 = 'xiaohua'
print('x' in str1)  # True
print("x" not in str1)  # False

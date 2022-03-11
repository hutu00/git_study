# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/6-15:06
=============================
"""
# 练习1:

# 创建一个空列表,名称为numbers
numbers = []
# 添加 1,2,3,6,2,4,2,4 添加到该列表中。
numbers.extend((1, 2, 3, 6, 2, 4, 2, 4))
print(numbers)

# 将下标为3的位置的值修改成 99
numbers[3] = 99
print(numbers)

# 根据下标值删除下标为4的数据
numbers.pop(4)
print(numbers)

# 一次删除列表中所有值为2的元素
numbers.remove(2)
print(numbers)

# 对该列表进行反转
numbers.reverse()
print(numbers)

# 对反转后的列表分别进行降序和升序排列
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# 统计该列表的和
print(sum(numbers))

# 统计出元素2出现的次数
print(numbers.count(2))

# 统计77是否在元素中
print(77 in numbers)

# 练习：将 [1,2,1,2,3,4,5] 中重复的元素进行去除重复，去重后进行排序,转换为一个字符串
list2 = [1, 2, 1, 2, 3, 4, 5]
list1 = list(set(list2))
list1.sort(reverse=True)
print(str(list1))

# 练习题2：
data = {"code": 1000, "msg": "登录成功",
        "token": "MTYxMDYyMTA5Mi40NTQwMDAyOmRlZjFjNDlkNzZhMWJhMmM5ZGQzMjEwY2Q0NTI4ODgzODlkZjdjYTc="
        }

# 1、获取token对应的值。
print(data["token"])
# 2、为data字典添加一组数据,status=200
data["status"] = 200
print(data)
# 3、获取该字典所有的key。
print(list(data.keys()))
# 4、获取该字典的所有键值对,转换为列表,并且通过下标获取该列表中token对应的值。
print(list(data.items())[2][1])

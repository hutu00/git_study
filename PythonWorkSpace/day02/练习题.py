# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/6-15:06
=============================
"""
# 练习1：填空题

'''
我们经常会在论坛上发现,很多敏感字符用XXX来做了替换,我们可以进行模拟
用户从控制台输入一个带 滚的字符串,将字符串中的 滚字替换为X,并且将替换后的字符串打印出来。
'''
comment = input('请输入评论:')
new_comment = comment.replace('滚', 'X')
print('和谐评论后的结果是:{}'.format(new_comment))

# 练习2：苦思冥想题
'''
截取返回json类型的msg的值：比如: {"rescode":"200","msg":"登录成功"} 中的登录成功
注意： msg的值的长度可能会发生变化
'''
json_code = '{"rescode": "200", "msg": "登录成功"}'
b_index = json_code.find('msg')  # 返回msg出现的位置
e_index = json_code.find('}')  # 返回}出现的位置
msg = json_code[b_index + 5:e_index]  # 通过切片进行截取
print(msg)

# 练习3：苦思冥想题
'''
用户从控制台输入一组手机号,判断是否为纯数字,并且长度是否为11位,
1、如果是纯数字并且长度为11位，计算出 则打印出8和6出现的次数总和。
2、如果不是则提示输入的手机号不正确。
'''
phone_number = input('请输入手机号:')
is_number = phone_number.isnumeric()  # 判断手机号是否为纯数字,用 is_number保存判定结果
is_eleven_lenth = len(phone_number) == 11  # 判断手机号是否为11位,用 is_eleven_lenth 存放判定结果

if is_number and is_eleven_lenth:  # 判断是否符合条件,如果符合执行如下代码
    count6 = phone_number.count('6')  # 获取 6出现的次数
    count8 = phone_number.count('8')  # 获取 8出现的次数
    print('6和8出现的总数为:%d' % (count6 + count8))  # 打印出 6和8出现的总次数
else:
    print('输入的手机号格式不正确')

# # 练习4: 用户输入一个年龄，如果年龄是为数字,并且大于0,小于18岁，打印出"未成年",反之打印"成年"
age = input('请输入年龄:')
if age.isnumeric() and 18 > int(age) > 0:
    print('未成年!')
else:
    print('成年!')

# # 练习5: 自动判分系统: 一个题目ABCD四个选项
# # 1、如果用户输入的不是ABCD，则给出提示,
# # 2、该题目只有D正确，根据判定用户输入的答案是否正确。
user_input = input('请输入答案:')
if user_input not in "ABCD":  # 1、先判定输入的内容是否为 ABCD中的选项
    print('请输入正确的信息！')
# 2、判定用户输入的是否为D
if user_input == "D":
    print('答案正确！')
else:
    print('答案错误')

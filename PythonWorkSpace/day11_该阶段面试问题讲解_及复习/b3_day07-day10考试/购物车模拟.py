# -- coding:utf-8 --
"""
============================
   Author:liucl
   date: 2021/12/9-16:43
=============================
"""


# 创建一个购物车条目类,用来存储 购物车中的一条信息: 商品名称，商品价格，商品数量
class Item:
    def __init__(self, goods_id, goods_name, goods_price, goods_count):
        self.goods_id = goods_id  # 商品id
        self.goods_name = goods_name  # 商品名称
        self.goods_price = goods_price  # 商品单价
        self.goods_count = goods_count  # 商品数量


# 创建一个购物车类,该类属性有 购物车编号、购物车所属用户名、商品条目列表
class ShoppingCart:
    def __init__(self, cart_id, cart_user):
        self.cart_id = cart_id
        self.cart_user = cart_user
        self.cart_items = []  # 创建购物车类的时候，自动创建一个空的列表属性。

    # 实例方法1:为购物车中添加商品,用购物车对象调用该方法
    def add_item(self, item):
        self.cart_items.append(item)  # 该方法将传入的商品条目添加到购物车对象的商品列表中。

    # 实例方法2: 删除购物车中的商品条目,用购物车对象调用该方法
    def del_item(self, goods_id):  # 传入商品编号,该方法会把该购物车中的商品进行删除
        for i in self.cart_items:  # 这行代码是干什么的？回答：遍历购物车列表中的所有商品实例对象
            if i.goods_id == goods_id:  # 这行代码的作用? 回答:判断购物车列表中的所有商品对象的编号是否和传入的编号一致
                self.cart_items.remove(i)  # 这行代码的作用? 回答:如果符合条件则删除购物车列表中的商品对象

    # 实例方法3 设计一个方法，该方法返回购物车中的商品条目数
    def goods_num(self):
        return len(self.cart_items)

    # 实例方法4 设计一个方法, 该方法返回购物车中所有商品的总价格（提示使用循环累加计算出总金额并且返回）
    def total_price(self):
        count = 0
        for i in self.cart_items:
            count += i.goods_price * i.goods_count
        return count


# 创建ShoppingCart类的一个对象,并且创建出三个条目对象，将创建好的条目添加到ShoppingCart类中
sc01 = ShoppingCart(10001, 'xiaohua')  # 创建购物车对象
item01 = Item(1001, '西施1号壶', 69.5, 2)  # 创建条目对象
item02 = Item(1002, '西施2号壶', 80.5, 1)
item03 = Item(1003, '西施3号壶', 30.5, 3)
# 添加商品条目到购物车
sc01.add_item(item01)
sc01.add_item(item02)
sc01.add_item(item03)
# 调用方法3，打印出购物车中的条目数
print(sc01.goods_num())
# 调用方法4，打印出结算一共需要多少钱
print(sc01.total_price())
# 调用删除方法删除1003商品
sc01.del_item(1003)
# 调用方法4, 打印出删除商品后一共需要多少钱。
print(sc01.total_price())

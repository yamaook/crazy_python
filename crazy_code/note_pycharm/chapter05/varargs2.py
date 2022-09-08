"""
    5.2.4逆向参数收集
"""


def test(name, message):
    print("用户名：", name)
    print("欢迎消息:", message)


my_list = ['孙悟空', '欢迎来到疯狂软件']
test(*my_list)


def foo(name, *nums):
    print("name参数:", name)
    print("nums参数：", nums)


my_tuple = (1, 2, 3)
# 即便是带有参数收集参数，也需要用加星号
foo('fkit', *my_tuple)

foo(*my_tuple)
foo(my_tuple)


def bar(book, price, desc):
    print(book, "真本书的价格是：", price)
    print("描述信息", desc)


my_dict = {'price': 89, 'book': "疯狂Python讲义", 'desc': '这是一本系统全面的python学习图书'}
bar(**my_dict)


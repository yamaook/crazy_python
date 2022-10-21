"""
    5.2.3参数收集
"""


def test(a, *books):
    print(books)
    for b in books:
        print(b)
    print(a)


test(5, "疯狂ios讲义", "疯狂Android讲义")


# 定义支持参数收集的函数
def test2(*books, num):
    print(books)
    for b in books:
        print(b)
    print(num)


# num必须使用关键字实参，否则认为所有参数都是传给books的
test2("疯狂ios讲义", "疯狂Android讲义", num=20)


def test_keyword(x, y, z=3, *books, **scores):
    print(x, y, z)
    print(books)
    print(scores)


test_keyword(1, 2, 3, "疯狂ios讲义", "疯狂Android讲义", 语文=89, 数学=94)


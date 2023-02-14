"""
    8.4 生成器
        迭代器和生成器区别：
            迭代器：先定义迭代器类，然后创建实例来创建迭代器。
            生成器：先定义一个包含yield语句的函数，然后通过调用该函数创建生成器。

        8.4.1 创建生成器
            1、定义一个包含yield语句的函数
            2、调用第一步创建的函数得到生成器。
            3、yield cur语句的作用：
                1、每次返回一个值
                2、冻结执行，程序每次执行到yield语句时就会被暂停。
                    当程序调用next()函数，程序才会继续向下执行。
            4、调用包含yield语句的函数不会立即执行，只会返回一个生成器。
            5、list() tuple()可以将生成器变成列表或者元组
            6、for循环生成器推导式也可以创建生成器。
"""


def test(val, step):
    print("-------函数开始执行--------")
    cur = 0
    for i in range(val):
        cur += i * step
        yield cur


# 执行函数返回生成器，并没有执行函数
t = test(10, 2)
print("================")
print(next(t))
print(next(t))

for ele in t:
    print(ele, end=' ')
print()
# 一个生成器，只能用一次
t = test(10, 1)
print(list(t))
t = test(10, 3)
print(tuple(t))

"""
    8.4.2 生成器的方法
        1、外部程序通过send方法发送数据。
        2、生成器函数通过yield语句接收数据。
        3、使用send第一次获取生成器值，只能传入None参数。
        4、如果使用next获取生成器生成的下一个值，yield语句返回None。
        5、只有生成器冻结，send才能发送数据，所以获取第一个值时候无法用send发送数据。
        6、close:停止生成器，关闭之后程序就不能获取生成器的下一个值。
            throw:在yield语句内引发一个异常。
"""


def square_gen(val):
    i = 0
    out_val = None
    while True:
        out_val = (yield out_val ** 2) if out_val is not None else (yield i ** 2)
        if out_val is not None: print("=====%d" % out_val)
        i += 1


sg = square_gen(5)
# 第一次调用send只能传入None
print(sg.send(None))
print(next(sg))
print('-------------')
print(sg.send(9))
print(next(sg))
# sg.throw(ValueError)
sg.close()
print(next(sg))

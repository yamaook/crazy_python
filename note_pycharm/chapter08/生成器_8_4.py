"""
    8.4.1 创建生成器
        通过调用函数来创建生成器
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

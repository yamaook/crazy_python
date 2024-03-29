"""
5.5 局部函数与lambda表达式
    函数：命名，方便复用的代码块
    lambda表达式：功能更灵活的代码块

    5.5.1 回顾局部函数：
        局部函数的函数名作用太有限，lambda表达式简化局部函数的写法。
    5.5.2 使用lambda表达式代替局部函数
        lambda表达式只能是单行表达式
        本质：匿名的、单行函数体的函数,就是一个简化的函数。

        map工具函数
"""


def get_math_func(tp):
    if tp == "square":
        return lambda n: n * n
    elif tp == "cube":
        return lambda n: n * n * n
    else:
        return lambda n: (1 + n) * n / 2


math_func = get_math_func("square")
print(math_func(5))
math_func = get_math_func("cube")
print(math_func(5))
math_func = get_math_func("other")
print(math_func(5))

x = map(lambda x: x ** 2, range(8))
print([e for e in x])
y = map(lambda x: x ** 2 if x % 2 == 0 else 0, range(8))
print([e for e in y])

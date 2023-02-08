"""
    5.4.2 使用函数类型参数作为函数形参
        可以动态改变被调用函数的部分代码。
"""


def map_test(data, fn):
    return [fn(e) for e in data]


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


def factorial(n):
    result = 1
    for index in range(2, n + 1):
        result *= index
    return result


data = [3, 4, 9, 5, 8]
print("原数据", data)
print(map_test(data, square))
print(map_test(data, cube))
print(map_test(data, factorial))
print(type(map_test))

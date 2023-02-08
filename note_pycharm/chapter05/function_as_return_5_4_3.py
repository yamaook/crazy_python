"""
    5.4.3 使用函数作为返回值
"""


def get_math_func(tp):
    def square(n):
        return n ** 2

    def cube(n):
        return n ** 3

    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    # 返回局部函数
    if tp == "square":
        return square
    elif tp == "cube":
        return cube
    else:
        return factorial


math_func = get_math_func("cube")
print(math_func(5))
math_func = get_math_func("square")
print(math_func(5))
math_func = get_math_func("other")
print(math_func(5))

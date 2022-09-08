"""
    5.1.5 递归函数
        在一个函数体内调用自身，被称为函数递归。
        递归一定要向已知方向进行
"""


def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    return 2 * fn(n - 1) + fn(n - 2)


def fn2(n):
    if n == 20:
        return 1
    elif n == 21:
        return 4
    return fn2(n + 2) - 2 * fn2(n + 1)


print(fn(10))
print(fn2(10))

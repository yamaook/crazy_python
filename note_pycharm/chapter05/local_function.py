"""
    5.3局部函数
        全局函数：全局范围内定义的
        局部函数：函数体内定义的

    nonlocal：声明访问当前函数所在函数内的局部变量
    global:声明访问全局变量
"""


# 局部函数的使用
def get_math_func(type, nn):
    def square(n):
        return n ** 2

    def cube(n):
        return n ** 3

    def factorial(n):
        result = 1
        for index in range(2, n + 1):
            result *= index
        return result

    if type == "square":
        return square(nn)
    elif type == "cube":
        return cube(nn)
    else:
        return factorial(nn)


print(get_math_func("square", 3))
print(get_math_func("cube", 3))
print(get_math_func("", 3))


# nonlocal的使用
def foo():
    name = 'charlie'

    def bar():
        nonlocal name
        print(name)
        name = '孙悟空'

    bar()
    print(name)


foo()

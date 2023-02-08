"""
    5.4 函数的高级内容
        函数本身就是一个function对象，可以用于赋值、其他函数参数或者返回值。


    5.4.1 使用函数变量
            函数赋值给变量，可以通过变量调用函数。
            使用函数变量的好处是让程序更加灵活

"""


# 一个乘方函数
def pow_test(base, exponent):
    result = 1
    for i in range(1, exponent + 1):
        result *= base
    return result


my_fun = pow_test
print(my_fun(3, 4))


# 定义计算面积的函数
def area_test(width, height):
    return width * height


my_fun = area_test
print(my_fun(3, 4))

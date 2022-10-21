"""
    5.2.2 参数默认值
        默认形参：定义函数时，要求带默认值的参数必须在没有默认值的参数之后
"""


def say_hi(name="孙悟空", message="欢迎来到疯狂"):
    print(name, "你好")
    print("消息是：", message)


# 全部使用默认值
say_hi()
# 后使用默认值
say_hi("白骨精")
# 都不使用默认值
say_hi("白骨精", "欢迎学习python")
# 前使用默认值（这个使用了关键字参数）
say_hi(message="欢迎学习python")


# 定义函数时，要求带默认值的参数必须在没有默认值的参数之后
def print_triangle(char, height=5):
    for i in range(1 + height):
        for j in range(height - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print(char, end='')
        print()


print_triangle('@', 6)
print_triangle('#', height=7)
print_triangle(char="*")

"""
    5.1.2定义和调用函数
        函数：执行特定任务的一段代码。
        函数名：合法的标识符即可。建议由一个或多个有意义的单词组成，字母全小写，下划线分隔单词。

"""


def my_max(x, y):
    # z = x if x > y else y
    # return z
    return x if x > y else y


def say_hi(name):
    print("========正在执行say_hi()函数====")
    return name + ",您好！"


a = 6
b = 9
result = my_max(a, b)
print("result:", result)
print(say_hi("孙悟空"))

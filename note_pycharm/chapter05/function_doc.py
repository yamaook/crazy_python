"""
    5.1.3 为函数提供说明文档
"""


def my_max(x, y):
    """
    获取两个数值之间较大数的函数
    :param x: 参数1
    :param y: 参数2
    :return: 返回x,y两个参数之间较大的那个数
    """
    return x if x > y else y


help(my_max)
print(my_max.__doc__)

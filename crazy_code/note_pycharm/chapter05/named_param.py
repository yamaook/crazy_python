"""
    5.2 函数的参数
        实际参数
            位置参数：按照形参位置传入的参数
            关键字参数：根据参数名传入参数值
        形式参数


        注意：混合使用时，关键字参数必须位于位置参数之后。关键字参数后面只能是关键字参数。

"""


def girth(width, height):
    print("width:", width)
    print("height:", height)
    return 2 * (width + height)


# 位置参数
print(girth(3.5, 4.8))
# 关键字参数
print(girth(width=3.5, height=4.8))
# 关键字参数可以不按照形参顺序
print(girth(height=4.8, width=3.5))
# 部分位置参数，部分关键字参数
print(girth(3.5, height=4.8))

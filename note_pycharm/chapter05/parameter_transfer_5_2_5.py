"""
    5.2.5 函数的参数传递机制
        python中函数的参数传递机制都是值传递。

"""


# 可变类型的参数传递效果
def swap(dw):
    dw['a'], dw['b'] = dw['b'], dw['a']
    print("在swap里a的值:", dw['a'], "b的值:", dw['b'])
    dw = None


dw = {'a': 6, 'b': 9}
swap(dw)
print("交换结束后，a的值:", dw['a'], "b的值:", dw['b'])

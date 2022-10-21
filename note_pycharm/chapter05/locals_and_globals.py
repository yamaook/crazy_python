"""
    5.2.6 变量作用域
        局部变量：函数里可访问。
        全局变量：可以在所有函数内访问。
        工具函数：
            获取指定范围内的变量字典：
            globals():返回全局范围内所有变量组成的"变量字典"
            locals():返回当前局部范围内所有变量"变量字典"
            vars(object):获取指定对象范围内所有变量组成的"变量字典"。如不传参，和locals()作用相同

        globals 和 locals 区别：
            1、如果在全局范围内调用locals()，和globals()效果一样。
            2、globals和locals获取的全局范围内的变量字典，可以修改并且会改变全局变量本身。
               但修改locals获取的局部范围内的变量字典不影响局部变量。
"""


def test():
    age = 20
    name = 'haha'
    print(age)
    # 访问局部变量字典
    print(locals())
    # 通过局部变量字典访问age
    print(locals()['age'])
    # 通过局部变量字典改变age
    locals()['age'] = 12
    print('xxx', age)
    # 修改全局变量
    globals()['x'] = 19


test()
# print(x)  # globals修改成功
x = 5
y = 20
print(globals())
print(locals())
print(x)
# 通过全局变量字典访问x
print(globals()['x'])
# 通过全局变量字典修改x
globals()['x'] = 39
print(x)
# 通过locals获取全局变量字典，从而修改x
locals()['x'] = 99
print(x)

# 局部变量遮蔽全局变量
name = 'charlie'


def test2():
    # print(name)#UnboundLocalError: local variable 'name' referenced before assignment
    # 解决遮蔽问题方法1：访问被遮蔽的全局变量用globals()
    # print(globals()['name'])
    # 解决遮蔽问题方法2 :申明全局变量
    global name
    print(name)
    name = '孙悟空'


test2()
print(name)

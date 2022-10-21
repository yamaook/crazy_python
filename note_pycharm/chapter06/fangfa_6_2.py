"""
    6.2方法
"""


# 6.2.1 类调用实例方法

# 类相当于一个命名空间
def foo():
    print("全局空间的foo方法")


bar = 20


class Bird:
    def foo():
        print("Bird空间的foo方法")

    bar = 200


foo()
print(bar)
Bird.foo()
print(Bird.bar)


# 通过类调用实例方法
class User:
    def walk(self):
        print(self, "正在走")


u = User()
User.walk(u)
# 并不是必须绑定对象
User.walk('fkit')


# 6.2.2 类方法和静态方法
class Bird:
    # 区别类方法第一个参数会自动绑定到类本身
    @classmethod
    def fly(cls):
        print('类方法fly', cls)

    @staticmethod
    def info(p):
        print("静态方法info", p)


Bird.fly()
Bird.info("crazyit")
b = Bird()
b.fly()
b.info('fkit')


# 6.2.3 函数装饰器
def funA(fn):
    print('A')
    fn()
    return 'fkit'


@funA
def funB():
    print('B')


# funB指向了返回值
print(funB)


# 一个更复杂的函数装饰器
def foo(fn):
    def bar(*args):
        print('====1====', args)
        n = args[0]
        print('===2===', n * (n - 1))
        print(fn.__name__)
        print('*' * 15)
        return fn(n * (n - 1))

    return bar


@foo
def my_test(a):
    print('===my_test函数', a)


print(my_test)
my_test(10)
my_test(6, 5)


# 面向切面编程
def auth(fn):
    def auth_fn(*args):
        print("模拟权限检查")
        fn(*args)

    return auth_fn


@auth
def test(a, b):
    print("执行test函数，参数a:%s,参数b:%s" % (a, b))


test(20, 15)


# 6.2.4 类命名空间
class Item:
    print('正在定义item类')
    for i in range(10):
        if i % 2 == 0:
            print('偶数', i)
        else:
            print('奇数', i)


# 代码放在全局命名空间和类命名空间的区别
global_fn = lambda p: print('执行lambda表达式,p参数', p)


class Category:
    cate_fn = lambda p: print('执行lambda表达式,p参数:', p)


global_fn('fkit')
c = Category()
c.cate_fn()

"""
    命名空间的概念：
        命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。
        命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，
        所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
"""

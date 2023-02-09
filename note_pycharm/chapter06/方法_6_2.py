"""
    6.2方法
        1、python的方法其实也是函数

        6.2.1 类也能调用实例方法
            1、python类就像命名空间，定义方法和变量时，其实和之前定义变量、函数没有太大不同，
                所以可以用类调用实例方法。
            2、python类可以调用实例方法，但不会自动绑定self参数值，必须为self传入方法调用者。

        6.2.2 类方法与静态方法
            推荐使用类调用这些方法，也可以用对象调用。
            1、类方法：自动绑定第一个参数cls到类本身。@classmethod
            2、静态方法：静态方法不会自动绑定参数。@staticmethod

        6.2.3 @函数装饰器
            1、staticmethod、classmethod都是python的内置函数
            2、A函数装饰B函数的过程：
                1、将B函数名作为参数传给A函数。
                2、将B函数名替换成1的返回值。
            3、意义：
                面向切面编程：在被修饰函数之前、之后、抛出异常后增加某种处理逻辑的方式。

        6.2.4 再论类命名空间
            1、python的类就像命名空间，python程序默认处于全局命名空间内，类体则处于类命名空间内。
            2、如果放一般执行语句，放在类命名空间与全局空间并没太大区别。
                但如果在这两个空间分别定义了变量或者函数，那就有区别了，
                    类里面的函数是实例方法会自动绑定第一个参数，而全局空间的函数参数不会自动绑定。


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

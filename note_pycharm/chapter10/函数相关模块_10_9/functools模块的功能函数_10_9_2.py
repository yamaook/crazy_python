"""
    10.9.2 functools模块的功能函数
        主要包含了一些函数装饰器和便捷的功能函数
"""
from functools import *

print(reduce(lambda x, y: x + y, range(5)))
print(reduce(lambda x, y: x + y, range(6)))
print(reduce(lambda x, y: x + y, range(6), 10))
print('--------------------')


@total_ordering
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'User[name=%s]' % self.name

    def _is_valid_operand(self, other):
        return hasattr(other, 'name')

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.name.lower() == other.name.lower()

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.name.lower() < other.name.lower()


def old_cmp(u1, u2):
    return len(u1.name) - len(u2.name)


my_data = [User('Kotlin'), User('Swift'), User('Go'), User('Java')]
my_data.sort(key=cmp_to_key(old_cmp))
print(my_data)
print('----------------')


@lru_cache(maxsize=32)
def factorial(n):
    print('计算%d的阶乘' % n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# 只有这行会计算，然后缓存
print(factorial(5))
print(factorial(3))
print(factorial(5))

print('--------------------')
print(int('12345'))
basetwo = partial(int, base=2)
basetwo.__doc__ = '将二进制形式的字符串转换为整数'
print(basetwo('10010'))
print(int('10010', 2))

print('-------partialmethod为类中方法参数绑定值------------')


class Cell:
    def __init__(self):
        self.__alive = False

    @property
    def alive(self):
        return self.__alive

    def set_state(self, state):
        self.__alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)


c = Cell()
print(c.alive)
c.set_alive()
print(c.alive)
c.set_dead()
print(c.alive)

print('-------------@total_ordering类装饰器--------------------')

print(User.__gt__)
print('-------------@singledispatch函数装饰器--------------------')


@singledispatch
def test(arg, verbose):
    if verbose:
        print('默认参数为：', end=' ')
    print(arg)


@test.register(int)
def _(argu, verbose):
    if verbose:
        print('整形参数为：', end=' ')
    print(argu)


@test.register(list)
def _(argb, verbose):
    if verbose:
        print('列表中所有元素为:')
    for i, elem in enumerate(argb):
        print(i, elem, end='  ')


def nothing(arg, verbose=False):
    print('None参数')


test('PYthon', True)
test(20, True)
test([20, 10, 16, 30, 14], True)
print('\n----------------------------')
test.register(type(None), nothing)
test(None, True)
print('\n----------------------------')
from decimal import Decimal


@test.register(float)
@test.register(Decimal)
def test_num(arg, verbose=False):
    if verbose:
        print('参数的一半为：', end=' ')
    print(arg / 2)


test(1.2, True)
print(test.dispatch(float) is test_num)
print(test.dispatch(Decimal) is test_num)
print(test is test_num)
print('\n----------------------------')
print(test.registry.keys())
print(test.registry[int])
print('\n------------wraps 和 update_wrapper----------------')
"""
    让包装函数的信息，和被包装函数的一致。
    例如下面的：
    wrapper函数信息，完全和test函数的一致
"""


def fk_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('调用被装饰函数')
        return f(*args, **kwargs)

    return wrapper


@fk_decorator
def test():
    """
    test 函数的说明信息
    """
    print('执行test函数')


test()
print(test.__name__)
print(test.__doc__)

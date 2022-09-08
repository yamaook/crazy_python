"""
    6.6 python的动态性
"""

"""
    6.6.1 动态属性与__slots__
"""


# 为类动态添加方法
class Cat:
    def __init__(self, name):
        self.name = name


def walk_func(self):
    print("%s满满地走过一片草地" % self.name)


d1 = Cat('Garfield')
d2 = Cat('Kitty')
Cat.walk = walk_func

d1.walk()
d2.walk()


# 限制实例动态添加属性和方法
class Dog:
    __slots__ = ('walk', 'age', 'name')

    def __init__(self, name):
        self.name = name

    def test():
        print("预先定义的test方法")


d = Dog('Snoopy')
from types import MethodType

d.walk = MethodType(lambda self: print("%s正在慢慢地走" % self.name), d)
d.age = 5
d.walk()
# d.foo = 30 #不允许实例动态添加
Dog.bar = lambda self: print('abc')
d.bar()


# 对该类派生出来的子类无限制
class GunDog(Dog):
    # 如果要限制子类实例动态添加属性和方法，则也定义该属性，但此时限制的是父类和子类的和
    __slots__ = ('speed')

    def __init__(self, name):
        super().__init__(name)

    pass


gd = GunDog('Puppy')
gd.speed = 90
gd.walk = 8
print(gd.speed)

"""
    6.6.2 使用type()函数定义类
"""


class Role:
    pass


r = Role()
print(type(r))
print(type(Role))


# type(）函数动态创建类
def fn(self):
    print("fn函数")


Dog = type('Dog', (object,), dict(walk=fn, age=6))
d = Dog()
print(type(d))
print(type(Dog))
d.walk()
print(d.age)

"""
    6.3.3 使用metaclass
"""


class ItemMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['cal_price'] = lambda self: self.price * self.discount
        print(attrs)
        return type.__new__(cls, name, bases, attrs)


class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '__discount')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount = discount


class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '__discount')

    def __init__(self, price):
        self.price = price

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        self.__discount = discount


b = Book('疯狂Python讲义', 89)
b.discount = 0.76
print(b.cal_price())
cp = CellPhone(2399)
cp.discount = 0.85
print(cp.cal_price())

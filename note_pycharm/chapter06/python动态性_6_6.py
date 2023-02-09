"""
    6.6 python的动态性
        动态语言特征：类、对象的属性和方法都可以动态增加和修改。

        6.6.1 动态属性与__slots__
            1、为类动态添加方法时不需要使用MethodType进行包装，该函数的第一个参数会自动绑定。
            2、隐患：定义好的类，完全有可能在后面被其他程序修改。带来了一些不确定性。
            2、__slots__属性：
                1、值是元组，列出了该类的实例允许动态添加的所有属性名和方法名。
                2、并不限制通过类来动态添加属性或方法。
                3、只对当前类的实例起作用，对该类派生出来的子类不起作用。
                4、如果要限制子类实例动态添加属性和方法，需要在子类中也定义__slots__，此时
                    子类的实例允许动态添加的属性和方法就是子类__slots__元组加上父类__slots__元组的和。

        6.6.2 使用type函数定义类
            1、定义类也是定义了一个特殊的对象---type类对象，并将该对象赋值给类名，
                所以class定义的类都是type类实例。
            2、type()函数动态创建类：
                type(类名，（父类1，父类2，...），dict(age =6,walk = fn))

        6.6.3 使用metaclass
            1、metaclass可以在创建类时，动态修改类定义。
            2、metaclass应该继承type类，重写__new__方法
            3、metaclass的__new__方法作用：
                当程序使用class定义新类时，如果指定了metaclass，那么__new__方法自动执行。
            4、语法：class Book(metaclass = ItemMeataCLass):...
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

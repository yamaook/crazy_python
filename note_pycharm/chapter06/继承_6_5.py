"""
    6.5 继承
        python多继承机制
        6.5.1 继承的语法
            1、语法：将多个父类放在子类之后的圆括号里，逗号隔开。
            2、默认继承object类
            3、子类继承父类可以得到父类方法
        6.5.2 关于多继承
            1、多父类中包含同名方法，排在前面的父类中方法会遮蔽排在后面的父类中方法。
        6.5.3 重写父类的方法
            override：子类包含与父类同名的方法的现象

        6.5.4 使用"未绑定方法"调用被重写方法
            1、"未绑定方法"：是指类直接调用实例方法的机制，需要手动绑定第一个参数。
            2、通过未绑定方法，可以在子类中调用父类中被重写的方法。

        6.5.5 使用super函数调用父类构造方法
            1、子类会继承得到父类的构造方法，排在前面的父类构造方法会被优先使用。
            2、子类重写父类构造方法，子类的构造方法必须调用父类的构造方法,调用方式有两种：
                    使用未绑定方法
                    使用super（）：通过super对象调用父类的构造函数
            3、super对象即可调用父类的实例方法，也可调用父类的类方法，并自动绑定方法的第一个参数。




"""


# 6.5.1 继承的语法
class Fruit:
    def info(self):
        print("我是一个水果！重%g克", self.weight)


class Food:
    def taste(self):
        print("不同食物的口感不同")


class Apple(Fruit, Food):
    pass


# 继承了父类方法
a = Apple()
a.weight = 5.6
a.info()
a.taste()

"""
    6.5.2 多继承
        推荐尽量不要使用多继承。
        多父类有同名方法时，排在前面的父类中方法会屏蔽掉后面的。
        
"""


class Item:
    def info(self):
        print("item中的方法", "这是一个商品")


class Product:
    def info(self):
        print("Product中的方法：", '这是一个工业商品')


class Mouse(Item, Product):
    pass


m = Mouse()
m.info()

"""
    6.5.3 重写父类方法override
        子类重写了父类方法或子类覆盖了父类方法。
"""


class Bird:
    def fly(self):
        print("我在天空里自由自在的飞翔")


class Ostrich(Bird):
    def fly(self):
        print("我只能在地上奔跑")


os = Ostrich()
os.fly()

"""
    6.5.4 使用未绑定方法调用被重写的方法
        未绑定方法就是类名直接调用实例方法不会自动绑定self
"""


class BaseClass:
    def foo(self):
        print("父类中定义的foo方法")


class SubClasee(BaseClass):
    def foo(self):
        print("子类重写的foo方法")

    def bar(self):
        print("执行bar方法")
        self.foo()
        BaseClass.foo(self)


sc = SubClasee()
sc.bar()

"""
    6.5.5 使用super函数调用父类的构造方法
"""


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def work(self):
        print("普通员工正在写代码，工资是：", self.salary)


class Customer:
    def __init__(self, favourite, address):
        self.favourite = favourite
        self.address = address

    def info(self):
        print("我是一个顾客，我的爱号是：%s,地址是%s" % (self.favourite, self.address))


class Manager(Employee, Customer):
    def __init__(self, salary, favorite, address):
        print('----Manager构造方法-----')
        super().__init__(salary)
        Customer.__init__(self, favorite, address)


m = Manager(25000, 'IT产品', '官洲')
m.work()
m.info()

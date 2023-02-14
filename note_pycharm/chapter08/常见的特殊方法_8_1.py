"""
    8、Python类的特殊方法
        8.1、常见的特殊方法
"""

"""
    8.1.1 重写__repr__方法
        作用：输出实例的自我描述信息，用来告诉外界实例的状态信息。
            对象.__repr__()
            通常返回的格式：类名[field=value1,field2=value2,...]       
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 29.8)
print(im)
print(im.__repr__())
im_str = im.__repr__() + ""


class Apple:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __repr__(self):
        return "Apple[color=" + self.color + \
               ",weight=" + str(self.weight) + "]"


a = Apple("红色", 3.68)
print(a)

"""
    8.1.2 析构方法：__del__
        1、用于销毁python对象。
        2、对象将要被系统回收之时，系统会自动调用该对象的del方法。
        3、python使用自动引用计数方式回收垃圾。
        4、如果父类提供析构方法，重写__del__方法时必须显式调用父类的__del__方法，
            这样才能保证合理地回收父类实例的部分属性。
"""


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __del__(self):
        print("del删除对象")


im = Item('鼠标', 29.8)
# x = im
del im
print('--------')

"""
    8.1.3 __dir__方法
        1、返回包含所有属性（包括方法）名的序列，
        2、当程序对某个对象执行dir()函数时，实际上将__dir__()返回值进行排序，然后包装成列表。
"""


class Item2:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        pass


im = Item2('鼠标', 29.8)
print(im.__dir__())
print(dir(im))

print('--------')
"""
    8.1.4 __dict__属性
        1、查看对象内部存储的属性名和属性值的字典。
        2、可以通过字典语法访问修改指定属性值。
"""


class Item:
    a = 100

    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 28.9)
print(im.__dict__)
print(im.__dict__['name'])
print(im.__dict__['price'])
im.__dict__['name'] = '键盘'
im.__dict__['price'] = 100
print(im.name)
print(im.price)

"""
    8.1.5 __getattr__、__setattr__等
    1、程序操作对象的属性时，系统会自动执行该对象特定的方法：
        __getattribute__:访问属性
        __getattr__:访问属性且该属性不存在
        __setattr__:对属性赋值
        __delattr__:删除属性
    2、属性不存在时，程序可通过重写这些方法来合成属性：
        通过后三个方法
    3、在读取或者设置属性之前进行某种拦截，可以重写1、3方法实现。
        
"""
print('----------------------')


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        print('设置%s属性' % key)
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print("读取%s属性" % item)
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError

    def __delattr__(self, item):
        print("删除%s属性" % item)
        if item == 'size':
            self.__dict__['width'] = 0
            self.__dict__['height'] = 0


rect = Rectangle(3, 4)
print(rect.size)
rect.size = 6, 8
print(rect.width)
del rect.size
print(rect.size)

print('----------------')


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        if key == 'name':
            if 2 < len(value) <= 8:
                self.__dict__['name'] = value
            else:
                raise ValueError("name长度必须在2-8之间")
        elif key == 'age':
            if 10 < value < 60:
                self.__dict__['age'] = value
            else:
                raise ValueError("age必须在10-60之间")


u = User('fkit', 24)
print(u.name)
print(u.age)
u.name = 'fku'
# u.age = 2  # 引发异常

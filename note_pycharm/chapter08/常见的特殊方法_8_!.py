"""
    8.1.1 重写__repr__方法
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
        用于销毁python对象
        对象将要被系统回收之时，系统会自动调用该对象的del方法
        python使用自动引用计数方式回收垃圾
        如果父类提供析构方法，必须显式调用父类的__del__方法
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
"""
    8.1.4 __dict__属性
        对象属性名和属性值的字典
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
u.age = 2  # 引发异常

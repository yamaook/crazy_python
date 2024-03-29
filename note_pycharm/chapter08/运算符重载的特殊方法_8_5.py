"""
    8.5 运算符重载的特殊方法
        让自定义类对象也支持各种运算符的运算。
"""

"""
    8.5.1 与数值运算符相关的特殊方法
        1、与数值运算相关的运算符：算术运算符、位运算符。
        2、运算符都有对应的方法提供支持，为自定义类提供这些方法，程序就可以用运算符来操作该类的实例。
        3、程序首先使用x.__add__(),然后使用y.__radd__()。
        4、__iadd__支持各种扩展后的赋值运算符。
        
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def setsize(self, size):
        self.width, self.height = size

    def getsize(self):
        return self.width, self.height

    size = property(getsize, setsize)

    # 运算符左侧调用
    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("+运算要求目标是Rectangle")
        return Rectangle(self.width + other.width, self.height + other.height)

    def __repr__(self):
        return 'Rectangle(width=%g,height=%g)' % (self.width, self.height)

    # 运算符右侧调用
    def __radd__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError("+运算符要求目标是数值")
        return Rectangle(self.width + other, self.height + other)

    # 增强运算符
    def __iadd__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError("+=运算符要求目标是数值")
        return Rectangle(self.width + other, self.height + other)

    # ><
    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError(">比较要求目标是Rectangle")
        return True if self.width * self.height > other.width * other.height else False

    # ==、!=
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("==比较要求目标是Rectangle")
        return True if self.width * self.height == other.width * other.height else False

    # >= <=
    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError(">=比较要求目标是Rectangle")
        return True if self.width * self.height >= other.width * other.height else False

    # 单目求负运算符支持
    def __neg__(self):
        self.width, self.height = self.height, self.width

    # 类型转换特殊方法
    def __int__(self):
        return int(self.width * self.height)

    # 内置函数四舍五入支持
    def __round__(self, n=None):
        self.width, self.height = round(self.width, n), round(self.height, n)
        return self


r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
r = r1 + r2
print(r)

r = 3 + r1
print(r)

r1 += 2
print(r1)

"""
    8.5.2 与比较运算符相关的特殊方法
        同一类实例比较大小，实现其中三个方法即可。
"""

print(r1 > r2)
print(r1 >= r2)
print(r1 < r2)
print(r1 <= r2)
print(r1 == r2)
print(r1 != r2)
print('----------------')
r3 = Rectangle(2, 6)
print(r2 >= r3)
print(r2 > r3)
print(r2 <= r3)
print(r2 < r3)
print(r2 == r3)
print(r2 != r3)
"""
    8.5.3 与单目运算符相关的特殊方法
        
"""
print("------------853-------------------------")
r = Rectangle(4, 5)
-r
print(r)

"""
    8.5.4 与类型转换相关的特殊方法
        
"""
print("------8.5.4-------------")
r = Rectangle(4, 5)
print(int(r))

"""
    8.5.5 与常见的内建函数相关的特殊方法
"""

r = Rectangle(4.13, 5.56)
result = round(r, 1)
print(r)
print(result)

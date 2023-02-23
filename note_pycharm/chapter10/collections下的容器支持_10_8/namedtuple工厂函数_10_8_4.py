"""
    10.8.4 namedtuple工厂函数
        创建一个tuple类的子类：命名元组类
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])
a, b = p
print(a, b)
print(p.x + p.y)
print(p)

my_data = ['East', 'North']
p2 = Point._make(my_data)
print(p2)

print(p2._asdict())
p3 = p2._replace(y='South')
print(p2)
print(p3)
print(p2._fields)
Color = namedtuple('Color', ' red green blue')
Pixel = namedtuple('Pixel', p2._fields + Color._fields)
pix = Pixel(11, 22, 128, 225, 0)
print(pix)

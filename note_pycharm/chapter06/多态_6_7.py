"""
    6.7多态
        同一个变量调用同一个方法时，呈现出多种行为就是多态。
        6.7.1 多态性
            1、多态是一种非常灵活的编程机制。
        6.7.2 检查类型
            issubclass(cls,class_or_tuple):
                检查cls是否为后一个类或元组包含的多个类中任意类的子类。
            isinstance(obj,class_or_tuple):
                检查obj是否为后一个类或元组包含的多个类中任意类或其子类的实例。
            __base__属性：
                返回所有直接父类组成的元组。
            __subclasses__()方法：
                返回所有直接子类组成的列表。R
"""
"""
    6.7.1多态性
            
"""


class Bird:
    def move(self, field):
        print('鸟在%s上自由地飞翔' % field)


class Dog:
    def move(self, field):
        print('狗在%s里飞快地奔跑' % field)


x = Bird()
x.move('天空')
x = Dog()
x.move('草地')


# 多态
class Canvas:
    def draw_pic(self, shape):
        print("开始绘图")
        shape.draw(self)


class Rectangle:
    def draw(self, canvas):
        print('在%s上绘制了矩形' % canvas)


class Triangle:
    def draw(self, canvas):
        print('在%s上绘制了三角形' % canvas)


class Circle:
    def draw(self, canvas):
        print('在%s上绘制了圆形' % canvas)


c = Canvas()
c.draw_pic(Rectangle())
c.draw_pic(Triangle())
c.draw_pic(Circle())

"""
    6.7.2 检查类型
"""
hello = 'Hello'
print(isinstance(hello, str))
print(isinstance(hello, object))
print(issubclass(str, object))
print(isinstance(hello, tuple))
print(issubclass(str, tuple))

my_list = [2, 4]
print(isinstance(my_list, list))
print(isinstance(my_list, object))
print(issubclass(list, object))
print(isinstance([2, 4], tuple))
print(issubclass(list, tuple))

data = (20, 'fkit')
print(isinstance(data, (list, tuple)))
print(issubclass(str, (list, tuple)))
print(issubclass(str, (list, tuple, object)))


# __bases__直接父类
class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(A.__bases__)
print(B.__bases__)
print(C.__bases__)

#查看直接子类
print(A.__subclasses__())
print(B.__subclasses__())
"""
    6.7多态
        同一个变量调用同一个方法时，呈现不同的行为就是多态。
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
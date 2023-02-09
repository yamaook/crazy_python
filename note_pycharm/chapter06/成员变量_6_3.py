"""
    6.3 成员变量

        6.3.1 类变量和实例变量
            1、类变量：不管全局范围还是实例方法内都需要用类名进行访问，不能直接访问类变量。
            2、对象也可以访问类变量，其本质还是通过类名访问类变量。
            3、如果通过对象对类变量赋值，就是定义了新的实例变量。
            4、类变量和实例变量有重名，修改变量值互不影响。

        6.3.2使用property函数定义属性
            1、其他语言称这种property合成的属性为计算属性，这种属性并不真正存储任何状态。
            2、可以使用装饰器来修饰方法，使之成为属性。

            简单点说，属性可以用装饰器和property函数定义。
"""


# 6.3.1类变量和实例变量

# 全局范围内和方法内访问类变量，都需要使用类名
class Address:
    detail = '广州'
    post_code = '510660'

    def info(self):
        print(Address.detail)
        print(Address.post_code)


print(Address.detail)
addr = Address()
addr.info()
Address.detail = '佛山'
Address.post_code = '460110'

addr.info()


# 使用对象访问类变量:本质还是通过类名访问类变量
class Record:
    item = '鼠标'
    date = '2016-6-12'

    def info(self):
        print('info方法中：', self.item)
        print('info方法中：', self.date)


rc = Record()
print(rc.item)
print(rc.date)
rc.info()
Record.item = '键盘'
Record.date = '2022-7-27'
rc.info()


# 通过对象修改类变量，实际是定义了新的实例变量
class Inventory:
    item = '鼠标'
    quantity = 2000

    def change(self, item, quantity):
        self.item = item
        self.quantity = quantity


iv = Inventory()
iv.change('显示器', 500)
print(iv.item)
print(iv.quantity)
print(Inventory.item)
print(Inventory.quantity)
# 如果程序通过类修改类变量，实例变量的值也不会受到影响
Inventory.item = '类变量item'
Inventory.quantity = '类变量quantity'
print(iv.item)
print(iv.quantity)
# 如果程序通过实例修改实例变量，类变量的值也不会受到影响
iv.item = '实例变量item'
iv.quantity = '实例变量quantity'
print(Inventory.item)
print(Inventory.quantity)


# 6.3.2 使用property函数定义属性
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def setsize(self, size):
        self.width, self.height = size

    def getsize(self):
        return self.width, self.height

    def delsize(self):
        self.width, self.height = 0, 0

    # 定义属性
    size = property(getsize, setsize, delsize, '用于描述矩形大小的属性')


# 通过类名访问属性的文档说明
print(Rectangle.size.__doc__)
help(Rectangle.size)

rect = Rectangle(4, 3)
# 读属性
print(rect.size)
# 修改属性
rect.size = (9, 7)
print(rect.width)
print(rect.height)
# 删除属性
del rect.size
print(rect.width)
print(rect.height)


# 只定义读写属性的case
class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def getfullname(self):
        return self.first + ',' + self.last

    def setfullname(self, fullname):
        first_last = fullname.rsplit(',')
        self.first = first_last[0]
        self.last = first_last[1]

    fullname = property(getfullname, setfullname)


u = User('悟空', '孙')
print(u.fullname)
u.fullname = '八戒, 猪'
print(u.first)
print(u.last)
"""
    这种合成的属性不存储任何状态，其他语言称为计算属性
"""


# 使用装饰器来修饰方法，使其成为属性
class Cell:
    def __init__(self, state):
        self.state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if 'alive' in value.lower():
            self._state = 'alive'
        else:
            self._state = 'dead'

    @property
    def is_dead(self):
        return not self._state.lower() == 'alive'


c = Cell('AAAAAliNNNNvehahaha')
c.state = 'Alive'
print(c.state)
print(c.is_dead)

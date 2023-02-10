"""
    自我感觉枚举确实是一个类，不过枚举类里定义的枚举值不是类变量，而是该枚举类的所有对象。
    6.8 枚举类
        实例有限且固定的类，就是枚举类。

        6.8.1 枚举入门
            1、直接使用Enum列出多个枚举值来创建枚举类：
                枚举类包含：类名
                          枚举值：name（枚举值的变量名）,value（枚举值的序号）
                可以通过name 和value直接访问枚举值。

            2、通过继承Enum基类来派生枚举类：
                定义更复杂的枚举，比如为枚举类定义方法，或者为枚举值指定value。

            3、__members__属性
                返回一个字典，包含了该枚举的所有对象。

        6.8.2 枚举的构造方法
            我觉得这块就是枚举的value会传给每个枚举对象的构造函数。
                相当于枚举除了有value值之外，还有其他变量，但是其他变量的值来源于value。

            1、枚举类有构造函数时，定义枚举实例时必须为构造函数参数设置值。
                枚举构造函数需要几个值，value就必须指定几个值。

"""
"""
    6.8.1 枚举入门
"""
import enum

Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
# 访问枚举对象通过name
print(Season['SUMMER'])
# 根据枚举value访问枚举对象
print(Season(3))

# 遍历枚举的所有成员
print(Season.__members__)
for name, member in Season.__members__.items():
    print(name, '->', member, ':', member.value)


# 定义更复杂的枚举

class Orientation(enum.Enum):
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'

    def info(self):
        print("这是一个代表方向【%s】的枚举实例" % self.value)


print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
print(Orientation['WEST'])
print(Orientation('南'))
Orientation.EAST.info()
for name, member in Orientation.__members__.items():
    print(name, '->', member, ':', member.value)

"""
    6.8.2 枚举的构造器
"""


class Gender(enum.Enum):
    MALE = '男', '阳刚之气'
    FEMALE = '女', '柔顺之美'

    def __init__(self, cn_name, desc):
        self._cn_name = cn_name
        self._desc = desc

    @property
    def desc(self):
        return self._desc

    @property
    def cn_name(self):
        return self._cn_name


print(Gender.FEMALE.name)
print(Gender.FEMALE.value)
print(Gender.FEMALE.cn_name)
print(Gender.FEMALE.desc)

"""
    6.8 枚举类
        实例有限且固定的类，就是枚举类
        枚举类自动生成了有限的枚举对象可以直接用。
        下面介绍了枚举类的定义方法2种，和枚举类构造函数的使用
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
# 根据枚举值访问枚举对象
print(Season(3))

# 遍历枚举实例
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

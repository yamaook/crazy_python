"""
    新的开始必须遗忘过去的遗憾
    6.1类和对象
        6.1.1定义类
            类名：单词连缀而成，每个单词首字母大写，单词与单词之间没分隔符
            类定义：由类头和类体构成，类体中最重要的两个成员就是类变量和方法，
                    类中成员之间定义顺序没有任何影响，各成员之间可以相互调用。
                        python类所包含的最重要的两个成员就是变量和方法。
            类变量：属于类本身，定义该类本身所包含的状态数据。
            实例变量：属于该类的对象，定义对象所包含的状态数据。
            方法：定义该类对象的行为和功能实现。
            实例方法：类中定义的方法默认是实例方法，定义实例方法和定义函数的方法基本相同，
                        只是实例方法的第一个参数会被绑定到方法的调用者，所以实例方法至少有一个参数。
            构造方法：属于实例方法，构造该类对象，通过调用构造方法返回该类对象。
                        如果没有定义构造方法，会自动定义一个只包含self参数的默认的构造方法。
            类说明文档：类申明之后，类体之前。
            python是动态语言：
                类变量可以动态增加或删除。
                对象的实例变量也可以动态增加或删除

        6.1.2对象的产生和使用
            对象的作用：
                    访问、添加、删除实例变量
                    调用、添加、删除实例方法

        6.1.3对象的动态性
            1、为对象动态增加实例变量，也可以动态删除实例变量。
            2、对对象动态增加方法。
                动态增加的方法不会自动将调用者自动绑定到第一个参数。
                如果希望动态增加的方法能自动绑定到第一个参数，需要借助types模块下的MethodType。

        6.1.4实例方法和自动绑定self
            1、对象的一个方法调用另一个方法时，不可以省略self。
            2、自动绑定的self参数并不依赖于具体的调用方式，不管是以方法调用还是以函数调用的方式执行它。
            3、self可以当成实例方法的返回值，虽然让代码简洁，但是实际意义模糊。
"""

# 空类
import decimal


class Empty:
    pass


class Person:
    """这是类说明文档"""
    hair = 'black'

    def __init__(self, name='Charlie', age=8):
        self.name = name
        self.age = age

    def say(self, content):
        print(content)


# 6.1.2对象的产生和使用
# 调用Person类的构造方法，返回一个对象
p = Person()
print(p.name, p.age)
p.name = 'ligang'
p.say('it`s easy')
print(p.name, p.age)

# 6.1.3 对象的动态性
# 增加实例变量
p.skills = ['programming', 'swin']
print(p.skills)
# 删除实例变量
del p.name


# print(p.name)


# 增加实例方法
def info(self):
    print("---info---", self)


p.foo = info
# 需要手动绑定对象
p.foo(p)
p.bar = lambda self: print("-----lambda", self)
p.bar(p)


# 自动绑定对象
def intro_func(self, content):
    print("我是一个人，信息为：%s" % content)


from types import MethodType

p.intro = MethodType(intro_func, p)
p.intro("生活在别处")


# 6.1.4 实例方法和自动绑定self
# self自动绑定方法的调用者
class Dog:
    def jump(self):
        print("jump正在执行")

    def run(self):
        self.jump()
        print("run正在执行")


dog = Dog()
dog.run()


# self自动绑定正在初始化的对象
class InConstructor:
    def __init__(self):
        foo = 0
        self.foo = 6


print(InConstructor().foo)


# self自动绑定不依赖于具体的调用方式
class User:
    def test(self):
        print('self参数：', self)


u = User()
# 以方法形式调用
u.test()
# 以函数形式调用
foo = u.test
foo()


# self参数作为对象的默认引用，
# self参数作为实例方法的返回值
class ReturnSelf:
    def grow(self):
        if hasattr(self, 'age'):
            self.age += 1
        else:
            self.age = 1
        return self


rs = ReturnSelf()
rs.grow().grow().grow().grow()
print('rs的age属性值是：', rs.age)

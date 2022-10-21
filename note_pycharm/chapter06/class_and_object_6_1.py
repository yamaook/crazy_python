"""
    新的开始必须遗忘过去的遗憾
    6.1类和对象
        6.1.1定义类
            类名：单词连缀而成，每个单词首字母大写，单词与单词之间没分隔符
            类成员：变量和方法
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


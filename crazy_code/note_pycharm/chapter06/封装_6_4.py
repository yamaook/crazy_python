"""
    6.4 封装
    将对象的状态信息隐藏在对象内部，不允许外部程序直接访问
        对象内部信息，而是通过该类所提供的方法来实现对内部访问。
"""

"""
    python没有真正的隐藏机制，所以python类成员默认是公开的。
    如果需要隐藏某些成员，只需要在成员名前加双下划线，但这种隐藏仍然可以绕过去。
"""


class User:

    def __hide(self):
        print("示范隐藏的hide方法")

    def getname(self):
        return self.__name

    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3-8之间')
        self.__name = name

    name = property(getname, setname)

    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户年龄必须在18-70之间')
        self.__age = age

    def getage(self):
        return self.__age

    age = property(getage, setage)


u = User()
u.name = 'fkit'
u.age = 25
print(u.name)
print(u.age)
# 没有真正隐藏
u._User__hide()
u._User__name = 'fk'
print(u.name)

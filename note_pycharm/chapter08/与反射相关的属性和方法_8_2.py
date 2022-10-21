"""
    动态判断是否包含某个属性、或者动态设置某个属性值，可以用python的反射支持
"""
"""
    8.2.1 动态操作属性
"""


class Comment:
    def __init__(self, detail, view_times):
        self.detail = detail
        self.view_times = view_times

    def info(self):
        print("一条简单的评论，内容是%s" % self.detail)


c = Comment("疯狂python讲义很不错", 20)
# 是否包含某属性或者方法
print(hasattr(c, 'detail'))
print(hasattr(c, 'view_times'))
print(hasattr(c, 'info'))
# 获取指定属性值
print(getattr(c, "detail"))
print(getattr(c, "view_times"))
print(getattr(c, "info"))
# 为指定属性设置属性值
setattr(c, 'detail', '天气不错')
setattr(c, 'view_times', 32)

print(c.detail, c.view_times)
# 设置不存在的属性，即为添加
setattr(c, 'test', '新增的测试属性')
print(c.test)


# 设置方法,新设置的方法是未绑定方法
def bar():
    print("一个简单的bar方法")


setattr(c, 'info', bar)
c.info()
print(getattr(c, 'info'))
# 帮方法设置成属性
setattr(c, 'info', 'fkit')
print(c.info)

"""
    8.2.2 __call__属性
"""


class User:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def validLogin(self):
        print("验证%s的登录" % self.name)


u = User('crazyit', 'leegang')
print(hasattr(u.name, '__call__'))
print(hasattr(u.passwd, '__call__'))
print(hasattr(u.validLogin, '__call__'))


class Role:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('执行role对象')


r = Role('管理员')
# 直接调用r对象就是调用该对象的————call方法
r()


# 函数也是对象，也有call方法
def foo():
    print("foo函数")


foo()
foo.__call__()

'测试__all__变量的模块'


def hello():
    print('hello,python')


def world():
    print('python world is funny')


def test():
    print('--test--')


__all__ = ['hello', 'world']

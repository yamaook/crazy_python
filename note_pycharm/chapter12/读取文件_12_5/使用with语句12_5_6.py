"""
    12.5.6 使用with语句
"""
import fileinput

with open('info.txt', 'r', True, 'utf-8') as f:
    for line in f:
        print(line, end='')

with fileinput.input(files=('test.txt', 'info.txt')) as f:
    for line in f:
        print(line, end='')


class FKResource:
    def __init__(self, tag):
        self.tag = tag
        print("构造器初始化资源:%s" % tag)

    def __enter__(self):
        print("[__enter__%s]" % self.tag)
        return 'fkit'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[__exit__%s]" % self.tag)
        if exc_tb is None:
            print("没有异常关闭资源")
        else:
            print('遇到异常关闭资源')
            return False


with FKResource('孙悟空') as dr:
    print(dr)
    print('[with代码块]没有异常')
print('--------------')

with FKResource('白骨精') as dr:
    print('[with代码块]异常之前的代码')
    raise Exception
    print('[with代码块]-----异常之后的代码')

"""
    7.4 Python的异常传播轨迹
"""
import sys
import traceback


class SelfException(Exception): pass


def main():
    fistMethod()


def fistMethod():
    secondMethod()


def secondMethod():
    thirdMethod()


def thirdMethod():
    raise SelfException("自定义异常信息")


try:
    main()
except:
    print("自己输出的")
    traceback.print_exc(limit=2)
    traceback.print_exc(file=open('log.txt', 'a'))
    # raise ValueError('同轨迹异常').with_traceback(sys.exc_info()[2])

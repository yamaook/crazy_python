"""
    7.4 Python的异常传播轨迹
        traceback模块：处理异常传播轨迹。
            traceback.print_exc():将异常传播轨迹信息输出到控制台或者文件中
                完整形式：
                    print_exception(etype,value,tb[,limit[,file]])
                sys对象可以获得except所捕获的异常信息，并作为上面的参数，
                    所以使用print_exc会自动处理当前块捕获的异常。

            format_exc():将异常传播轨迹信息转换成字符串


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
except Exception as e:
    print("自己输出的")
    traceback.print_exc(limit=2)
    traceback.print_exc(file=open('log.txt', 'a'))
    # raise ValueError('同轨迹异常').with_traceback(sys.exc_info()[2])

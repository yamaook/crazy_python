"""
    7.3 使用raise引发异常
        自行引发异常使用raise语句

        7.3.1 引发异常
            1、如果程序中的数据、执行与既定的业务需求不符，这就是一种异常。这种异常系统无法引发，只能自行引发。
            2、raise用法：
                raise:引发当前上下文捕获的异常，或者默认运行时异常。
                raise 异常类：引发指定异常类的默认实例。
                raise 异常对象：引发指定异常对象。
            3、python解释器无差别处理系统异常和自行引发的异常。
            4、处理用户引发异常的两种方式：
                用try处理掉
                不管向上传播

        7.3.2 自定义异常类
            1、继承Exception类或者其子类。
            2、一般不写更多代码，只要指定自定义异常类的父类即可：
                class AuctionException(Exception):pass
            3、让异常类名能准确描述该异常。

        7.3.3 except 和 raise 同时使用
            1、作用：多个方法协作处理同一个异常，可以在except块中结合raise语句来完成。
            2、实际应用对异常的处理分为两个部分
                日志记录异常详细情况。
                根据异常向使用者传达提示。
            3、异常包装：
                传播原始异常的详细信息，自定义异常包装原始异常：
                    raise AuctionException(e)

        7.3.4 raise不需要参数
            raise在except块中，不带参数会自动引发当前上下文激活的异常，否则默认引发运行时异常。
"""
BOARD_SIZE = 15
board = []


def initBoard():
    for i in range(BOARD_SIZE):
        row = ["✚"] * BOARD_SIZE
        board.append(row)


def printBoard():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end=" ")
        print()


# initBoard()
# printBoard()
# while True:
#     inputStr = input("请输入您下棋的坐标，应为x,y的格式：\n")
#     if inputStr == '':
#         print("下棋结束。。。")
#         break
#     try:
#         x_str, y_str = inputStr.split(sep=",")
#         if board[int(x_str) - 1][int(y_str) - 1] != "✚":
#             # 默认引发运行时异常
#             raise
#         board[int(x_str) - 1][int(y_str) - 1] = "O"
#         printBoard()
#     except Exception as e:
#         print(type(e))
#         print("输入不合法，请重新输入----")
#         continue

# 处理用户引发异常的两种方式
def main():
    try:
        mtd(3)
    except Exception as e:
        print("程序出现异常：", e)
    # mtd(3)


def mtd(a):
    if a > 0:
        raise ValueError("a的值大于0，不符合要求")


main()
"""
    7.3.2 自定义异常类
"""


class AuctionException(Exception): pass


"""
    7.3.3 except和raise同时使用
"""

# class AuctionTest:
#     def __init__(self, init_price):
#         self.init_price = init_price
#
#     def bid(self, bid_price):
#         d = 0.0
#         try:
#             d = float(bid_price)
#         except Exception as e:
#             print("转换出异常", e)
#             # raise AuctionException("竞拍价格必须是数值，不能包含其他字符")
#             # 异常转译
#             raise AuctionException(e)
#         if self.init_price > d:
#             raise AuctionException("竞拍价格比起拍价格低，不允许竞拍")
#         self.init_price = d
#
#
# def main():
#     at = AuctionTest(20.4)
#     try:
#         at.bid('df')
#     except AuctionException as ae:
#         print("main函数捕获异常", ae)
#
#
# main()

"""
    7.3.4 raise不需要参数
"""


class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price

    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            print("转换出异常", e)
            # 引发当前激活的异常
            raise
        if self.init_price > d:
            raise AuctionException("竞拍价格比起拍价格低，不允许竞拍")
        self.init_price = d


def main():
    at = AuctionTest(20.4)
    try:
        at.bid('df')
    except Exception as ae:
        print("main函数捕获异常", type(ae))


main()

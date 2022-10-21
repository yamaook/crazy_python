"""
    自行引发异常使用raise
    7.3.1 引发异常
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

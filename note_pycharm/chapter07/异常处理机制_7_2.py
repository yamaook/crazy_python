"""
    7.2 异常处理机制
"""
# 7.2.1 使用try except捕获异常
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
#             print("已有棋子，请重新输入")
#             continue
#         board[int(x_str) - 1][int(y_str) - 1] = "O"
#         printBoard()
#     except Exception:
#         print("输入不合法，请重新输入----")
#         continue
"""
    7.2.2 异常类的继承体系
    从这里又是一次过哈
"""
import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a, b)
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except IndexError:
    print("索引错误：输入的参数个数不够")
except ValueError:
    print("数值错误: 只能接受整数参数")
except ArithmeticError:
    print("算数错误")
except Exception:
    print("未知错误")
"""
    7.2.3 多异常捕获
"""
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a, b)
    c = a / b
    print("您输入的两个数相除的结果是：", c)
except (IndexError, ValueError, ArithmeticError):
    print("程序发生数组越界，数字格式异常，算数异常之一")
except:
    print("未知异常")

"""
 7.2.4 访问异常信息
    忘记过去，从头开始。
"""

# def foo():
#     try:
#         fis = open('a.txt')
#     except Exception as e:
#         print(e.args)
#         print(e.errno)
#         print(e.strerror)
#
#
# foo()
"""
    7.2.5 else 块
    try没有出现异常,会执行else块
"""
# s = input("请输入除数-----")
# try:
#     result = 20 / int(s)
#     print('20除以%s的结果是：%g' % (s, result))
# except ValueError:
#     print("值错误，您必须输入数值")
# except ArithmeticError:
#     print('算数错误，您不能输入0')
# else:
#     print('没有出现异常')

# 直接写在try块代码后和放在else块中的代码的区别
# def else_test():
#     s = input("请输入除数")
#     result = 20 / int(s)
#     print('20除以%s的结果是：%g' % (s, result))
#
#
# def right_main():
#     try:
#         print("try块的代码，没有异常")
#     except:
#         print("程序出现异常")
#     else:
#         else_test()
#
#
# def wrong_main():
#     try:
#         print('try块的代码，没有异常')
#         else_test()
#     except:
#         print('程序出现异常')
#
#
# wrong_main()
# right_main()

"""
    7.2.6 使用finally回收资源
"""
import os


def test():
    fis = None
    try:
        fis = open('a.txt')
    except OSError as e:
        print(e.strerror)
        return
        # os._exit(1)#推出解释器
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print("执行finally块里的资源回收")


test()


def test():
    try:
        return True
    finally:
        return False


a = test()
print(a)

"""
    7.2.7 异常处理嵌套
"""

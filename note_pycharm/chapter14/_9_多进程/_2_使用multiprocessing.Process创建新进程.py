"""
    14.9.2 使用multiprocessing.Process创建新进程
"""
import multiprocessing
import os


# # 1、以指定函数创建新进程
# def action(max):
#     for i in range(max):
#         print('(%s)子进程(父进程:(%s)): %d' % (os.getpid(), os.getppid(), i))
#
#
# if __name__ == '__main__':
#     for i in range(100):
#         print("(%s)主进程：%d" % (os.getpid(), i))
#         if i == 20:
#             mp1 = multiprocessing.Process(target=action, args=(100,))
#             mp1.start()
#             mp2 = multiprocessing.Process(target=action, args=(100,))
#             mp2.start()
#             mp2.join()
#     print("主进程执行完成")


# 2、继承Process类创建子进程
class MyProcess(multiprocessing.Process):
    def __init__(self, max):
        self.max = max
        super().__init__()

    def run(self) -> None:
        for i in range(self.max):
            print('(%s)子进程(父进程:(%s)): %d' % (os.getpid(), os.getppid(), i))


if __name__ == '__main__':
    for i in range(100):
        print("(%s)主进程：%d" % (os.getpid(), i))
        if i == 20:
            mp1 = MyProcess(100)
            mp1.start()
            mp2 = MyProcess(100)
            mp2.start()
            mp2.join()
    print("主进程执行完成")

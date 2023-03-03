"""
    14.2 线程的创建和启动

"""

"""
14.2.1 调用Thread类构造器创建线程
"""
import threading

# def action(max):
#     for i in range(max):
#         print(threading.current_thread().getName() + ' ' + str(i))
#
#
# for i in range(100):
#     print(threading.current_thread().getName() + ' ' + str(i))
#     if i == 20:
#         t1 = threading.Thread(target=action, args=(100,))
#         t1.start()
#         t2 = threading.Thread(target=action, args=(100,))
#         t2.start()
#
# print('主线程执行完成！')


"""
14.2.2 继承Thread类创建线程类
"""


class FKThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.i = 0

    def run(self):
        while self.i < 100:
            print(threading.current_thread().getName() + ' ' + str(self.i))
            self.i += 1


for i in range(100):
    print(threading.current_thread().getName() + ' ' + str(i))
    if i == 20:
        ft1 = FKThread()
        ft1.start()
        ft2 = FKThread()
        ft2.start()
print('主线程执行完成')

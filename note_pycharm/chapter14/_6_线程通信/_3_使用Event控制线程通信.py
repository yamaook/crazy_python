"""
    14.6.3 使用event控制线程通信
"""
import threading
import time


# event = threading.Event()
#
#
# def cal(name):
#     print("%s 启动" % threading.current_thread().getName())
#     print('%s 准备开始计算状态' % name)
#     event.wait()
#     print('%s 收到通知了' % threading.current_thread().getName())
#     print('%s 正式开始计算！' % name)
#
#
# threading.Thread(target=cal, args=('甲',)).start()
# threading.Thread(target=cal, args=('乙',)).start()
# time.sleep(2)
# print('-----------------')
# print('主线程发出事件')
# event.set()


# Event 改写后的Account
class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance
        self.lock = threading.Lock()
        self.event = threading.Event()

    def getBalance(self):
        return self.__balance

    # 取钱操作
    def draw(self, draw_amount):
        self.lock.acquire()
        if self.event.is_set():
            print(threading.current_thread().name + "取钱" + str(draw_amount))
            self.__balance -= draw_amount
            print('取之后账户余额为：' + str(self.__balance))
            self.event.clear()
        self.lock.release()
        self.event.wait()

    def deposit(self, deposit_amount):
        self.lock.acquire()
        if not self.event.is_set():
            print(threading.current_thread().name + "存款" + str(deposit_amount))
            self.__balance += deposit_amount
            print('存之后账户余额为：' + str(self.__balance))
            self.event.set()
        self.lock.release()
        self.event.wait()

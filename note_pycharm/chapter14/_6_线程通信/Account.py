import threading
import time


class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance
        self.cond = threading.Condition()
        # 是否已经存钱
        self.__flag = False

    def getBalance(self):
        return self.__balance

    # 取钱操作
    def draw(self, draw_amount):
        self.cond.acquire()
        try:
            if not self.__flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name + "取钱" + str(draw_amount))
                self.__balance -= draw_amount
                print('取之后账户余额为：' + str(self.__balance))
                self.__flag = False
                self.cond.notify_all()
        finally:
            self.cond.release()

    def deposit(self, deposit_amount):
        self.cond.acquire()
        try:
            if self.__flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name + "存款" + str(deposit_amount))
                self.__balance += deposit_amount
                print('存之后账户余额为：' + str(self.__balance))
                self.__flag = True
                self.cond.notify_all()
        finally:
            self.cond.release()

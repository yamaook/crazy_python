"""
    14.5.2 同步锁
"""
import threading
import time


class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.__balance = balance
        self.lock = threading.RLock()

    def getBalance(self):
        return self.__balance

    def draw(self, draw_amount):
        self.lock.acquire()
        try:
            if self.__balance >= draw_amount:
                print(threading.current_thread().name + '取钱成功，突出炒片' + str(draw_amount))
                time.sleep(0.001)
                self.__balance -= draw_amount
                print('\t余额为：' + str(self.__balance))
            else:
                print(threading.current_thread().name + '失败,余额不足')
        finally:
            self.lock.release()


def draw(account, draw_amount):
    account.draw(draw_amount)


acct = Account('1234567', 1000)
threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 800)).start()

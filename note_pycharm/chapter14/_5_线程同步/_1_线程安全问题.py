"""
14.5.1 线程安全问题
"""


class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


import threading
import time


def draw(account, draw_amount):
    if account.balance >= draw_amount:
        print(threading.current_thread().name + '取钱成功，突出炒片' + str(draw_amount))
        time.sleep(0.001)
        account.balance -= draw_amount
        print('\t余额为：' + str(account.balance))
    else:
        print(threading.current_thread().name + '失败余额不足')


acct = Account('1234567', 1000)
threading.Thread(name='甲', target=draw, args=(acct, 800)).start()
threading.Thread(name='乙', target=draw, args=(acct, 800)).start()

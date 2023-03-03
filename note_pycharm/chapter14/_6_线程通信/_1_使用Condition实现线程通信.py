"""
    14.6.1 使用condition实现线程通信
"""
from Account import *


def draw_many(account, draw_amount, max):
    for i in range(max):
        account.draw(draw_amount)


def deposit_many(account, deposit_amount, max):
    for i in range(max):
        account.deposit(deposit_amount)


acct = Account('1234567', 0)

threading.Thread(name="取钱者 ", target=draw_many, args=(acct, 800, 100)).start()
threading.Thread(name='存款者甲 ', target=deposit_many, args=(acct, 800, 100)).start()
threading.Thread(name='存款者乙 ', target=deposit_many, args=(acct, 800, 100)).start()
threading.Thread(name='存款者丙 ', target=deposit_many, args=(acct, 800, 100)).start()

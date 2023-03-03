"""
    14.5.3 死锁
"""
import threading
import time


class A:
    def __init__(self):
        self.lock = threading.RLock()

    def foo(self, b):
        try:
            self.lock.acquire()
            print('当前线程名：' + threading.current_thread().name + ' 进入了A实例的foo方法\n')
            time.sleep(0.2)
            print('当前线程名：' + threading.current_thread().name + ' 企图调用B实例的last方法')
            b.last()
        finally:
            self.lock.release()

    def last(self):
        try:
            self.lock.acquire()
            print("进入了A类的last方法内部")
        finally:
            self.lock.release()


class B:
    def __init__(self):
        self.lock = threading.RLock()

    def bar(self, a):
        try:
            self.lock.acquire()
            print('当前线程名：' + threading.current_thread().name + ' 进入了B实例的bar方法\n')
            time.sleep(0.2)
            print('当前线程名：' + threading.current_thread().name + ' 企图调用A实例的last方法')
            a.last()
        finally:
            self.lock.release()

    def last(self):
        try:
            self.lock.acquire()
            print("进入了B类的last方法内部")
        finally:
            self.lock.release()


a = A()
b = B()


def init():
    threading.current_thread().name = "主线程"
    a.foo(b)
    print('进入了主线程之后')


def action():
    threading.current_thread().name = '副线程'
    b.bar(a)
    print('进入了副线程之后')


threading.Thread(target=action).start()
init()

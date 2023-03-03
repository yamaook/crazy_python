"""
    14.8 线程相关类
"""
import time

"""
    14.8.1 线程局部变量
"""
import threading
from concurrent.futures import ThreadPoolExecutor

# mydata = threading.local()
#
#
# def action(max):
#     for i in range(max):
#         try:
#             mydata.x += i
#         except:
#             mydata.x = i
#         print("%s mydata.x的值为：%d" % (threading.current_thread().name, mydata.x))
#
#
# with ThreadPoolExecutor(max_workers=2) as pool:
#     pool.submit(action, 10)
#     pool.submit(action, 10)

"""
    14.8.2 定时器
"""

# def hello():
#     print('hello world')
#
#
# t = threading.Timer(10.0, hello)
# t.start()

## 重复调用函数
# count = 0
#
#
# def print_time():
#     print("当前时间:%s" % time.ctime())
#     global t, count
#     count += 1
#     if count < 10:
#         t = threading.Timer(1, print_time)
#         t.start()
#
#
# t = threading.Timer(1, print_time)
# t.start()

"""
    14.8.3 任务调度
"""
import sched

s = sched.scheduler()


def print_time(name='default'):
    print("%s 的时间:%s" % (name, time.ctime()))


print('主线程:', time.ctime())
s.enter(10, 1, print_time)
s.enter(5, 2, print_time, argument=('位置参数',))
s.enter(5, 1, print_time, kwargs={'name': '关键字参数'})
s.run(blocking=True)
print('主线程', time.ctime())

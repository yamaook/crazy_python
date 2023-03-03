"""
    14.4 控制线程
"""

"""
        14.4.1 join线程
"""
import threading

#
# def action(max):
#     for i in range(max):
#         print(threading.current_thread().name + ' ' + str(i))
#

# threading.Thread(target=action, args=(100,), name='新线程').start()
#
# for i in range(100):
#     if i == 20:
#         jt = threading.Thread(target=action, args=(100,), name='被join的线程')
#         jt.start()
#         jt.join()
#     print(threading.current_thread().name + ' ' + str(i))
"""
        14.4.2 后台线程
"""

# def action(max):
#     for i in range(max):
#         print(threading.current_thread().name + ' ' + str(i))
#
#
# t = threading.Thread(target=action, args=(100,), name='后台线程')
# t.daemon = True
# t.start()
# for i in range(10):
#     print(threading.current_thread().name + ' ' + str(i))

"""
    14.4.3 线程睡眠:sleep
"""
import time

for i in range(10):
    print("当前时间:%s" % time.ctime())
    time.sleep(1)

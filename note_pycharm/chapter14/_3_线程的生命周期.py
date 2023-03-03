"""
    14.3 线程的生命周期
        14.3.1 新建和就绪状态
"""
import threading

"""
14.3.1 新建和就绪状态
"""
# def action(max):
#     for i in range(max):
#         print(threading.current_thread().name + ' ' + str(i))
#
#
# for i in range(100):
#     print(threading.current_thread().name + ' ' + str(i))
#     if i == 20:
#         threading.Thread(target=action, args=(100,)).run()
#         threading.Thread(target=action, args=(100,)).run()
"""
    14.3.2 运行和阻塞状态
"""

"""
    14.3.3 线程死亡
"""


def action(max):
    for i in range(max):
        print(threading.current_thread().name + ' ' + str(i))


sd = threading.Thread(target=action, args=(100,))

for i in range(300):
    print(threading.current_thread().name + ' ' + str(i))
    if i == 20:
        sd.start()
        print(sd.is_alive())
    if i > 20 and not sd.is_alive():
        sd.start()

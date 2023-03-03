"""
    14.7 线程池
"""
"""
    14.7.1 使用线程池
"""
from concurrent.futures import ThreadPoolExecutor
import threading
import time


# task函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))
        my_sum += i
    return my_sum


# pool = ThreadPoolExecutor(max_workers=2)
# future1 = pool.submit(action, 50)
# future2 = pool.submit(action, 100)
# print(future1.done())
# time.sleep(3)
# print(future2.done())
# print(future1.result())
# print(future2.result())
# pool.shutdown()

"""
    14.7.2 获取执行结果
"""
# #1、 添加回调函数
# with ThreadPoolExecutor(max_workers=2) as pool:
#     future1 = pool.submit(action, 50)
#     future2 = pool.submit(action, 100)
#
#
#     def get_result(future):
#         print(future.result())
#
#
#     future1.add_done_callback(get_result)
#     future2.add_done_callback(get_result)
#     print('----------------')

# 2、 使用map()方法，启动线程并收集线程任务的返回值
with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(action, (50, 100, 150))
    print('-------------')
    # for r in results:
    #     print(r)
    print(list(results))

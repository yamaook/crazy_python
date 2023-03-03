"""
    14.9.4 使用进程池管理进程
"""
import multiprocessing
import time
import os


# # 1、使用apply_async启动进程
# def action(name='default'):
#     print('(%s)进程正在执行，参数为: %s' % (os.getpid(), name))
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     pool = multiprocessing.Pool(processes=4)
#     pool.apply_async(action)
#     pool.apply_async(action, args=('位置参数',))
#     pool.apply_async(action, kwds={'name': '关键字参数'})
#     pool.close()
#     pool.join()

# 2、使用map方法启动进程
def action(max):
    my_sum = 0
    for i in range(max):
        print('(%s) 进程正在执行：%d' % (os.getpid(), i))
        my_sum += i
    return my_sum


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(action, (50, 100, 150))
        print('---------------')
        for r in results:
            print(r)

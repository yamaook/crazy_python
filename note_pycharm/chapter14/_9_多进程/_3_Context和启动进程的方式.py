"""
    14.9.3 Context 和 启动进程的方式
"""
import multiprocessing
import os


def foo(q):
    print('被启动的新进程：(%s)' % os.getpid())
    q.put('Python')


# 方法1
# if __name__ == '__main__':
#     multiprocessing.set_start_method('fork')
#     q = multiprocessing.Queue()
#     mp = multiprocessing.Process(target=foo, args=(q,))
#     mp.start()
#     print(q.get())
#     mp.join()

# 方法2
if __name__ == '__main__':
    ctx = multiprocessing.get_context('fork')
    q = ctx.Queue()
    mp = ctx.Process(target=foo, args=(q,))
    mp.start()
    print(q.get())
    mp.join()

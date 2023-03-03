"""
    14.9.5 进程通信

"""
import multiprocessing


# # 1、使用queue实现进程通信
# def f(q):
#     print("（%s）进程开始放入数据...." % multiprocessing.current_process().pid)
#     q.put('Python')
#
#
# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#     p = multiprocessing.Process(target=f, args=(q,))
#     p.start()
#     print('(%s) 进程开始取出数据。。。' % multiprocessing.current_process().pid)
#     print(q.get())
#     p.join()

# 2、使用pipe 实现进程通信
def f(conn):
    print("（%s）进程开始发送数据...." % multiprocessing.current_process().pid)
    conn.send('Python')


if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(child_conn,))
    p.start()
    print('(%s) 进程开始接收数据。。。' % multiprocessing.current_process().pid)
    print(parent_conn.recv())

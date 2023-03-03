"""
    14.9.1 使用fork创建新进程
"""
import os

print('父进程（%s）开始执行' % os.getpid())
pid = os.fork()
print("进入进程：%s " % os.getpid())
if pid == 0:
    print("子进程，其id为（%s），父进程ID为（%s）" % (os.getpid(), os.getppid()))
else:
    print("我(%s)创建的子进程ID为：(%s)." % (os.getpid(), pid))
print("进程结束：%s" % os.getpid())

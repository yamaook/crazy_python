"""
    10.2 os模块
        获取程序运行所在操作系统的相关信息
"""
import os

print(os.__all__)
print(os.name)
print(os.getenv('PYTHONPATH'))
print(os.getlogin())
print(os.getpid())
print(os.getppid())
print(os.cpu_count())
print(os.sep)
print(os.pathsep)
print(os.linesep)
print(os.urandom(3))

# 与进程有关的函数
print("-----------------------")
os.system('ls')
# os.startfile('hh.txt')#windows系统才能用
os.spawnl(os.P_NOWAIT, '/Applications/QQ.app/Contents/MacOS/QQ', ' ')
os.execl('/usr/local/bin/python3.9', ' ', 'test.py', 'i')

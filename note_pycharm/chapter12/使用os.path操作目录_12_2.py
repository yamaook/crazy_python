"""
    12.2 使用os.path操作目录
        操作系统的目录本身
"""
import os
import time

print(os.path.abspath('abc.txt'))
print(os.path.commonprefix(['/usr/lib', '/usr/local/lib']))
print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))

print(os.path.dirname('abc/xyz/README.txt'))
print(os.path.exists('abc/xyz/README.txt'))

print(time.ctime(os.path.getatime('文件io_12_1.py')))
print(time.ctime(os.path.getmtime('文件io_12_1.py')))
print(time.ctime(os.path.getctime('文件io_12_1.py')))

print(os.path.getsize('使用os.path操作目录_12_2.py'))

print(os.path.isfile('文件io_12_1.py'))
print(os.path.isdir('使用os.path操作目录_12_2.py'))
print(os.path.samefile('使用os.path操作目录_12_2.py', './使用os.path操作目录_12_2.py'))

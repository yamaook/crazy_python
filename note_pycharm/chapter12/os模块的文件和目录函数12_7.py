"""
    12.7 os模块的文件和目录函数
        12.7.1 与目录相关的函数

"""
import os

# print(os.getcwd())
# os.chdir('../chapter12')
# print(os.getcwd())
#
# # 创建目录
# path = 'my_dir'
# os.mkdir(path, 0o755)
# path = 'abc/xyz/wawa'
# os.makedirs(path, 0o755)

# # 删除目录
# path = 'my_dir'
# os.rmdir(path)
# path = 'abc/xyz/wawa'
# os.removedirs(path)

# 重命名
# path = 'my_dir'
# os.rename(path, 'your_dir')
# path = 'abc/xyz/wawa'
# os.renames(path, 'foo/bar/haha')

"""
    12.7.2 与权限相关的函数
"""
import os, sys, stat

ret = os.access('.', os.F_OK | os.R_OK | os.W_OK | os.X_OK)
print("返回值：", ret)
ret = os.access('_test.txt', os.F_OK | os.R_OK | os.W_OK)
print("返回值：", ret)

os.chmod('a_test.txt', stat.S_IREAD)
ret = os.access('a_test.txt', os.W_OK)
print(ret)

"""
    12.7.3 与文件访问相关的函数
"""
f = os.open('new.txt', os.O_RDWR | os.O_CREAT)
len1 = os.write(f, '水晶探底英语月，\n'.encode('utf-8'))
len2 = os.write(f, '情绪风中比干哼。\n'.encode('utf-8'))
os.lseek(f, 0, os.SEEK_SET)
data = os.read(f, len1 + len2)
print(data)
print(data.decode('utf-8'))
os.close(f)

os.symlink('c_test.txt', 'tt')
os.link('c_test.txt', 'dst')

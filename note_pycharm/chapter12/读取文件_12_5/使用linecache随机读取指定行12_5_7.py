"""
    12.5.7 使用linecache随机读取指定行
"""
import linecache
import random

print(linecache.getline(random.__file__, 3))
print(linecache.getline('使用linecache随机读取指定行12_5_7.py', 3))
print(linecache.getline('info.txt', 2))

"""
    12.3 使用fnmatch处理文件名匹配
        文件存不存在无所谓，主要匹配文件名
"""
from pathlib import *
import fnmatch

for file in Path('.').iterdir():
    if fnmatch.fnmatch(file, '*_12_*.py'):
        print(file)

names = ['a.py', 'b.py', 'c.py', 'd.py']
sub = fnmatch.filter(names, '[ac].py')
print(sub)

print(fnmatch.translate('?.py'))
print(fnmatch.translate('[ac].py'))
print(fnmatch.translate('[a-c].py'))

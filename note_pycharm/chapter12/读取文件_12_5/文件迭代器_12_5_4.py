"""
 12.5.4 文件迭代器

"""
import sys

f = open('test.txt', 'r', True, 'utf-8')
for line in f:
    print(line, end='')
f.close()

print(list(open('test.txt', 'r', True, 'utf-8')))

# sys.stdin 类文件对象
for line in sys.stdin:
    print('用户输入：', line, end='')


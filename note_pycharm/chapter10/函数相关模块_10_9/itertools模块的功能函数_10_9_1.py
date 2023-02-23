"""
10.9 函数相关模块
    支持函数式编程
    10.9.1 itertools模块的功能函数
        包含了一些生成迭代器的函数。
"""
import itertools as it

# 生成无限迭代器的三个函数
for e in it.count(10, 3):
    print(e)
    if e > 20:
        break
print('-------------')
my_counter = 0
for e in it.cycle(['Python', 'Kotlin', 'Swift']):
    print(e)
    my_counter += 1
    if my_counter > 7:
        break
print('------------')
for e in it.repeat('Python', 3):
    print(e)

print('\n------------------')
for e in it.accumulate(range(6)):
    print(e, end=', ')
print('\n------------------')

print('\n------------------')
print('\n------------------')
print('\n------------------')
print('\n------------------')
print('\n------------------')
print('\n------------------')
print('\n------------------')
print('\n------------------')


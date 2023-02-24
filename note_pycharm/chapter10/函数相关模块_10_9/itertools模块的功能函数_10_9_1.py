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

print('\n-------常用迭代器函数-----------')
for e in it.accumulate(range(6)):
    print(e, end=', ')
print('\n------------------')
for e in it.accumulate(range(1, 6), lambda x, y: x * y):
    print(e, end=', ')
print('\n------------------')
for e in it.chain(['a', 'b'], ['Kotlin', 'Swift']):
    print(e, end=', ')
print('\n------------------')
for e in it.compress(['a', 'b', 'Kotlin', 'Swift'], [0, 1, 1, 0]):
    print(e, end=', ')
print('\n------------------')
for e in it.dropwhile(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')

print('\n------------------')
for e in it.takewhile(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')
print('\n------------------')
for e in it.filterfalse(lambda x: len(x) < 4, ['a', 'b', 'Kotlin', 'x', 'y']):
    print(e, end=', ')
print('\n------------------')
for e in it.starmap(pow, [(2, 5), (3, 2), (10, 3)]):
    print(e, end=', ')
print('\n------------------')
for e in it.zip_longest('ABCD', 'xy', fillvalue='-'):
    print(e, end=', ')
print('\n---------排列组合迭代器---------')
for e in it.product('AB', 'CD'):
    print(''.join(e), end=' ')
print('\n------------------')
for e in it.product('AB', repeat=2):
    print(''.join(e), end=' ')
print('\n------------------')
for e in it.permutations('ABCD', 2):
    print(''.join(e), end=' ')

print('\n------------------')
for e in it.combinations('ABCD', 2):
    print(''.join(e), end=' ')

print('\n------------------')
for e in it.combinations_with_replacement('ABCD', 2):
    print(''.join(e), end=' ')

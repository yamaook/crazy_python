"""
10.7 容器相关类
"""
"""
    10.7.1 set 和 frozenset
"""
print(
    [e for e in dir(set) if not e.startswith('_')]
)
c = {'白骨精'}
c.add('孙悟空')
c.add(6)
print('c的集合元素个数为：', len(c))
c.remove(6)
print('c的集合元素个数为：', len(c))
print('c集合是否包含孙悟空字符串', '孙悟空' in c)
c.add('轻量级java EE企业应用实战')
print('c集合的元素：', c)
books = set()
books.add('轻量级java EE企业应用实战')
books.add("疯狂java讲义")
print("books集合的元素", books)

print("books是不是c的子集：", books.issubset(c))
print("books集合是否为c的子集合：", books <= c)

print("c集合是否包含books集合", c.issuperset(books))
print("c集合是否包含books集合", c >= books)

result1 = c - books
print(result1)
result2 = c.difference(books)
print(result2)
c.difference_update(books)
print("c集合的元素为：", c)
c.clear()
print(c)
d = {'疯狂java讲义', '疯狂python讲义', '疯狂kotlin讲义'}
print('d集合的元素：', d)
inter1 = d & books
print(inter1)
inter2 = d.intersection(books)
print(inter2)
d.intersection_update(books)
print(d)
e = set(range(5))
f = set(range(3, 7))
print('e集合的元素：', e)
print('f集合的元素：', f)

xor = e ^ f
print('e和f执行异或的结果', xor)
un = e.union(f)
print('e和f执行并集的结果', un)
e.update(f)
print('e集合的元素：', e)
# frozenset
print(
    [e for e in dir(frozenset) if not e.startswith('_')]
)
# set中添加frozenset
s = set()
frozen_s = frozenset('Kotlin')
s.add(frozen_s)
print('s集合的元素----', s)
sub_s = {'python'}
# s.add(sub_s)
print(s)

"""
10.7.2 双端队列deque
"""
from collections import deque

print(
    [e for e in dir(deque) if not e.startswith('_')]
)
# 双端队列当栈
stack = deque(('Kotlin', 'Python'))
stack.append('Erlang')
stack.append('Swift')
print('stack中的元素', stack)
print(stack.pop())
print(stack.pop())
print(stack)
# 队列
q = deque(('Kotlin', 'Python'))
q.append('Erlang')
q.append('Swift')
print('q中的元素', q)
print(q.popleft())
print(q.popleft())
print(q)
print("---------rotate------------------------")
p = deque(range(5))
print('p中的元素为', p)
p.rotate()
print('p中元素', p)
p.rotate()
print('p中元素', p)

"""
10.7.3 python的堆操作
"""
print("---------堆操作------------------------")
import heapq

print(heapq.__all__)
from heapq import *

my_data = list(range(10))
my_data.append(0.5)
print("my_data的数据为：", my_data)
heapify(my_data)
print("应用堆之后my_data的元素：", my_data)
heappush(my_data, 7.2)
print("添加7.2之后my_data的元素：", my_data)
print(heappop(my_data))
print(heappop(my_data))
print("弹出两个最小元素之后my_data的元素：", my_data)
print(heapreplace(my_data, 8.1))
print("replace之后my_data的元素：", my_data)
print("my_data最大的3个元素是：", nlargest(3, my_data))
print("my_data最小的4个元素是：", nsmallest(4, my_data))

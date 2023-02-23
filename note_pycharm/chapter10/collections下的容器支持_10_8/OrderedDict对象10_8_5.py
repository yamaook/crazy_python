"""

10.8.5 OrderedDict对象
    dict的子类，可以维护添加key-value对的顺序。
"""
from collections import OrderedDict

dx = OrderedDict(b=5, c=2, a=7)
print(dx)
d = OrderedDict()
d['Python'] = 89
d['Swift'] = 92
d['Kotlin'] = 97
d['Go'] = 87
for k, v in d.items():
    print(k, v)

my_data = {'Python': 20, 'Swift': 32, 'Kotlin': 43, 'Go': 25}
d1 = OrderedDict(sorted(my_data.items(), key=lambda t: t[0]))
d2 = OrderedDict(sorted(my_data.items(), key=lambda t: t[1]))
print(d1)
print(d2)
print(d1 == d2)

d = OrderedDict.fromkeys('abcde')
print(d)
d.move_to_end('b')
print(d)
d.move_to_end('b', last=False)
print(d)
print(d.popitem()[0])
print(d.popitem(last=False)[0])

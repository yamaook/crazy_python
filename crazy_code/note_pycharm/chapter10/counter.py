"""
10.8.2 Counter对像
"""

from collections import Counter

c1 = Counter()
c2 = Counter('hannah')
print(c2)
c3 = Counter(['Python', 'Swift', 'Swift', 'Python', 'Kotlin', 'Python'])
print(c3)
c4 = Counter({'red': 4, 'blue': 2})
print(c4)
c5 = Counter(Python=4, Swift=8)
print(c5)

print("----------------------------------")
cnt = Counter()
print(cnt['Python'])
for word in ['Swift', 'Swift', 'Python', 'Kotlin', 'Kotlin', 'Go']:
    cnt[word] += 1
print(cnt)
print(list(cnt.elements()))
chr_cnt = Counter('abracadabra')
print(chr_cnt.most_common(3))
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)
e = Counter({'x': 2, 'y': 3, 'z': -4})
del e['y']
print(e)
print(e['w'])
del e['w']
print(e['w'])

print('------------------------------------')
c = Counter(Pyhon=4, Swift=2, Kotlin=3, Go=-2)
print(sum(c.values()))
print(list(c))
print(set(c))
print(dict(c))
list_of_pairs = c.items()
print(list_of_pairs)
c2 = Counter(list_of_pairs)
print(c2)
print(c.most_common()[:-4:-1])
c.clear()
print(c)
c = Counter(a=3, b=1, c=-1)
d = Counter(a=1, b=-2, d=3)
print(c+d)
print(c-d)
Counter({'a':2})


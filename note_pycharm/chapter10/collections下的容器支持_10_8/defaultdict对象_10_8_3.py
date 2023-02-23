"""
    10.8.3 defaultdict对象
        dict的子类，可以为不存在的key生成value

"""
from collections import defaultdict

my_dict = {}
my_defaultdict = defaultdict(int)
print(my_defaultdict['a'])
# print(my_dict['a'])

s = [('Python', 1), ('Swift', 2), ('Python', 3), ('Swift', 4), ('Python', 9)]
d = {}
# 使用dict
for k, v in s:
    d.setdefault(k, []).append(v)
print(list(d.items()))

# 使用defaultdict
d2 = defaultdict(list)
for k, v in s:
    d2[k].append(v)
print(list(d2.items()))

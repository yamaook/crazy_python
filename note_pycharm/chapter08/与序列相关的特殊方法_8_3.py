"""
    8.3 与序列相关的特殊方法
        实现符合序列要求的特殊方法，可以实现自己的序列。

        8.3.1 序列相关方法
"""


# 自定义一个字符串序列
def check_key(key):
    if not isinstance(key, int): raise TypeError("索引必须是整数值")
    if key < 0: raise IndexError("索引必须是非负整数")
    if key >= 26 ** 3: raise IndexError("索引不能超过%s" % 26 ** 3)


class StringSeq:
    def __init__(self):
        self.__changed = {}
        self.__deteled = []

    def __len__(self):
        return 26 ** 3

    def __getitem__(self, item):
        check_key(item)
        if item in self.__changed:
            return self.__changed[item]
        if item in self.__deteled:
            return None
        three = item // (26 * 26)
        two = (item - three * 26 * 26) // 26
        one = item % 26
        return chr(65 + three) + chr(two + 65) + chr(65 + one)

    def __setitem__(self, key, value):
        check_key(key)
        self.__changed[key] = value

    def __delitem__(self, key):
        check_key(key)
        if key not in self.__deteled: self.__deteled.append(key)
        if key in self.__changed: del self.__changed[key]


sq = StringSeq()
print(len(sq))
print(sq[26 * 26])
print(sq[1])
sq[1] = 'fkit'
print(sq[1])
del sq[1]
print(sq[1])
sq[1] = 'crazyit'
print(sq[1])

"""
    8.3.2实现迭代器
        实现迭代器需要实现两个方法即可:
            __iter__()：返回一个迭代器，迭代器包含一个__next__()方法。
            __reversed__():为reverse()反转函数提供支持。
        iter()函数：
            将列表元组等转换成迭代器。
"""


# 定义一个迭代器
class Fibs:
    def __init__(self, len):
        self.first = 0
        self.sec = 1
        self.__len = len

    def __next__(self):
        if self.__len == 0:
            raise StopIteration
        self.first, self.sec = self.sec, self.first + self.sec
        self.__len -= 1
        return self.first

    def __iter__(self):
        return self


fibs = Fibs(10)
print(next(fibs))
for el in fibs:
    print(el, end=' ')
# 将列表转换为迭代器
print()
my_iter = iter([2, 'fkit', 4])
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print('----------')
"""
    8.3.3 扩展列表、元组和字典
    
"""


# 定义一个新的字典类
class ValueDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def getkeys(self, val):
        result = []
        for key, value in self.items():
            if value == val:
                result.append(key)
        return result


my_dict = ValueDict(语文=92, 数学=89, 英语=92)
print(my_dict.getkeys(92))
my_dict['编程'] = 92
print(my_dict.getkeys(92))

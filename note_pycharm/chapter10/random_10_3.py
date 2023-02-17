"""
    10.3 random
        包含生成伪随机数的各种功能变量和函数
"""
import random

print(random.__all__)
print(random.random())
print(random.uniform(2.5, 10.0))
# 指数分布的伪随机浮点数
print(random.expovariate(1 / 5))
print(random.randrange(10))
print(random.randrange(0, 101, 2))
print(random.choice(['python', 'swift', 'kotlin']))
book_list = ['python', 'swift', 'kotlin']
random.shuffle(book_list)
print(book_list)
print(random.sample([10, 20, 30, 40, 50], k=4))

print("====================")
import collections

print(random.choices(['python', 'swift', 'kotlin'], [5, 5, 1], k=6))
deck = collections.Counter(tens=16, low_cards=36)
seen = random.sample(list(deck.elements()), k=20)
print(seen.count('tens') / 20)

"""
    5.1.4 多个返回值
        函数有多个返回值：
            1、包装成列表返回
            2、直接返回多个指：自动封装成元组
"""


def sum_and_avg(a_list):
    a_sum = 0
    count = 0
    for e in a_list:
        if isinstance(e, int) or isinstance(e, float):
            count += 1
            a_sum += e
    return a_sum, a_sum / count


my_list = [20, 15, 2.8, 'a', 35, 5.9, -1.8]
a_tuple = sum_and_avg(my_list)
print(a_tuple)
# 序列解包
a, avg = a_tuple
print(a)
print(avg)

"""
    15.2.3 使用urllib.request读取资源
"""
from urllib.request import *

# result = urlopen('https://fanyi.baidu.com/?aldtype=16047#en/zh/hurry')
# data = result.read(326)
# print(data.decode('utf-8'))
#
# with urlopen('https://fanyi.baidu.com/?aldtype=16047#en/zh/hurry') as f:
#     data = f.read(326)
#     print(data.decode('utf-8'))

with urlopen(url='http://localhost:8001/cgi-bin/test.py', data='测试数据'.encode('utf-8')) as f:
    print(f.read().decode('utf-8'))


"""
    15.2.3 使用urllib.request读取资源
"""
from urllib.request import *

# 1、
# result = urlopen('https://fanyi.baidu.com/?aldtype=16047#en/zh/hurry')
# data = result.read(326)
# print(data.decode('utf-8'))
#
# with urlopen('https://fanyi.baidu.com/?aldtype=16047#en/zh/hurry') as f:
#     data = f.read(326)
#     print(data.decode('utf-8'))


# # 2、通过data属性给url发送数据
# with urlopen(url='http://localhost:8000/cgi-bin/test.py', data='测试数据'.encode('utf-8')) as f:
#     print(f.read().decode('utf-8'))

# 3、发送get请求
import urllib.parse

params = urllib.parse.urlencode({'name': 'fkit', 'password': '123888'})
url = 'http://localhost:8080/test/get.jsp?%s' % params
print(url, end=' ')
with urlopen(url=url) as f:
    print(f.read().decode('UTF-8'))

# 4、发送post请求
params = urllib.parse.urlencode({'name': '疯狂软件', 'password': '123888'})
params = params.encode('utf-8')
with urlopen('http://localhost:8080/test/post.jsp', data=params) as f:
    print(f.read().decode('utf-8'))

# 5、Request对象发送put请求
params = 'put请求数据'.encode('utf-8')
req = Request(url='http://localhost:8080/test/post.jsp', data=params, method='PUT')
with urlopen(req) as f:
    print(f.status)
    print(f.read().decode('utf-8'))

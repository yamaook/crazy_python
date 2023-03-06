"""
    15.2.2 使用urllib.parse子模块

"""
from urllib.parse import *

# 用urlparse()解析url字符串
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit#frag')
print(result)
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('主机:', result.hostname)
print('端口:', result.port)
print('资源路径:', result.path, result[2])
print('参数:', result.params, result[3])
print('查询字符串:', result.query, result[4])
print('fragment:', result.fragment, result[5])
print(result.geturl())
print('--------------------------------------')

# 使用urlunparse()生成URL对象
result = urlunparse(('http', 'www.crazyit.org:80', 'index.php', 'yeeku', 'name=fkit', 'frag'))
print('URL为：', result)
print('-----------------------')

# 解析//开头的url
result = urlparse('//www.crazyit.org:80/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('资源路径:', result.path, result[2])
print('-----------------------')
# 解析没有scheme和//和端口号 的URL
result = urlparse('www.crazyit.org/index.php')
print('scheme:', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('资源路径:', result.path, result[2])
print('-----------------------')

# 解析查询字符串
result = parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
result = parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
# 反解析查询字符串
print(urlencode(result))
print('---------------------')

# urljoin()函数拼接两个url
# 被拼接的url不以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result)
result = urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result)
# 被拼接的url以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', '/help.html')
print(result)
# 被拼接的url以双斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', '//help.html')
print(result)

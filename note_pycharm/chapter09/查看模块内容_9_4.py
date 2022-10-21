'''
    9.4.1 模块包含什么
'''
import string

print(dir(string))
a = [e for e in dir(string) if not e.startswith('_')]
print(a)
print(string.__all__)

"""
    9.4.2 使用__doc__属性查看文档
"""
help(string.capwords)
print(string.capwords('abc    xyz'))
print(string.capwords('abc;xyz', sep=';'))
print(string.capwords.__doc__)

"""
    9.4.3 使用__file__属性查看模块的源文件路径
"""
print(string.__file__)
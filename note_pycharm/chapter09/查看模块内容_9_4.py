'''
    9.4.1 模块包含什么
        如何查看模块中包含的可以使用的程序单元
            列表推倒式
            __all__变量
'''
import string

print(dir(string))
a = [e for e in dir(string) if not e.startswith('_')]
print(a)
print(string.__all__)

print("------------------------")
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

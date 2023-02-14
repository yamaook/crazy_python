"""
    9.1 模块化编程
        以模块化的方式来组织项目的源代码

        9.1.1 导入模块的语法
            1、导入整个模块：导入模块
                import m1 as name1,m2 as name2,...
            2、导入模块中指定成员：导入成员
                from m1 import 成员名1 as name1,成员名2 as name2,...
                from module import * 导入指定模块所有成员。



"""
"""
    import 语法
"""
# 导入整个模块
import sys

print(sys.argv[0])

# 为模块指定个别名
import sys as s

print(s.argv[0])

# 导入多个模块
import sys, os

print(sys.argv[0])
print(os.sep)

# 导入多模块指定别名
import sys as s, os as o

print(s.argv[0])
print(o.sep)
print('------------------------------')
"""
    from import 语法
"""
# 导入模块指定成员
from sys import argv

print(argv[0])
# 为成员指定别名
from sys import argv as v

print(v[0])
# 导入多个成员
from sys import argv, version

print(argv[0])
print(version)
# 导入多个成员指定别名
from sys import argv as v, version as n

print(v[0])
print(n)
# 一次导入模块内所有成员
from sys import *

print(argv[0])
print(version, "===")
print('>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<')
"""
    9.1.2定义模块
        1、模块就是python程序，任何python程序都可作为模块导入。
        2、使用模块好处：
            提供更好的复用。
        3、模块文件的文件名就是模块名。
"""
import module1

module1.say_hi('jj')

"""
    9.1.3 为模块编写说明文档
        模块开始处定义一个字符串直接量即可。
        模块__doc__属性可以访问到。
"""
print('>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<')

print(module1.__doc__, end='')
print()
print('>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<')

"""
    9.1.4 为模块编写测试代码
        模块内置的__name__变量。
"""

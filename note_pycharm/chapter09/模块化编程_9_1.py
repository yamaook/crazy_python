"""
 9.1.1 导入模块的语法

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

"""
    9.1.2定义模块
"""
import module1

module1.say_hi('jj')

"""
    9.1.3 为模块编写说明文档
"""
print(module1.__doc__, end='')

"""
    9.1.4 为模块编写测试代码
"""

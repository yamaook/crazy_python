"""
    9.2.1 使用环境变量
        python会搜索PYTHONPATH环境变量所指定的多个路径
"""
import module1 as md
import module1 as md

print(md.my_book)
md.say_hi('charlie')
user = md.User('孙悟空')
print(user)
user.walk()
"""
    9.2.2 默认的模块加载路径
"""
import sys, pprint

pprint.pprint(sys.path)

import print_shape

print(print_shape.__doc__)
print(print_shape.print_triangle.__doc__)
print(print_shape.my_list[1])
print_shape.print_triangle(4)

"""
    9.2.3 导入模块的本质
"""
# import fk_module
#
# print("=============")
# print(type(fk_module))
# print(fk_module)
# print(fk_module.name)
# print(fk_module.hello)

from fk_module import name, hello

print("===============")
print(name)
print(hello)
#
# print(fk_module)

"""
    9.2.4 模块的__all__变量
"""
from all_module import *

hello()
world()
# test()没有导入

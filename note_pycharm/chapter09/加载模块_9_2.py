"""
    9.2 加载模块
        为了让python找到模块，有两种方式：
            使用环境变量
            将模块放在默认的模块加载路径下

        9.2.1 使用环境变量

            python会搜索PYTHONPATH环境变量所指定的多个路径。
            重复导入同一个模块，python只会导入一次。
"""
import module1 as md

print(md.my_book)
md.say_hi('charlie')
user = md.User('孙悟空')
print(user)
user.walk()
print('>>>>>>>>>>>>>>>>>')
"""
    9.2.2 默认的模块加载路径
        sys.path代表了python默认模块加载路径。
        pprint打印结果更友好。
        lib/site-packages这个默认模块加载路径一般存放python扩展模块和包。
"""
import sys, pprint

pprint.pprint(sys.path)

# import print_shape
#
# print(print_shape.__doc__)
# print(print_shape.print_triangle.__doc__)
# print(print_shape.my_list[1])
# print_shape.print_triangle(4)


"""
    9.2.3 导入模块的本质
        1、import module本质：
            将代码全部加载到内存并执行，将模块内容赋值给模块同名变量，变量类型为module，
                而该模块中的程序单元都相当于module对象的成员。
        2、from module import name 本质：
            将代码全部加载到内存并执行，然后只导入指定变量、函数等成员单元，不会将整个模块导入。
        3、__pycache__文件夹：
            保存模块编译生成的字节码，用于提升模块运行效率。
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
        1、from module import * 默认导入该模块中所有不以下划线开头的程序单元。
            如果设置了__all__列表变量，则只能导入列表中的程序单元。
        2、import module 和 from module import 成员：
            不受__all__变量限制。
"""
from all_module import *

hello()
world()
# test()没有导入

"""
    9.3 使用包

        问题：实际应用的模块非常大，如果都定义在一个文件中，不利于模块化开发。

        9.3.1 什么是包
            1、一个文件夹，包含__init__.py文件，用于包含多个模块源文件
            2、包的本质依然是模块
            3、包的作用是包含多个模块,包也可以包含包。

        9.3.2 定义包
            1、创建包：
                1、创建文件夹，该文件夹的名字就是该包的包名。
                2、添加__init__.py文件。
            2、导入包时，执行了__init__.py文件
            3、导入包的本质：
                加载并执行__init__文件，然后将整个文件内容赋值给包同名变量，该变量是module类型。
"""
import first_package

print("========")
print(first_package.__doc__)
print(type(first_package))
print(first_package)

"""
    9.3.3 导入包内成员
        包内包含的模块，就是包的成员。
"""
import fk_package
import fk_package.print_shape
from fk_package import billing
import fk_package.artthmetic_chart

fk_package.print_shape.print_blank_triangle(5)
im = billing.Item(4.5)
print(im)
fk_package.artthmetic_chart.print_multiple_chart(5)

fk_package.print_blank_triangle(3)
im = fk_package.Item(3.4)
print(im)
fk_package.print_multiple_chart(5)

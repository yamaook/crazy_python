"""
9.3.1 什么是包
    包的作用是包含多个模块，包的本质依然是模块，因此包又可以包含包。
9.3.2 定义包
"""
import first_package

print("========")
print(first_package.__doc__)
print(type(first_package))
print(first_package)

"""
    9.3.3 导入包内成员
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

"""
    10 常见模块
        10.1 sys模块
            代表了python解释器，获取和python解释器相关的信息
"""
import sys
import pprint

a = [e for e in dir(sys) if not e.startswith('_')]
# pprint.pprint(a)

# 本地字节序
print(sys.byteorder)
# python解释器的版权信息
print(sys.copyright)
# 显示解释器在磁盘上的存储路径
print(sys.executable)
# 文件系统保存文件时使用的字符集
print(sys.getfilesystemencoding())
# 整数支持的最大值
print(sys.maxsize)
# 显示解释器所在平台
print(sys.platform)
# 显示解释器的版本信息
print(sys.version)
# 运行python命令时指定的旗标
print(sys.flags)
# 返回指定对象的引用计数
print(sys.getrefcount(a))
print(sys.modules)
print(sys.stdin)
print('----------10.1----------------')

"""
    10.1.1 获取运行参数
"""
from sys import argv

print(len(argv))
for arg in argv:
    print(arg)
"""
    10.1.2动态修改 模块加载路径
    
"""
print(sys.path)
sys.path.append('/Users/heyanan/mygit/crazy_python/note_pycharm/chapter09')
print(sys.executable)
import all_module

all_module.hello()

"""
    12 文件IO
        12.1 使用pathlib模块操作目录
            purepath:代表并不访问实际文件系统的"纯路径"
            path:代表访问实际文件系统的"真正路径"
"""
"""
    12.1.1 PurePath的基本功能
        1、在不同系统下使用PurePath创建对象，都会生成对应系统的对象
"""
from pathlib import *

pp = PurePath('set.py')
print(type(pp))
pp = PurePath('crazy', 'some/path', 'info')
print(pp)
pp = PurePath(Path('crazyit'), Path('info'))
print(pp)
pp = PureWindowsPath('crazy', 'some/path', 'info')
print(pp)

pp = PurePath()
print(pp)

pp = PurePosixPath('/etc', '/usr', 'lib64')
print(pp)
pp = PureWindowsPath('c:/windows', 'd:info')
print(pp)

pp = PureWindowsPath('c:/windows', '/Program Files')
print(pp)

pp = PurePath('foo//bar')
print(pp)
pp = PurePath('foo/./bar')
print(pp)
pp = PurePath('foo/../bar')
print(pp)
# PurePath对象的比较
print(PurePosixPath('info') == PurePosixPath('INFO'))
print(PureWindowsPath('info') == PureWindowsPath('INFO'))
print(PureWindowsPath('INfo') in {PureWindowsPath('info')})
print(PurePosixPath('D:') < PurePosixPath('c:'))
print(PureWindowsPath('D:') > PureWindowsPath('c:'))
print(PureWindowsPath('crazyit') == PurePosixPath('crazyit'))
# print(PureWindowsPath('crazyit') < PurePosixPath('crazyit'))

pp = PureWindowsPath('abc')
print(pp / 'xyz' / 'wawa')
pp = PurePosixPath('abc')
print(pp / 'xyz' / 'wawa')
pp2 = PurePosixPath('haha', 'hehe')
print(pp / pp2)

pp = PureWindowsPath('abc', 'xyz', 'wawa')
print(str(pp))
pp = PurePosixPath('abc', 'xyz', 'wawa')
print(str(pp))
print('-------------------------------------')

"""
    12.1.2 PurePath的属性和方法
"""

print(PureWindowsPath('c:/Program Files/').drive)
print(PureWindowsPath('/Program Files/').drive)
print(PurePosixPath('/etc').drive)

print(PureWindowsPath('c:/Program Files/').root)
print(PureWindowsPath('c:Program Files/').root)
print(PurePosixPath('/etc').root)

print(PureWindowsPath('c:/Program Files/').anchor)
print(PureWindowsPath('c:Program Files/').anchor)
print(PurePosixPath('/etc').anchor)

pp = PurePath('abc/xyz/wawa/haha')
print(pp.parents[0])
print(pp.parents[1])
print(pp.parents[2])
print(pp.parents[3])
print(pp.parent)

print(pp.name)
pp = PurePath('abc/wawa/bb.txt')
print(pp.name)
pp = PurePath('abc/wawa/bb.txt.tar.zip')
print(pp.suffixes[0])
print(pp.suffixes[1])
print(pp.suffixes[2])
print(pp.suffix)
print(pp.stem)

pp = PurePath('abc', 'xyz', 'wawa', 'haha')
print(pp)
print(pp.as_posix())
# print(pp.as_uri())

pp = PureWindowsPath('d:/', 'Python', 'Python3.6')
print(pp.as_uri())

print(PurePath('a/b.py').match('*.py'))
print(PurePath('/a/b/c.py').match('b/*.py'))
print(PurePath('/a/b/c.py').match('a/*.py'))

pp = PurePosixPath('c:/abc/xyz/wawa')
print(pp.relative_to('c:/'))
print(pp.relative_to('c:/abc'))
print(pp.relative_to('c:/abc/xyz'))

p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_name('fkit.py'))
p = PureWindowsPath('e:/')
# print(p.with_name('fkit.py'))

p = PureWindowsPath('e:/Downloads/pathlib.tar.gz')
print(p.with_suffix('.zip'))
p = PureWindowsPath('README')
print(p.with_suffix('.txt'))

print('----------------------------------------')

"""
    12.1.3 Path的功能和用法
        
"""

p = PosixPath('.')
for x in p.iterdir():
    print(x)

p = Path('../')
for x in p.glob('**/*.py'):
    print(x)

p = Path('/Users/heyanan/mycode')
for x in p.glob('**/duplicate.py'):
    print(x)
print('----------------------')
# 使用path读写文件
p = Path('./a_test.txt')
result = p.write_text(
    """又一个美丽的新世界
    它在远方等我
    那里有天真的孩子
    还有姑娘的酒窝""", encoding='GBK')
print(result)

content = p.read_text(encoding='GBK')
print(content)

bb = p.read_bytes()
print(bb)


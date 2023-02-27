"""
12.6 写文件
    12.6.1 文件指针的概念

"""
f = open('a_test.txt', 'rb')
print(f.tell())
f.seek(3)
print(f.tell())
print(f.read(1))
print(f.tell())
f.seek(5)
print(f.tell())
f.seek(5, 1)
print(f.tell())
f.seek(-10, 2)
print(f.tell())
print(f.read(1))
f.seek(0)
print(f.tell())
print(f.read(1))
print(f.tell())
f.close()
print('--------------------------------------')
"""
    12.6.2 输出内容
"""
import os

f = open('b_test.txt', 'w+')
f.write('我爱Python' + os.linesep)
f.writelines(('土门比生煎，' + os.linesep,
              '星缘肚难以。' + os.linesep,
              '是一夜城下，' + os.linesep,
              '总司室友款。' + os.linesep))

# 二进制形式

f = open('c_test.txt', 'wb+')
f.write(('我爱Python' + os.linesep).encode('GBK'))
f.writelines(
    (
        ('土门比生煎，' + os.linesep).encode('GBK'),
        ('星缘肚难以。' + os.linesep).encode('GBK'),
        ('是一夜城下，' + os.linesep).encode('GBK'),
        ('总司室友款。' + os.linesep).encode('GBK')
    )
)
f.close()

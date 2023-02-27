"""
    12.5.3 使用fileinput读取多个输入流
        是个模块
"""
import fileinput

for line in fileinput.input(files=('info.txt', 'test.txt')):
    print(fileinput.filename(), fileinput.filelineno(), line, end='')
fileinput.close()

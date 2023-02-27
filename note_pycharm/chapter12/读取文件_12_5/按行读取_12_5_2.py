"""
    12.5.2 按行读取
"""
f = open('test.txt', 'r', True, 'utf-8')
print(f.encoding)
while True:
    line = f.readline()
    if not line: break
    print(line, end='')
f.close()
print('\n-----------')
f = open('test.txt', 'r', True, 'utf-8')
for i in f.readlines():
    print(i, end='')
f.close()

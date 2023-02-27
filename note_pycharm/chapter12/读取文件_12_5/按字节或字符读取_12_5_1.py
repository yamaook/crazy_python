"""
    12.5.1 按字节或字符读取

"""
# read有参数
f = open('test.txt', 'r', True)
while True:
    ch = f.read(1)
    if not ch:
        break
    print(ch, end='')
f.close()
# read没参数
f = open('test.txt', 'r', True)
print(f.read())
f.close()

# 字符集
f = open('test.txt', 'rb', 3)
print(f.read().decode('utf-8'))
f.close()

f = open('test.txt', 'r', True, 'utf-8')
while True:
    ch = f.read(1)
    if not ch:
        break
    print(ch, end='')
f.close()

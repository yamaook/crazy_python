"""
    12.8 使用tempfile模块生成临时文件和临时目录

"""
import tempfile

fp = tempfile.TemporaryFile()
print(fp.name)
fp.write('两情若是久长时，'.encode('utf-8'))
fp.write('又岂在朝朝暮暮。'.encode('utf-8'))
fp.seek(0)
print(fp.read().decode('utf-8'))
fp.close()

with tempfile.TemporaryFile() as fp:
    fp.write(b'I love you ')
    fp.seek(0)
    print(fp.read())

with tempfile.TemporaryDirectory() as tmpdirname:
    print("创建临时目录", tmpdirname)

"""
10.5.1 json的基本知识
    1、把python字符串连同最外层引号全部反转义，再在外面套一层引号，就是json字符串
    2、把json字符串去掉最外层引号，直接转义就得到python字符串
    3、自定义恢复函数可以将json类型转换成python特殊类型
    4、扩展JSONEncoder类可以将python特殊类型转换成json字符串
"""
"""
    10.5.2 Python的JSON支持
"""
import json

print(json.__all__)

print("============encode=================")
# python对象->json字符串
s = json.dumps(['yeeku', {'favorite': ('coding', None, 'game', 25)}])
print(s)
# python字符串->json字符串
s2 = json.dumps("\"foo\bar")
# 把python字符串连同最外层引号全部反转义，再在外面套一层引号，就是json字符串
print(s2, '实际的jason字符串为：', '\"\\"foo\\bar\"')
# python字符串->json字符串
s3 = json.dumps("\\")
print(s3, '实际的jason字符串为：', '\"\\\\\"')
# dict->json
s4 = json.dumps({'c': 0, 'b': 0, 'a': 0}, sort_keys=True)
print(s4)
# list->json
s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators=(',', ':'))
print(s5)
# json带缩进
s6 = json.dumps({'python': 5, 'kotlin': 7}, sort_keys=True, indent=4)
print(s6)
# JSONEncoder类的使用效果同dumps
s7 = json.JSONEncoder().encode({'names': ('孙悟空', '齐天大圣')})
print(s7)
# dump使用d
f = open('a.json', 'w')
json.dump(['kotlin', {'python': 'excellent'}], f)
print("===============decode======================")
# json字符串->列表
result1 = json.loads('["yeeku", {"favorite": ["coding", null, "game", 25]}]')
print(result1)
# json字符串->python字符串("\"foo\"bar")
result2 = json.loads('"\\"foo\\"bar"')
# 把json字符串去掉最外层引号，直接转义就得到python字符串
print(result2, "实际的python字符串为：", "\"foo\"bar")


# 自定义转换函数
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


# 自定义恢复函数
result3 = json.loads('{"__complex__":true,"real":1,"imag":2}', object_hook=as_complex)
print(result3)

f = open('a.json')
# 从文件流恢复
result4 = json.load(f)
print(result4)

print("=========扩展JSONEncoder====================")


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {"__complex__": 'true', "real": obj.real, "imag": obj.imag}
        return json.JSONEncoder.default(self, obj)


# 两种使用子类的方式
s1 = json.dumps(2 + 1j, cls=ComplexEncoder)
print(s1)
s2 = ComplexEncoder().encode(2 + 1j)
print(s2)

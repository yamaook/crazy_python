"""
10.6.1 python的正则表达式支持
"""
import re

print(re.__all__)
# compile
print("=========compile========")
# 使用正则表达式对象
p = re.compile('abc')
print(p.search("www.abc.com"))
# 直接使用re模块函数
print(re.search('abc', 'www.abc.com`'))
# macth
print("=========match========")
m1 = re.match('www', 'www.fkit.com')
print(m1.span())
print(m1.group())
print(re.match('fkit', 'www.fkit.org'))
# search
print("=========search========")
m2 = re.search('www', 'www.fkit.org')
print(m2.span())
print(m2.group())
#
m3 = re.search('fkit', 'www.fkit.com')
print(m3.span())
print(m3.group())
# findall
print("=========findall对比finditer========")
print(re.findall('fkit', 'FkIt is very good,Fkit.org is my favorite', re.I))
# finditer
it = re.finditer('fkit', 'FkIt is very good,Fkit.org is my favorite', re.I)
for i in it:
    # 迭代器的元素是匹配对象
    print(str(i.span()) + '-->' + i.group())

# sub
print("=========sub========")
my_date = '2008-08-18'
print(re.sub(r'-', '/', my_date))
print(re.sub(r'-', '/', my_date, 1))


def fun(matched):
    value = "《疯狂" + (matched.group('lang')) + "讲义》"
    return value


s = 'Python很好，Kotlin也很好'
# 指定使用fun函数作为替换内容
print(re.sub(r'(?P<lang>\w+)', fun, s, flags=re.A))

# split返回分割后子串的列表
print("=========split========")
print(re.split(',', 'fkit,fkjava,crazyit'))
print(re.split(',', 'fkit,fkjava,crazyit', 1))
print(re.split('a', 'fkit,fkjava,crazyit'))
print(re.split('x', 'fkit,fkjava,crazyit'))

# escape
print("=========escape========")
# 转义模式中的特殊字符。
# 如果要匹配可能包含正则表达式元字符的任意文字字符串，则此选项非常有用。例如：
print(re.escape(r'www.crazyit.org is good, i love it!'))
print(re.escape(r'A-Zand0-9?'))

# _sre.SRE_Pattern正则表达式类，使用正则表达式的方法执行匹配
print("==================_sre.SRE_Patter=================")
pa = re.compile('fkit')
print(pa.match('www.fkit.org', 4).span())
print(pa.match('www.fkit.org', 4, 6))
print(pa.fullmatch('www.fkit.org', 4, 8).span())
# _sre.SRE_Match
print("==================_sre.SRE_Match=================")
m = re.search(r'(fkit).(org)', r"www.fkit.org is a good domain")
print(m.group(0))
print(m[0])
print(m.span(0))
print(m.group(1))
print(m[1])
print(m.span(1))
print(m.group(2))
print(m[2])
print(m.span(2))
print(m.groups())

# groupdict()
print("==========groupdict()==============")
m2 = re.search(r'(?P<prefix>fkit).(?P<suffix>org)', r"www.fkit.org is a good domain")
print(m2.groupdict())
# lastindex
print('=============lastindex=======================')
# 组的序号是由外向内，由左向右排序。但匹配顺序是递归，最外层是最后匹配。
m4 = re.search(r'(a)b', r"ab", 1)
print(m4.lastindex, m4.group(1))
m4 = re.search(r'((a)(b))', r"ab")
print(m4.lastindex, m4.group(1), m4.group(2), m4.group(3))
m4 = re.search(r'((ab))', r"ab")
print(m4.lastindex, m4.group(1), m4.group(2))
m4 = re.search(r'(a)(b)', r"ab")
print(m4.lastindex, m4.group(1), m4.group(2))
print('=============其他属性测试=======================')
# match.pos等属性测试
m = re.search(r'fkit', r"www.fkit.org is a good domain fkit")
p = re.compile(r'(fkit)')
m2 = p.search(r"www.fkit.org is a good domain fkit", 8)
print(m.span(), m.pos, m.endpos)
print(m2.span(), m2.pos, m2.endpos)
print(m2.lastindex)
print(m2.re)
print(m2.string)

"""
10.6.2 正则表达式旗标
"""
print('--------------------10.6.2 旗标-------------------------')
# 旗标re.I
m5 = re.findall(r'fkit', 'FKit is a good domain,FKIT is good', re.I)
print(m5)
# 正则表达式可以换行和注释
a = re.compile(r"""020  #广州的区号
                    -  #中间的短横线
                    \d{8} #8个数值""", re.X)
b = re.compile(r'020-\d{8}')
print(b.search('020-12345678'))

"""
    10.6.3创建正则表达式
"""
print('--------------------10.6.3 创建正则表达式-------------------------')
print(re.fullmatch(r'\u0041\\', 'A\\'))
print(re.fullmatch(r'\u0061\t', 'a\t'))
print(re.fullmatch(r'\?\[', '?['))

print(re.fullmatch(r'c\wt', 'cat'))
print(re.fullmatch(r'c\wt', 'c9t'))
print(re.fullmatch(r'\d\d\d-\d\d\d-\d\d\d\d', '123-456-8888'))

print('---------------10.6.4 子表达式-----------------------------')
print(re.search(r'Windows (95|98|NT|2000)[\w|\s]+\1', 'Windows 98 published in 98'))
print(re.search(r'<(?P<tag>\w+)>\w+</(?P=tag)>', '<h3>xx</h3>'))
print(re.search(r'Windows (?:95|98|NT|2000) [a-z]+', 'Windows 98 published in 98'))
print(re.search(r'(?<=<h1>).+?(?=</h1>)', 'help!<h1>fkit.org</h1>!technology'))
print(re.search(r'(?<=<h1>).+?(?=</h1>)', 'help!<h1><div>fkit</div></h1>!technology'))
print(re.search(r'[a-zA-Z0-9]{3,}(?#username)@fkit\.org', 'sun@fkit.org'))
print(re.search(r'(?i)[a-zA-Z0-9]{3,}(?#username)@fkit\.org', 'sun@FKIT.org'))
print(re.search(r'(?i:[a-zA-Z0-9]){3,}(?#username)@fkit\.org', 'sUn@fkit.org'))
print(re.search(r'(?-i:[a-z0-9]){3,}(?#username)@fkit\.org', 'sun@FKIT.org', re.I))

print('---------------10.6.5 贪婪模式与勉强模式-----------------------------')
# 贪婪模式
print(re.search(r'@.+\.', 'sun@fkit.com.cn'))
# 勉强模式
print(re.search(r'@.+?\.', 'sun@fkit.com.cn'))

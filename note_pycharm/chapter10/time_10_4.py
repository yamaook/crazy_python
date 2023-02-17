"""
10.4 time模块
    包含提供日期、时间功能的类和函数
"""
import time

a = [e for e in dir(time) if not e.startswith('_')]
print(a)

# 时间对象
b = time.struct_time((2018, 5, 2, 8, 0, 30, 3, 1, 0))
print(b)

# 将以秒数代表的时间转换为时间对象，在中国以秒代表的时间是按照1970.1.1.8.0.0计算的。
c = time.localtime(30)
print(c)
# 把时间对象，转换成在中国距1970.1.1.8.0.0的秒
print(time.mktime(c))
print("=====================")

print("将当前时间转换为时间字符串:", time.asctime())
print("将指定时间转换为时间字符串:", time.asctime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))
print("秒数时间转换为时间字符串:", time.ctime(30))

# 当前国际时间
print("秒数时间转换为时间object:", time.gmtime(30))
print("当前时间转换为时间object:", time.gmtime())

# 当前本地时间
print('秒数时间转换为本地时间object:', time.localtime(30))
print('当前时间转换为本地时间object:', time.localtime())
#
print('元组转换成秒时间', time.mktime((2018, 2, 4, 11, 8, 23, 0, 0, 0)))

print("perf", time.perf_counter())
print(time.process_time())
# time.sleep(10)

# 字符串与时间对象的相互转换
print("当前时间转换为指定格式的字符串:", time.strftime('%Y-%m-%d %H:%M:%S'))
st = '2018年3月20日'
print("时间字符串->时间对象", time.strptime(st, "%Y年%m月%d日"))
print(time.time())
print(time.timezone)
print(time.tzname)

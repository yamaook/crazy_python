"""
    13.2.3 使用序列重复执行DML语句

"""
import sqlite3

conn = sqlite3.connect('first.db')
c = conn.cursor()

# c.execute('insert into user_tb values(null,?,?,?)', ('孙悟空', '123456', 'male'))
# c.execute('insert into order_tb values(null,?,?,?,?)', ('鼠标', '34.2', '3', 1))

# # 重复执行一条sql语句
# c.executemany('insert into user_tb values(null,?,?,?)',
#               (
#                   ('sun', '123456', 'male'),
#                   ('bai', '123456', 'female'),
#                   ('zhu', '123456', 'male'),
#                   ('niu', '123456', 'male'),
#                   ('tang', '123456', 'male'),
#               ))


# 重复执行update语句
c.executemany('update user_tb set name=? where _id=?', (
    ('小孙', 2),
    ('小白', 3),
    ('小猪', 4),
    ('小牛', 5),
    ('小唐', 6)))
print('记录被修改的条数：', c.rowcount)
conn.commit()
c.close()
conn.close()

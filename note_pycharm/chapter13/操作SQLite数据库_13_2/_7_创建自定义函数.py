"""
    13.2.7 创建自定义函数
"""
import sqlite3


def reverse_ext(st):
    return '[' + st[::-1] + ']'


conn = sqlite3.connect('first.db')
conn.create_function('enc', 1, reverse_ext)
c = conn.cursor()
c.execute('insert into user_tb values (null,?,enc(?),?)',
          ('贾宝玉', '123456', 'male'))
conn.commit()
c.close()
conn.close()

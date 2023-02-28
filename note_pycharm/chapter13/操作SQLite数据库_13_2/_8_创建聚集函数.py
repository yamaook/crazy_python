"""
    13.2.8 创建聚集函数
"""
import sqlite3


class MinLen:
    def __init__(self):
        self.mini_len = None

    def step(self, value):
        if self.mini_len is None:
            self.mini_len = value
            return
        if len(self.mini_len) > len(value):
            self.mini_len = value

    def finalize(self):
        return self.mini_len


conn = sqlite3.connect('first.db')
conn.create_aggregate('min_len', 1, MinLen)
c = conn.cursor()
c.execute('select min_len(pass) from user_tb')
print(c.fetchone()[0])
conn.commit()
c.close()
conn.close()

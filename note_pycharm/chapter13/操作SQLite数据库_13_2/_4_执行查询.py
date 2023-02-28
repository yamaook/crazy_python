"""
    13.2.4 执行查询
"""
import sqlite3

conn = sqlite3.connect('first.db')
c = conn.cursor()
c.execute('select * from user_tb where _id > ?', (2,))
print('查询返回的记录数：', c.rowcount)
for col in c.description:
    print(col[0], end='\t')
print('\n-------------------------------------')
while True:
    row = c.fetchone()
    if not row:
        break
    print(row)
    print(row[1] + '-->' + row[2])
c.close()
conn.close()

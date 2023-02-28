"""
    13.2.9 创建比较函数

"""
import sqlite3


def my_collate(st1, st2):
    if st1[1:-1] == st2[1:-1]:
        return 0
    elif st1[1:-1] > st2[1:-1]:
        return -1
    else:
        return 1


conn = sqlite3.connect('first.db')
conn.create_collation('sub_cmp', my_collate)
c = conn.cursor()
c.execute('select * from user_tb order by pass collate sub_cmp')
for row in c:
    print(row)
conn.commit()
c.close()
conn.close()

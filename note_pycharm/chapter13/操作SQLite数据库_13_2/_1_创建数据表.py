"""
    13.2.1创建数据表

"""
import sqlite3

print(sqlite3.apilevel)
print(sqlite3.paramstyle)

# 打开或创建一个数据库
conn = sqlite3.connect('first.db')
c = conn.cursor()
c.execute("""
    create table user_tb(
        _id integer primary key autoincrement,
        name text,
        pass text,
        gender text)""")

c.execute('''create table order_tb(
        _id integer primary key autoincrement,
        item_name text,
        item_price real,
        item_number real,
        user_id integer,
        foreign key (user_id) references user_tb(_id) )''')
c.close()
conn.close()

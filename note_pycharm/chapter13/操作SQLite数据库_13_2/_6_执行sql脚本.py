"""
    13.2.6 执行sql脚本
"""
import sqlite3

conn = sqlite3.connect('first.db')
c = conn.cursor()
c.executescript(
    """
        insert into user_tb values(null,'武松','3444','male');
        insert into user_tb values(null,'林冲','44444','male');
        create table item_tb(
            _id integer primary key autoincrement,
            name,
            price);
    """
)
conn.commit()
c.close()
conn.close()

"""
    13.3.4 执行DML语句
"""
import mysql.connector

print(mysql.connector.apilevel)
print(mysql.connector.paramstyle)

conn = mysql.connector.connect(user='root', password='907256', host='localhost', port='3306',
                               database='python', use_unicode=True)
c = conn.cursor()

# c.execute('insert into user_tb values(null,%s,%s,%s)', ('猪八戒', '123456', 'male'))
# c.execute('insert into order_tb values(null,%s,%s,%s,%s)', ('鼠标', '34.2', '3', 8))

# 重复执行一条sql语句
c.executemany('insert into user_tb values(null,%s,%s,%s)',
              (
                  ('sun', '123456', 'male'),
                  ('bai', '123456', 'female'),
                  ('zhu', '123456', 'male'),
                  ('niu', '123456', 'male'),
                  ('tang', '123456', 'male'),
              ))

conn.commit()
c.close()
conn.close()

"""
    13.3.5 执行查询语句

"""
import mysql.connector

print(mysql.connector.apilevel)
print(mysql.connector.paramstyle)

conn = mysql.connector.connect(user='root', password='907256', host='localhost', port='3306',
                               database='python', use_unicode=True)
c = conn.cursor()

c.execute('select * from user_tb where user_id > %s', (2,))

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

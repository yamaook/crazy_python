"""
    13.3.6  调用存储过程
"""
import mysql.connector

print(mysql.connector.apilevel)
print(mysql.connector.paramstyle)

conn = mysql.connector.connect(user='root', password='907256', host='localhost', port='3306',
                               database='python', use_unicode=True)
c = conn.cursor()
result_args = c.callproc('add_pro', (5, 6, 0))
print(result_args)
print(result_args[2])

c.close()
conn.close()

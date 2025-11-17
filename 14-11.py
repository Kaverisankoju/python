import mysql.connector
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Kaveri@123',
    database = '56r',
    port = 3306,
    autocommit = False
)
print(conn.is_connected())
curs = conn.cursor()
try:
    curs.execute('''insert into emp1 (id,name,job_role,salary)
                values(%s, %s, %s, %s)''',(12,'Rammurthy','IT',100000))
    curs.execute('''update emp1 set salary = %s where id = %s''',(60000,2))
except mysql.connector.Error as e:
    print("Error Occured",e)
    conn.rollback()
else:
    print("Insert Successfull!")
    conn.commit()
finally:
    curs.close()
    conn.close()


# conn.commit()
# conn.close()
# for i in curs.fetchall():
#     print(i)
    
# print(curs.fetchone())
    
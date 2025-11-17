import mysql.connector
import logging
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
    logging.basicConfig(filename="logging.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")
    curs.execute('''insert into emp1 (id,name,job_role,salary)
                values(%s, %s, %s, %s)''',(12,'Rammurthy','IT',100000))
    curs.execute('''update emp1 set salary = %s where id = %s''',(60000,2))
except mysql.connector.Error as e:
    print("Error Occured",e)
    conn.rollback()
    logging.error('SQL error...')
    
else:
    print("Insert Successfull!")
    logging.info('code runs successufully')
    conn.commit()
finally:
    curs.close()
    conn.close()


# conn.commit()
# conn.close()
# for i in curs.fetchall():
#     print(i)
    
# print(curs.fetchone())
    
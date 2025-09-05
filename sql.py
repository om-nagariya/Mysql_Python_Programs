import mysql.connector as sqlc
conn=sqlc.connect(host='localhost',user='root',passwd='mysql',database='school_management',charset 
="utf8")
if conn.is_connected():
 print("CONNECTED SUCCESSFULLY")
else:
 print("NOT CONNECTED")
def delete_Students():
 cursor=conn.cursor()
 rno=int(input('enter roll no of student to delete:'))
 query= cursor.execute('delete from student where rno={}'.format(rno))
 conn.commit()
 print('DELETED SUCCESSFULLY....')
delete_Students()

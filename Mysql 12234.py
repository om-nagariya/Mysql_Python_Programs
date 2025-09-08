#Hello guys kya kar rahe ho?
import mysql.connector as mysqltor
import tabulate as tb

mycon = mysqltor.connect(host = "localhost", user = "root", password = "root", database = "stu_data")
cursor = mycon.cursor()

cursor.execute("Select * from student_details order by srno")
row = cursor.fetchall()
headers = ("SrNo", "Admno", "Rollno", "Name", "Stream", "DOB", "Age", "Per", "Gender", "House", "Title")
data = tb.tabulate(row, headers = headers, tablefmt= "fancy_grid" )
print(data)

mycon.close()  
print("Bye")

print("Hi")
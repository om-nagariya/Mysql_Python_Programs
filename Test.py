import mysql.connector as my
from tabulate import tabulate

mycon = my.connect(host = "localhost", user = "root", passwd = "root", database = "stu_data")
cursor = mycon.cursor()

cursor.execute("SELECT * FROM STUDENT_DETAILS")
data = cursor.fetchall()

headers = ("SrNo", "Admno", "Rollno", "Name", "Stream", "DOB", "Age", "Per", "Gender", "House", "Title")

data_table = tabulate(data, headers = headers, tablefmt = "fancy_grid")

print(data_table)

mycon.close()  

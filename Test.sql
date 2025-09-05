import pandas as pd
import mysql.connector

# Read the CSV file
df = pd.read_csv('C:/Users/omnag/OneDrive/Documents/MS Excel/Students Marks 2.csv')

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='stu_data'
)
cursor = conn.cursor()

# Insert data into the stu_marks table
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO stu_marks (
            SrNo, admno, Rollno, Name, DOB, Class, Section,
            Maths, Biology, Physics, Chemistry, CS, Hindi, English, Total
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s
        )
        """,
        tuple(row)
    )

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data inserted successfully.")

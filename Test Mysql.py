import pandas as pd
import mysql.connector
from mysql.connector import Error

# Read the CSV file
df = pd.read_csv(r'C:/Users/omnag/OneDrive/Documents/MS Excel/Students Marks 2.csv')

# Ensure that column names have no leading or trailing whitespace
df.columns = df.columns.str.strip()

# Replace NaN with None for compatibility with SQL insertion
df = df.where(pd.notnull(df), None)

# Convert the Class column to integers (remove non-numeric characters)
df['Class'] = df['Class'].str.extract(r'(\d+)').astype(int)

try:
    # Connect to the MySQL database using root user
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # root user
        password='root',  # root password
        database='stu_data'  # stu_data database
    )
    
    if conn.is_connected():
        print("Connected to MySQL database")

        cursor = conn.cursor()

        # Prepare the SQL INSERT statement
        insert_stmt = """
        INSERT INTO stu_marks (
            SrNo, admno, Rollno, Name, DOB, Class, Section,
            Maths, Biology, Physics, Chemistry, CS, Hindi, English, Total
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s
        )
        """

        # Insert data into the stu_marks table
        for _, row in df.iterrows():
            try:
                cursor.execute(insert_stmt, (
                    row['SrNo'], row['Admno'], row['Rollno'], row['Name'], 
                    row['DOB'], row['Class'], row['Section'], row['Maths'], 
                    row['Biology'], row['Physics'], row['Chemistry'], row['C.S.'], 
                    row['Hindi'], row['English'], row['Total']
                ))
            except Error as e:
                print(f"Error inserting row: {row}")
                print(f"Error message: {e}")

        # Commit the transaction
        conn.commit()
        print("Data inserted successfully.")

except Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")


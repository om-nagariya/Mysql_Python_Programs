import mysql.connector as my
import tabulate as tb
from tabulate import tabulate
mycon = my.connect(host = "localhost", user = "root", passwd = "root", database = "school_management")
cursor = mycon.cursor()



def show_students():
    cursor.execute("SELECT * FROM students ORDER BY Name")
    data = cursor.fetchall()
    headers = ("SrNo", "Admno", "RollNo", "Name", "Stream", "DOB",  "Gender", "House", "Title")
    data_table = tabulate(data, headers = headers, tablefmt = "fancy_grid")
    print(data_table)

def show_student_marks():
    cursor.execute("SELECT * FROM student_marks ORDER BY Name")
    data = cursor.fetchall()
    headers = ("SrNo", "Admno", "RollNo", "Name", "Class","Section", "Maths", "Biology", "Physics", "Chemistry", "CS", "Hindi", "English")
    data_table = tabulate(data, headers = headers, tablefmt = "fancy_grid")
    print(data_table)

def show_teachers():
    cursor.execute("SELECT * FROM teachers")
    data = cursor.fetchall()
    headers = ("SrNo", "ID", "Name", "Subject", "Post")
    data_table = tabulate(data, headers = headers, tablefmt = "fancy_grid")
    print(data_table)



print("""Welcome to Student Management System""")
while True:
    print("\t1. Admin login")
    print("\t2. Student login")
    print("\t3. Exit")
    choice = input("Enter your choice:")
    if choice == '1':  # Admin login
        print("\t\t\tAdmin Login Page")
        username = input("Enter username:")
        password = input("Enter password:")
        if username == "flame" and password == "root": #password is root
            print("Login successful")
            cursor.execute("SHOW TABLES")
            data = cursor.fetchall()
            data_table = tabulate(data, tablefmt = "fancy_grid")
            print(data_table)
    
            table = input("Choose a table to view/alter:")
            if table == "1":
                while True:
                    print("1. View student marks")
                    print("2. Alter student marks")
                    print("3. Exit")

                    choice = int(input("Enter your choice:"))
                    if choice == 1:
                        print("View student marks selected")
                        show_student_marks()
                    elif choice == 2:
                        print("Alter student marks selected")
                        while True:
                            print("Enter Operation to be performed:")
                            print("1. Add students marks")
                            print("2. Delete students marks")
                            print("3. Update students marks")
                            print("4. Exit")
                            choice = int(input("Enter your choice:"))
                            if choice == 1:
                                print("Add students marks selected")
                                srno = int(input("Enter srno:"))
                                admno = int(input("Enter admno:"))
                                rollno = int(input("Enter rollno:"))
                                name = input("Enter name:")
                                Class = int(input("Enter class:"))
                                section = input("Enter section:")
                                maths = int(input("Enter maths:"))
                                biology = int(input("Enter biology:"))
                                physics = int(input("Enter physics:"))
                                chemistry = int(input("Enter chemistry:"))
                                CS = int(input("Enter cs:"))
                                hindi = int(input("Enter hindi:"))
                                english = int(input("Enter english:"))
                            #i have to fix the option for maths biology and for cs hindi, handling null values

                                query = """
                                INSERT INTO student_marks (srno, admno, rollno, name, Class, section, maths, biology, physics, chemistry, CS, hindi, english)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """

#                               Create a tuple with the values to insert
                                values = (srno, admno, rollno, name, Class, section, maths, biology, physics, chemistry,CS,  hindi, english)

# Execute the query with the values
                                cursor.execute(query, values)
                                mycon.commit()
                                print("Record inserted successfully")
                                print("Current student marks:")
                                show_student_marks()
                                # show_students()   
                            elif choice == 2:
                                print("Delete students marks selected")
                                admno = int(input("Enter admno:"))
                                query = "DELETE FROM student_marks WHERE admno = {}".format(admno)
                                cursor.execute(query)
                                mycon.commit()
                                print("Record deleted successfully")
                                print("Current student marks:")
                                show_student_marks()
                                # show_students()
                            elif choice == 3:
                                print("Update students marks selected")
                                while True:
                                    print("Enter the field to update:")
                                    print("1. Update srno")
                                    print("2. Update admno")                           
                                    print("3. Update rollno")
                                    print("4. Update name")
                                    print("5. Update class")
                                    print("6. Update section")
                                    print("7. Update maths")     
                                    print("8. Update biology")
                                    print("9. Update physics")
                                    print("10. Update chemistry")
                                    print("11. Update cs")
                                    print("12. Update hindi")
                                    print("13. Update english")
                                    print("14. Exit")
                                    choice = int(input("Enter your choice:"))
                                    if choice == 1:
                                        print("Update admno selected")
                                        admno = int(input("Enter admno:"))
                                        new_srno = int(input("Enter new srno:"))
                                        query = "UPDATE student_marks SET srno = {} WHERE admno = {}".format(new_srno, admno)   
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        # show_students()
                                        show_student_marks()
                                    elif choice == 2:
                                        print("Update admno selected")
                                        admno = int(input("Enter admno:"))
                                        new_admno = int(input("Enter new admno:"))
                                        query = "UPDATE student_marks SET admno = {} WHERE admno = {}".format(new_admno, admno)   
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        show_student_marks()
                                    elif choice == 3:
                                        print("Update rollno selected")
                                        admno = int(input("Enter admno:"))
                                        new_rollno = int(input("Enter new rollno:"))
                                        query = "UPDATE student_marks SET rollno = {} WHERE admno = {}".format(new_rollno, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        # show_students()
                                        show_student_marks()
                                    elif choice == 4:
                                        print("Update name selected")
                                        admno = int(input("Enter admno:"))
                                        new_name = input("Enter new name:")
                                        query = "UPDATE student_marks SET name = '{}' WHERE admno = {}".format(new_name, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        # show_students()
                                        show_student_marks()
                                    elif choice == 5:
                                        print("Update class selected")
                                        admno = int(input("Enter admno:"))  
                                        new_class = input("Enter new class:")
                                        query = "UPDATE student_marks SET class = '{}' WHERE admno = {}".format(new_class, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        # show_students()
                                        show_student_marks()
                                    elif choice == 6:
                                        print("Update section selected")
                                        admno = int(input("Enter admno:"))
                                        new_section = input("Enter new section:")
                                        query = "UPDATE student_marks SET section = '{}' WHERE admno = {}".format(new_section, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        # show_students() 
                                        show_student_marks()
                                    elif choice == 7:
                                        print("Update maths selected")
                                        admno = int(input("Enter admno:"))
                                        new_maths = input("Enter new maths:")
                                        query = "UPDATE student_marks SET maths = '{}' WHERE admno = {}".format(new_maths, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        # show_students() 
                                        show_student_marks()
                                    elif choice == 8:
                                        print("Update biology selected")
                                        admno = int(input("Enter admno:"))
                                        new_biology = input("Enter new biology:")
                                        query = "UPDATE student_marks SET biology = '{}' WHERE admno = {}".format(new_biology, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        # show_students() 
                                        show_student_marks()
                                    elif choice == 9:
                                        print("Update physics selected")
                                        admno = int(input("Enter admno:"))
                                        new_physics = input("Enter new physics:")
                                        query = "UPDATE student_marks SET physics = '{}' WHERE admno = {}".format(new_physics, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        show_student_marks()
                                    elif choice == 10:
                                        print("Update chemistry selected")
                                        admno = int(input("Enter admno:"))
                                        new_chemistry = input("Enter new chemistry:")                                    
                                        query = "UPDATE student_marks SET chemistry = '{}' WHERE admno = {}".format(new_chemistry, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        show_student_marks()
                                    elif choice == 11:
                                        print("Update cs selected")
                                        admno = int(input("Enter admno:"))
                                        new_cs = input("Enter new cs:")
                                        query = "UPDATE student_marks SET cs = '{}' WHERE admno = {}".format(new_cs, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        show_student_marks()
                                    elif choice == 12:  
                                        print("Update hindi selected")
                                        admno = int(input("Enter admno:"))
                                        new_hindi = input("Enter new hindi:")
                                        query = "UPDATE student_marks SET hindi = '{}' WHERE admno = {}".format(new_hindi, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        show_student_marks()
                                    elif choice == 13:
                                        print("Update english selected")
                                        admno = int(input("Enter admno:"))
                                        new_english = input("Enter new english:")
                                        query = "UPDATE student_marks SET english = '{}' WHERE admno = {}".format(new_english, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student marks:")
                                        show_student_marks()
                                    elif choice == 14:
                                        print("Exit selected")
                                        print("Exiting program...")
                                        break
                                    else:
                                        print("Invalid choice. Please enter a valid option.")
                            elif choice == 4:
                                print("Exit selected")
                                print("Exiting program...")
                                break
                            else:
                                print("Invalid choice. Please enter a valid option.")
                    elif choice == 3:
                        print("Exit selected")
                        print("Exiting program...")
                        break
                    else:
                        print("Invalid choice")
            elif table == "2":
                while True:
                    print("1. View students marks")
                    print("2. Alter students marks")
                    print("3. Exit")

                    choice = int(input("Enter your choice:"))
                    if choice == 1:
                        print("View student marks selected")
                        show_student_marks()
                    elif choice == 2:
                        print("Alter student marks selected")
                        while True:
                            print("Enter the operation you want to perform")
                            print("1. Add student details")
                            print("2. Delete student details")
                            print("3. Update student details")
                            print("4. Exit")
                            choice = int(input("Enter your choice:"))
                            if choice == 1:
                                print("Add student details selected")
                                admno = int(input("Enter admno:"))
                                rollno = int(input("Enter rollno:"))
                                name = input("Enter name:")                               
                                class_ = input("Enter class:")
                                section = input("Enter section:")
                                maths = float(input("Enter maths marks:"))
                                biology = float(input("Enter biology marks:"))
                                physics = float(input("Enter physics marks:"))
                                chemistry = float(input("Enter chemistry marks:"))
                                cs = float(input("Enter cs marks:"))
                                hindi = float(input("Enter hindi marks:"))
                                english = float(input("Enter english marks:"))
                                query = "Insert into student_marks values({}, {}, '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {})".format(admno, rollno, name, class_, section, maths, biology, physics, chemistry, cs, hindi, english)
                                cursor.execute(query)
                                mycon.commit()
                                print("Record inserted successfully")
                                print("Current student details:")
                                show_student_marks()
                            elif choice == 2:
                                print("Delete student details selected")
                                admno = int(input("Enter admno :"))
                                query = "DELETE FROM student_marks WHERE admno = {}".format(admno)
                                cursor.execute(query)
                                mycon.commit()
                                print("Record deleted successfully")
                                print("Current student details:")
                                show_student_marks()
                            elif choice == 3:
                                print("Update student details selected")
                                while True:
                                    print("Enter the field you want to update")
                                    print("1. Update admno")
                                    print("2. Update rollno")                           
                                    print("3. Update name")
                                    print("4. Update class")
                                    print("5. Update section")
                                    print("6. Update maths")
                                    print("7. Update biology")
                                    print("8. Update physics")
                                    print("9. Update chemistry")
                                    print("10. Update cs")
                                    print("11. Update hindi")
                                    print("12. Update english")
                                    print("13. Exit")
                                    choice = int(input("Enter your choice:"))
                                    if choice == 1:
                                        print("Update admno selected")
                                        admno = int(input("Enter admno:"))
                                        new_admno = int(input("Enter new admno:"))
                                        query = "UPDATE student_marks SET admno = '{}' WHERE admno = {}".format(new_admno, admno)   
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 2:
                                        print("Update rollno selected.")
                                        admno = int(input("Enter admno:"))
                                        new_rollno = int(input("Enter new rollno:"))
                                        query = "UPDATE student_marks SET rollno = '{}' WHERE admno = {}".format(new_rollno, admno)                
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 3:
                                        print("Update name selected.")
                                        admno = int(input("Enter admno:"))
                                        new_name = input("Enter new name:")
                                        query = "UPDATE student_marks SET name = '{}' WHERE admno = {}".format(new_name, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 4:
                                        print("Update class selected.")
                                        admno = int(input("Enter admno:"))
                                        new_class = input("Enter new class:")
                                        query = "UPDATE student_marks SET class = '{}' WHERE admno = {}".format(new_class, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 5:
                                        print("Update section selected.")
                                        admno = int(input("Enter admno:"))
                                        new_section = input("Enter new section:")
                                        query = "UPDATE student_marks SET section = '{}' WHERE admno = {}".format(new_section, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 6:
                                        print("Update maths selected.")
                                        admno = int(input("Enter admno:"))
                                        new_maths = float(input("Enter new maths marks:"))
                                        query = "UPDATE student_marks SET maths = '{}' WHERE admno = {}".format(new_maths, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 7:
                                        print("Update biology selected.")
                                        admno = int(input("Enter admno:"))
                                        new_biology = float(input("Enter new biology marks:"))
                                        query = "UPDATE student_marks SET biology = '{}' WHERE admno = {}".format(new_biology, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 8:
                                        print("Update physics selected.")
                                        admno = int(input("Enter admno:"))
                                        new_physics = float(input("Enter new physics marks:"))
                                        query = "UPDATE student_marks SET physics = '{}' WHERE admno = {}".format(new_physics, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 9:
                                        print("Update chemistry selected.")
                                        admno = int(input("Enter admno:"))
                                        new_chemistry = float(input("Enter new chemistry marks:"))
                                        query = "UPDATE student_marks SET chemistry = '{}' WHERE admno = {}".format(new_chemistry, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 10:
                                        print("Update cs selected.")
                                        admno = int(input("Enter admno:"))
                                        new_cs = float(input("Enter new cs marks:"))
                                        query = "UPDATE student_marks SET cs = '{}' WHERE admno = {}".format(new_cs, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 11:
                                        print("Update hindi selected.")
                                        admno = int(input("Enter admno:"))
                                        new_hindi = float(input("Enter new hindi marks:"))
                                        query = "UPDATE student_marks SET hindi = '{}' WHERE admno = {}".format(new_hindi, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 12:
                                        print("Update english selected.")
                                        admno = int(input("Enter admno:"))
                                        new_english = float(input("Enter new english marks:"))
                                        query = "UPDATE student_marks SET english = '{}' WHERE admno = {}".format(new_english, admno)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record updated successfully")
                                        print("Current student details:")
                                        show_student_marks()
                                    elif choice == 13:
                                        print("Exit selected.")
                                        print("Exiting program...")
                                        break
                                    else:
                                        print("Invalid choice. Please try again.")          
                            elif choice == 4:
                                print("Exit selected.")
                                print("Exiting program...")
                                break
                            else:
                                print("Invalid choice. Please try again.")
                    elif choice == 3:
                        print("Exit selected." )
                        print("Exiting program...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            elif table == "3":
                print("2. Teachers selected.")
                while True:
                    print("1. View teacher details")
                    print("2. Alter teacher details")
                    print("3. Exit")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        print("View teacher details selected.")
                        show_teachers()
                    elif choice == 2:
                        print("Alter teacher details selected.")
                        while True:
                            print("Enter the option you want to perform:")
                            print("1. Add new teacher")
                            print("2. Delete teacher details")
                            print("3. Update teacher details")
                            print("4. Exit")
                            choice = int(input("Enter your choice: "))
                            if choice == 1:
                                print("1. Add new teacher selected.")
                                show_teachers()
                            elif choice == 2:
                                print("Delete teacher details selected.")
                                id = int(input("Enter ID of the teacher you want to delete: "))
                                query = "DELETE FROM teachers WHERE id = {}".format(id)
                                cursor.execute(query)
                                mycon.commit()
                                print("Record deleted successfully")
                                print("Current teacher details:")
                                show_teachers()
                            elif choice == 3: 
                                print("Update teacher details selected.")  
                                while True:
                                    print("1. Add Teacher Details")
                                    print("2. Delete Teacher Details")
                                    print("3. Update Teacher Details")
                                    print("4. Exit")
                                    choice = int(input("Enter your choice: "))
                                    if choice == 1:
                                        print("Add Teacher Details selected.")
                                        srno = int(input("Enter SrNo:"))
                                        id = int(input("Enter ID:"))
                                        name = input("Enter Name:")
                                        subject = input("Enter Subject:")
                                        qualification = input("Enter Qualification:")
                                        post = input("Enter Post:")
                                        query = "INSERT INTO teachers(srno,id,name,subject,qualification,post) VALUES('{}','{}','{}','{}','{}','{}')".format(srno,id,name,subject,qualification,post)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record inserted successfully")
                                        print("Current teacher details:")
                                        show_teachers()
                                    elif choice == 2:
                                        print("Delete Teacher Details selected.")
                                        id= input("Enter admno to delete:")
                                        query = "DELETE FROM teachers WHERE id = '{}'".format(id)
                                        cursor.execute(query)
                                        mycon.commit()
                                        print("Record deleted successfully")
                                        print("Current teacher details:")
                                        show_teachers()
                                    elif choice == 3:
                                        print("Update Teacher Details selected.")
                                        while True:
                                            print("Enter the option you want to perform:")
                                            print("1. Update Srno")
                                            print("2. Update ID")
                                            print("3. Update Name")
                                            print("4. Update Subject")
                                            print("5. Update Qualification")
                                            print("6. Update Post")
                                            print("7. Exit")
                                            choice = int(input("Enter your choice: "))
                                            if choice == 1:
                                                print("Update Srno selected.")
                                                id = int(input("Enter the id of the teacher whose Srno is to be updated:"))
                                                new_srno = int(input("Enter the new Srno:"))
                                                query = "UPDATE teachers SET srno = '{}' WHERE id = {}".format(new_srno, id)
                                                cursor.execute(query)
                                                mycon.commit()
                                                print("Record updated successfully")
                                                print("Current teacher details:")
                                                show_teachers()
                                            elif choice == 2:
                                                print("Update ID selected.")
                                                id = int(input("Enter the id of the teacher whose ID is to be updated:"))
                                                new_id = int(input("Enter the new ID:"))
                                                query = "UPDATE teachers SET id = '{}' WHERE id = {}".format(new_id, id)
                                                cursor.execute(query)
                                                mycon.commit()
                                                print("Record updated successfully")
                                                print("Current teacher details:")
                                                show_teachers()
                                            elif choice == 3:
                                                print("Update Name selected.")
                                                id = int(input("Enter the id of the teacher whose Name is to be updated:"))
                                                new_name = input("Enter the new Name:")
                                                query = "UPDATE teachers SET name = '{}' WHERE id = {}".format(new_name, id)
                                                cursor.execute(query)
                                                mycon.commit()
                                                print("Record updated successfully")
                                                print("Current teacher details:")
                                                show_teachers()
                                            elif choice == 4:
                                                print("Update Subject selected.")
                                                id = int(input("Enter the id of the teacher whose Subject is to be updated:"))
                                                new_subject = input("Enter the new Subject:")
                                                query = "UPDATE teachers SET subject = '{}' WHERE id = {}".format(new_subject, id) 
                                                cursor.execute(query)
                                                mycon.commit()
                                                print("Record updated successfully")
                                                print("Current teacher details:")
                                                show_teachers()
                                            elif choice == 5:
                                                print("Update Qualification selected.")
                                                id = int(input("Enter the id of the teacher whose Qualification is to be updated:"))
                                                new_qualification = input("Enter the new Qualification:")
                                                query = "UPDATE teachers SET qualification = '{}' WHERE id = {}".format(new_qualification, id)
                                                cursor.execute(query)
                                                mycon.commit()
                                                print("Record updated successfully")
                                                print("Current teacher details:")
                                                show_teachers()
                                            elif choice == 6:
                                                print("Update Post selected.")
                                                id = int(input("Enter the id of the teacher whose Post is to be updated:"))
                                                new_post = input("Enter the new Post:")
                                                query = "UPDATE teachers SET post = '{}' WHERE id = {}".format(new_post, id)
                                                cursor.execute(query)
                                                mycon.commit()
                                                print("Record updated successfully")
                                                print("Current teacher details:")
                                                show_teachers()
                                            elif choice == 7:
                                                print("Exit selected.")
                                                print("Exiting program...")
                                                break
                                            else:
                                                print("Invalid choice. Please enter a valid option.")
                                    elif choice == 4:
                                        print("Exit selected.")
                                        print("Exiting program...")
                                        break
                                    else:
                                        print("Invalid choice. Please enter a valid option.")
                    elif choice == 3:
                        print("Exit selected.")
                        print("Exiting program...")
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")                                            
            else:
                print("Invalid choice. Please enter a valid option.")
        else:
            print("Wrong password. Please try again.")
    elif choice == '2': #Student login...
        print("\t\t\tStudent Login Page")
        admno = int(input("Enter admno: "))
        print("What operation do you want to perform?")
        while True:
            print("1. View Your Details")
            print("2. View Your Marks")
            print("3. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("View Your Details selected.")
                print("Your details are:")
                data = "SELECT * FROM students WHERE admno = '{}'".format(admno)
                cursor.execute(data)
                records = cursor.fetchall()
                headers = ("SrNo", "Admno", "RollNo", "Name", "Stream", "DOB",  "Gender", "House", "Title")
                data_table = tabulate(records, headers = headers, tablefmt = "fancy_grid")
                print(data_table)
            elif choice == 2:
                print("View Your Marks selected.")
                query = "SELECT * FROM student_marks WHERE admno = '{}'".format(admno)
                cursor.execute(query)
                records = cursor.fetchall()
                print("Your marks are:")                
                headers = ("SrNo", "Admno", "RollNo", "Name", "Class","Section", "Maths", "Biology", "Physics", "Chemistry", "CS", "Hindi", "English")
                data_table = tabulate(records, headers = headers, tablefmt = "fancy_grid")
                print(data_table)
            elif choice == 3:
                print("Exit selected.")
                print("Exiting program...")
                break
            else:   
                print("Invalid choice. Please enter a valid option.")
    elif choice == '3':
        print("Exit selected.")
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

mycon.close()  

        

                                        
                                                 
                                
    




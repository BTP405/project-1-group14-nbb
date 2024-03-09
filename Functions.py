# Import required libraries
import mysql.connector as mysql
from tabulate import tabulate

# Database password
mysql_password = 'Jui#1510'

# Connect to MySQL
db_connection = mysql.connect(host='localhost', user='root', passwd=mysql_password, auth_plugin='mysql_native_password')
db_cursor = db_connection.cursor()


# Create the database and tables if they don't exist
def create_database_and_tables():
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS coaching")
    db_cursor.execute("USE coaching")

    # Creating Tables
    tables = [
        "CREATE TABLE IF NOT EXISTS student(name varchar(50), class varchar(2), roll int(2), address varchar(100), phone varchar(11))",
        "CREATE TABLE IF NOT EXISTS teacher(name varchar(50), tcode int(10), salary int(10), address varchar(100), phone varchar(11))",
        "CREATE TABLE IF NOT EXISTS CIAttendance(class varchar(5), classT varchar(50), classS int(3), date varchar(20), Absentees int(3))",
        "CREATE TABLE IF NOT EXISTS subjects(subID int(10), title varchar(20), cost varchar(10), timings varchar(30), duration varchar(30))"
    ]

    for table in tables:
        db_cursor.execute(table)


# Add Student
def add_student():
    n = input("Student name: ")
    cl = input("Class: ")
    r = int(input("Roll no: "))
    a = input("Address: ")
    ph = input("Phone: ")
    data = (n, cl, r, a, ph)
    sql = 'INSERT INTO student VALUES (%s, %s, %s, %s, %s)'
    db_cursor.execute(sql, data)
    db_connection.commit()
    print("Data entered successfully")
    print("")
    main()


# Remove Student
def remove_student():
    cl = input("Class: ")
    r = int(input("Roll no: "))
    data = (cl, r)
    sql = 'DELETE FROM student WHERE class=%s AND roll=%s'
    db_cursor.execute(sql, data)
    db_connection.commit()
    print("Data Updated")
    print("")
    main()


# Display Student Data
def display_student():
    cl = input("Class: ")
    data = (cl,)
    sql = 'SELECT * FROM student WHERE class=%s'
    db_cursor.execute(sql, data)
    student_data = db_cursor.fetchall()
    print("")
    header = ["Name", "Class", "Roll no.", "Address", "Phone Number"]
    print(tabulate(student_data, headers=header))
    print("")
    main()


# Add Teacher
def add_teacher():
    tcode = int(input("TCode: "))
    n = input("Teacher name: ")
    s = int(input("Salary: "))
    a = input("Address: ")
    ph = input("Phone: ")
    data = (n, tcode, s, a, ph)
    sql = 'INSERT INTO teacher VALUES (%s, %s, %s, %s, %s)'
    db_cursor.execute(sql, data)
    db_connection.commit()
    print("Data entered successfully")
    print("")
    main()


# Remove Teacher
def remove_teacher():
    tcode = int(input("Tcode: "))
    name = input("Teacher: ")
    data = (tcode, name)
    sql = 'DELETE FROM teacher WHERE tcode=%s AND name=%s'
    db_cursor.execute(sql, data)
    db_connection.commit()
    print("Data Removed")
    print("")
    main()


# Update Salary
def update_salary():
    n = input("Teacher: ")
    tcode = int(input("Tcode: "))
    salary = int(input("Salary: "))
    data = (salary, n, tcode)
    sql = 'UPDATE teacher SET salary=%s WHERE name=%s AND tcode=%s'
    db_cursor.execute(sql, data)
    db_connection.commit()
    print("Data Updated")
    print("")
    main()


# Display Teacher Data
def display_teacher():
    sql = 'SELECT * FROM teacher'
    db_cursor.execute(sql)
    teacher_data = db_cursor.fetchall()
    print("")
    header = ["Name", "Teacher Code", "Salary", "Address", "Phone Number"]
    print(tabulate(teacher_data, headers=header))
    print("")
    main()


# Class Attendance
def class_attendance():
    c = input("Class: ")
    clt = input("Class teacher: ")
    t = int(input("Class strength: "))
    d = input("Date: ")
    ab = int(input("No of absentees: "))
    data = (c, clt, t, d, ab)
    sql = 'INSERT INTO CIAttendance VALUES (%s, %s, %s, %s, %s)'
    db_cursor.execute(sql, data)
    db_connection.commit()
    print("Data entered successfully")
    print("")
    main()


# Display Class Attendance
def display_class_attendance():
    sql = 'SELECT * FROM CIAttendance'
    db_cursor.execute(sql)
    attendance_data = db_cursor.fetchall()
    print("")
    header = ["Class", "Class Teacher", "Total Students", "Date", "Absentees"]
    print(tabulate(attendance_data, headers=header))
    print("")
    main()


# Add Subject
def add_subject():
    bid = int(input("Subject id: "))
    t = input("Title: ")
    a = input("Cost: ")
    p = input("Timings: ")
    g = input("Duration: ")
    data = (bid, t, a, p, g)
    sql = 'INSERT INTO subjects VALUES (%s, %s, %s, %s, %s)'
    db_cursor.execute(sql, data)
    db_connection.commit()
    print("Data entered successfully")
    print("")
    main()


# Remove Subject
def remove_subject():
    t = input("Title: ")
    data = (t,)
    sql = 'DELETE FROM subjects WHERE title=%s'
    db_cursor.execute(sql, data)
    db_connection.commit()
    print("Data Removed")
    print("")
    main()


# Display Subject Data
def display_subject():
    sql = 'SELECT * FROM subjects'
    db_cursor.execute(sql)
    subject_data = db_cursor.fetchall()
    print("")
    header = ["Subject ID", "Title", "Cost", "Timing", "Duration"]
    print(tabulate(subject_data, headers=header))
    print("")
    main()


# Main function
def main():
    ch = 'y'
    while ch.lower() == 'y':
        print("Coaching Management System")
        print("1. Student")
        print("2. Teacher")
        print("3. Class Attendance")
        print("4. Subject")
        table = int(input("Enter table no: "))
        print("")
        if table == 1:
            op = 'y'
            while op.lower() == 'y':
                print("1. Add student")
                print("2. Remove student")
                print("3. Display student details")
                task = int(input("Enter task no: "))
                if task == 1:
                    add_student()
                elif task == 2:
                    remove_student()
                elif task == 3:
                    display_student()
                else:
                    print("Enter Valid Choice!!")
                op = input("Continue in this table (y/n): ")

        elif table == 2:
            op = 'y'
            while op.lower() == 'y':
                print("1. Add teacher")
                print("2. Remove teacher")
                print("3. Update Salary")
                print("4. Display teacher details")
                task = int(input("Enter task no: "))
                if task == 1:
                    add_teacher()
                elif task == 2:
                    remove_teacher()
                elif task == 3:
                    update_salary()
                elif task == 4:
                    display_teacher()
                else:
                    print("Enter Valid Choice!!")
                op = input("Continue in this table (y/n): ")

        elif table == 3:
            op = 'y'
            while op.lower() == 'y':
                print("1. Class Attendance")
                print("2. Display Class Attendance details")
                task = int(input("Enter task no: "))
                if task == 1:
                    class_attendance()
                elif task == 2:
                    display_class_attendance()
                else:
                    print("Enter Valid Choice!!")
                op = input("Continue in this table (y/n): ")

        elif table == 4:
            op = 'y'
            while op.lower() == 'y':
                print("1. Add Subject")
                print("2. Remove Subject")
                print("3. Display Subject details")
                task = int(input("Enter task no: "))
                if task == 1:
                    add_subject()
                elif task == 2:
                    remove_subject()
                elif task == 3:
                    display_subject()
                else:
                    print("Enter Valid Choice!!")
                op = input("Continue in this table (y/n): ")
        else:
            print("ENTER VALID CHOICE!!")
        ch = input("Do you want to continue (y/n): ")

    db_cursor.close()
    db_connection.close()


if __name__ == "__main__":
    create_database_and_tables()
    main()

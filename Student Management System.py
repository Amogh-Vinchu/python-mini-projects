# Student Management System in Python

students = []

#  ADD STUDENT

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    course = input("Enter Course: ")

    student = {
        "Name": name,
        "Roll": roll,
        "Course": course
    }

    students.append(student)
    print("\n Student Added Successfully!\n")


#  VIEW STUDENTS

def view_students():

    if len(students) == 0:
        print("\n No Students Found!\n")

    else:
        print("\n------ STUDENT RECORDS ------")

        for student in students:
            print(f"Name   : {student['Name']}")
            print(f"Roll   : {student['Roll']}")
            print(f"Course : {student['Course']}")
            print("-----------------------------")


#  SEARCH STUDENT 

def search_student():

    roll = input("Enter Roll Number to Search: ")

    found = False

    for student in students:

        if student["Roll"] == roll:

            print("\n Student Found")
            print(f"Name   : {student['Name']}")
            print(f"Roll   : {student['Roll']}")
            print(f"Course : {student['Course']}")

            found = True
            break

    if not found:
        print("\n Student Not Found!")


#  UPDATE STUDENT 

def update_student():

    roll = input("Enter Roll Number to Update: ")

    found = False

    for student in students:

        if student["Roll"] == roll:

            print("\nEnter New Details")

            student["Name"] = input("New Name: ")
            student["Course"] = input("New Course: ")

            print("\n✅ Student Updated Successfully!")

            found = True
            break

    if not found:
        print("\n Student Not Found!")


#  DELETE STUDENT 

def delete_student():

    roll = input("Enter Roll Number to Delete: ")

    found = False

    for student in students:

        if student["Roll"] == roll:

            students.remove(student)

            print("\n Student Deleted Successfully!")

            found = True
            break

    if not found:
        print("\n Student Not Found!")


#  MAIN MENU 

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\n Thank You for Using the System!")
        break

    else:
        print("\n Invalid Choice! Please Try Again.")
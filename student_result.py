students = []


def add_student():
    name = input("Enter your Name: ")
    roll_num = int(input("Enter your Roll Number: "))

    python = int(input("Enter your Python Mark: "))
    english = int(input("Enter your English Mark: "))
    maths = int(input("Enter your Maths Mark: "))

    total = python + english + maths
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "roll_num": roll_num,
        "python": python,
        "english": english,
        "maths": maths,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("\nStudent added successfully!")



def view_students():
    if len(students) == 0:
        print("\nNo students found.")
    else:
        for student in students:
            print("\n========== STUDENT RESULT ==========")
            print("Name        :", student["name"])
            print("Roll Number :", student["roll_num"])
            print("Python      :", student["python"])
            print("English     :", student["english"])
            print("Maths       :", student["maths"])
            print("Total       :", student["total"])
            print("Average     :", round(student["average"], 2))
            print("Grade       :", student["grade"])


def search_student():
    roll_num = int(input("Enter Roll Number to search: "))

    found = False

    for student in students:
        if student["roll_num"] == roll_num:
            print("\n========== STUDENT FOUND ==========")
            print("Name        :", student["name"])
            print("Roll Number :", student["roll_num"])
            print("Python      :", student["python"])
            print("English     :", student["english"])
            print("Maths       :", student["maths"])
            print("Total       :", student["total"])
            print("Average     :", round(student["average"], 2))
            print("Grade       :", student["grade"])

            found = True
            break

    if found == False:
        print("\nStudent not found.")


def delete_student():
    roll_num = int(input("Enter Roll Number to delete: "))

    for student in students:
        if student["roll_num"] == roll_num:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


while True:

    print("\n==========================================")
    print("     STUDENT RESULT MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice. Please try again.")
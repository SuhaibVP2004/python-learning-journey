Student_name = str(input("Enter your Name: "))
Roll_number = str(input("Enter your Roll Number: "))
Python_mark = float(input("Enter your Python Mark: "))
Maths_mark = float(input("Enter your Maths Mark: "))
English_mark = float(input("Enter your English Mark: "))

Total_mark = Python_mark + Maths_mark + English_mark
average_mark = Total_mark / 3

print("\n")
print("=" * 50)
print("        STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 50)

print("Student Name      :", Student_name)
print("Roll Number       :", Roll_number)
print("-" * 50)

print("Python Mark       :", Python_mark)
if Python_mark >= 90:
    print("Grade             : A+")
elif Python_mark >= 80:
    print("Grade             : A")
elif Python_mark >= 70:
    print("Grade             : B+")
elif Python_mark >= 60:
    print("Grade             : B")
elif Python_mark >= 50:
    print("Grade             : C+")
elif Python_mark >= 40:
    print("Grade             : C")
else:
    print("Grade             : FAIL")

print("-" * 50)

print("Maths Mark        :", Maths_mark)
if Maths_mark >= 90:
    print("Grade             : A+")
elif Maths_mark >= 80:
    print("Grade             : A")
elif Maths_mark >= 70:
    print("Grade             : B+")
elif Maths_mark >= 60:
    print("Grade             : B")
elif Maths_mark >= 50:
    print("Grade             : C+")
elif Maths_mark >= 40:
    print("Grade             : C")
else:
    print("Grade             : FAIL")

print("-" * 50)

print("English Mark      :", English_mark)
if English_mark >= 90:
    print("Grade             : A+")
elif English_mark >= 80:
    print("Grade             : A")
elif English_mark >= 70:
    print("Grade             : B+")
elif English_mark >= 60:
    print("Grade             : B")
elif English_mark >= 50:
    print("Grade             : C+")
elif English_mark >= 40:
    print("Grade             : C")
else:
    print("Grade             : FAIL")

print("=" * 50)
print("Total Marks       :", Total_mark)
print("Average Marks     :", round(average_mark, 2))

if Python_mark >= 40 and Maths_mark >= 40 and English_mark >= 40:
    print("Result            : PASS ✅")
else:
    print("Result            : FAIL ❌")

print("=" * 50)
print("        THANK YOU")
print("=" * 50)
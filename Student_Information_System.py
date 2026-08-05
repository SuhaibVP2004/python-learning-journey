# Student Information System

student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
age = int(input("Enter Age: "))
place = input("Enter Place: ")

python_mark = float(input("Enter Python Mark: "))
english_mark = float(input("Enter English Mark: "))
maths_mark = float(input("Enter Maths Mark: "))

total_mark = python_mark + english_mark + maths_mark
average_mark = total_mark / 3

print("\n" + "=" * 50)
print("        STUDENT INFORMATION SYSTEM")
print("=" * 50)

print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("Age          :", age)
print("Place        :", place)

print("-" * 50)

print("Python Mark  :", python_mark)
print("English Mark :", english_mark)
print("Maths Mark   :", maths_mark)

print("-" * 50)

print("Total Mark   :", total_mark)
print("Average Mark :", round(average_mark, 2))

print("=" * 50)
print("Thank You")
print("=" * 50)